from django.urls import path
from . import views
from store import views as store_views

urlpatterns = [
    path('', store_views.index, name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
]
