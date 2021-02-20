from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('blog', views.blog, name='blog'),
    path('bookReservation', views.bookReservation),
    path('contact', views.contact),
    path('feedback', views.feedback)
]
