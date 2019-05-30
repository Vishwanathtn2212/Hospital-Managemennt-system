from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views  import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':'accounts:login'}, name='logout'),
    url(r"signup/$",views.SignUp.as_view(),name="signup"),
]
