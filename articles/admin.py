from django.contrib import admin
from .models import Article, Ipp


class PostModelAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['author','hash']


admin.site.register(Article,PostModelAdmin)
admin.site.register(Ipp)

