from django.urls import path
from . import views
urlpatterns = [


    path('', views.play_list, name='play_list'),
    path('player/<str:id_play>/', views.play_detail, name='play_detail'),
    path('player/<str:id_play>/?<str:message>', views.play_detail, name='play_detail_mes'),

]