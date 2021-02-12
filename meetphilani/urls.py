from django.urls import path
from . import views
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

app_name = 'meetphilani'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    url(r'^download/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT})
]
