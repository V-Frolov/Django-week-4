from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterFormView.as_view(), name='register'),   # Create new user
    path('login/', views.LoginFormView.as_view(), name='login'),            # Login into site
    path('logout/', views.LogoutFormView.as_view(), name='logout'),         # Logout
]
