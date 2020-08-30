from django.conf.urls import url
from loginapp import views

app_name='loginapp'

urlpatterns = [
        url("signup/", views.signup, name="signup"),
        url("user_login/", views.user_login, name="user_login"),
]
