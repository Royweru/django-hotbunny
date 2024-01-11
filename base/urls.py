
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('escort/<str:pk>/',views.individual_escort,name='view-escort')
]
