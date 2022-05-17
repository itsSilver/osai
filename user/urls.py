from django.urls import path
from user.views import login_user, Register_Users, User_logout,user_detail


app_name = 'user'

urlpatterns = [

    path("login", login_user),
    path('register', Register_Users, name='auth_register'),
    path('logout', User_logout, name='auth_logout'),
    path('detail', user_detail, name='auth_detail'),
]
