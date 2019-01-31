from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('add_category/', views.add_category, name='add_category'),
    # path('register/',views.register, name='register'),
    # path('login/',views.user_login, name='login'),
    re_path('category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),  # New!
    re_path('category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    # path('logout/', views.user_logout, name='logout'),
]