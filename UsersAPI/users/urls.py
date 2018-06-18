from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^users/search/', views.Users.as_view()),
    url(r'^users/', views.Users.as_view())
# url(r'^/users/$', views.Users.as_view()),
]
