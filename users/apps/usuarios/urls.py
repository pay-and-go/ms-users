from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.usuarios.views import UserList
from apps.usuarios.views import UserDetail
from apps.usuarios.views import LogList
from apps.usuarios.views import registration_view, detail_view, update_view, delete_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('log/', LogList.as_view()),
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('detail/<username>', detail_view, name='detail'),
    path('update/<username>', update_view, name='update'),
    path('delete/<username>', delete_view, name='delete'),
    #path('login', UserDetail.login),
]

urlpatterns = format_suffix_patterns(urlpatterns)