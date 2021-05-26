from django.urls import path

from adminapp.views import index, admin_users_create, admin_users_update, admin_users_remove
from adminapp.views import UserListView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('admin-users-remove/<int:user_id>/', admin_users_remove, name='admin_users_remove'),
]