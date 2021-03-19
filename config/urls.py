from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('',include('pages.urls')),
    path('articles/', include('articles.urls')),
    path('utente/<int:id>/', views.byId, name='by_id'),


]
