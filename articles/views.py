from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.contrib.auth.models import User
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view


from .forms import ArticleModelForm
from .models import Article, Ipp
from .serializers import lasthourpostsSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)






class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    queryset = Article.objects.order_by('-date')





class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'




class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@staff_member_required
def num_post(request):
    num_post = Article.objects.filter(author=request.user).count()
    user_posts = User.objects.annotate(total_posts=Count('articles'))
    return render(request, 'users_count_post.html', {'user_posts': user_posts})




@login_required
def article_create_view(request):
    if request.method == "POST":
        form=ArticleModelForm(request.POST)
        if form.is_valid():
            contenuto_check = request.POST.get("body")
            if "hack" in contenuto_check:
                raise ValidationError("Do not write hack")
            else:
                il_post=Article.objects.create(
                    author=request.user,
                    body=form.cleaned_data["body"]
                )
                post = Article.objects.latest()
                post.writeOnChain()
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ipaddress = x_forwarded_for.split(',')[-1].strip()
                else:
                    ipaddress = request.META.get('REMOTE_ADDR')
                get_ip = Ipp()  # imported class from model
                get_ip.ip_address = ipaddress
                get_ip.user = request.user
                get_ip.save()

                return HttpResponseRedirect(reverse('article_list'))
    else:
        form=ArticleModelForm()
    context={"form":form,"article": Article}
    return render(request,"article_new.html", context)

@cache_page(CACHE_TTL)
@staff_member_required
@api_view(['GET'])
def appearance(request):

    word = request.GET['search']
    all_p = Article.objects.all()
    counts=0
    for a in all_p:
        print(a.body)
        counts += a.body.count(word)
    print(counts)
    return Response(counts)


@cache_page(CACHE_TTL)
@staff_member_required
@api_view(['GET'])
def lasthourposts(request):
    one_h_ago = timezone.now() - timezone.timedelta(hours=1)

    queryset = Article.objects.filter(date__gte=one_h_ago)

    serializer_class = lasthourpostsSerializer(queryset, many=True)
    return Response(serializer_class.data)












