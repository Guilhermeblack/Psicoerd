from django.urls import path
from psicoerd import views

app_name='psicoerd'

urlpatterns =[
    path('',views.index, name="index"),
]