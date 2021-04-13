from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.usuarios.views import UserList
from apps.usuarios.views import UserDetail
from apps.usuarios.views import LogList

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('log/', LogList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)