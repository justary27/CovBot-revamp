from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.bots),
    path('features',views.features),
    path('commands',views.commands),
    path('tutorial',views.tutorial),
]
