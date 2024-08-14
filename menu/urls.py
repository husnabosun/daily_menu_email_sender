from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup_view, name='signup_view'),
    path('success/', views.success_view, name='success')

]
