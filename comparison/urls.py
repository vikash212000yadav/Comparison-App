from django.urls import path
from . import views

app_name = 'comparison'

urlpatterns = [
    path('', views.home, name='comp'),
    path('users/', views.all_users, name="user_list"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
]
