from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login_user"),
    path('user_profile/' , views.user_profile , name="user_profile"),
    path('logout_user/' , views.logout , name = "logout"), 
    path('reset_pass/' , views.reset_password , name = "reset_password")

]
