from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', views.login_user, name="login_user"),
    path('user_profile/' , views.user_profile , name="user_profile"),
    path('logout/' , views.logout_view , name = "logout"), 
    path('reset_pass/' , views.reset_password , name = "reset_password"),
    path('all_tasks/' ,  views.show_all_tasks , name = "all_tasks"), 
    

]
