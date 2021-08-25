from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.usuarios.views import UserList
from apps.usuarios.views import UserDetail
from apps.usuarios.views import LogList
from apps.usuarios.views import registration_view, detail_view, update_view, delete_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users-ms/user/', UserList.as_view()),
    path('users-ms/user/<int:pk>', UserDetail.as_view()),
    path('users-ms/log/', LogList.as_view()),
    path('users-ms/register/', registration_view, name='register'),
    path('users-ms/login/', obtain_auth_token, name='login'),
    path('users-ms/detail/<username>', detail_view, name='detail'),
    path('users-ms/update/<username>', update_view, name='update'),
    path('users-ms/delete/<username>', delete_view, name='delete'),
    #path('login', UserDetail.login),
]

urlpatterns = format_suffix_patterns(urlpatterns)