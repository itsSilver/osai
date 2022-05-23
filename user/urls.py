from django.urls import path

from user.views import login_user, Register_Users, User_logout, user_detail, permissions_list, get_users, \
    add_permission, user_delete, remove_permission, update_user, add_permission_to_user

app_name = 'user'

urlpatterns = [

    path("login", login_user),
    path('register', Register_Users, name='auth_register'),
    path('logout', User_logout, name='auth_logout'),
    path('detail', user_detail, name='user_detail'),
    path('users-list', get_users, name='users'),
    path('remove/<int:id>', user_delete, name='delete_user'),
    path('update/<int:id>', update_user, name='update_user'),

    path('add/permission/<int:id>', add_permission_to_user),

    path('permissions', permissions_list, name='permissions_list'),
    path('add_permission/<int:id>', add_permission, name='add_permission'),
    path('remove_permission/<int:id>', remove_permission) ]
