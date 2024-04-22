from django.urls import path
from .import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
     path('crop',views.crop,name='crop'),
    path('predict',views.predict,name='predict'),
     path('team',views.team,name='team'),
    path('contact',views.contact,name='contact')
]