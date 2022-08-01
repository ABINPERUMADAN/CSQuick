
from django.urls import path

from . import views

urlpatterns=[
    path('',views.home),
    path('sign/',views.signin),
    path('main/<str:uname1>',views.main,name='main'),
    path('logout/',views.logout),
    path('library/',views.library1),
    path('laptop/',views.laptop1),
    path('searchbooks/',views.searchbooks,name='searchbooks'),
    path('book_status/<str:bookname>',views.book_status),
   
]