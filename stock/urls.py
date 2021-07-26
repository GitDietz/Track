from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views

from .views import test_db

app_name = 'stock'
urlpatterns = [
    # path('about', about, name='about'),
    # path('base', base, name='base'),
    # re_path('code/(?P<pk>\d+)', code_detail, name='code_detail'),
    # path('code_list', code_list, name='code_list'),
    # re_path('code_file/(?P<pk>\d+)', code_file, name='code_file'),
    # path('contact', contact, name='contact'),
    # path('blog', blog, name='blog'),
    # re_path('feature/(?P<pk>\d+)', feature_detail, name='feature_detail'),
    # path('feature_new', feature_new, name='feature_new'),
    # path('feature_list', feature_list, name='feature_list'),
    # path('home', home, name='home'),
    # path('pdf', pdf, name='pdf'),
    # path('services', services, name='services'),
    path('test_db', test_db, name='test_db'),
    # path('test_multi', test_multi, name='test_multi'),
    # re_path('article/(?P<pk>\d+)', show_pdf, name='show_pdf'),

    ]
