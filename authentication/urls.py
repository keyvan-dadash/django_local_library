from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_site,logout_site
from django.contrib.auth.urls import views

app_name = 'authentication'
urlpatterns = [
    path('login/', login_site, name='login'),
    path('logout/', logout_site, name='logout'),
    path('password_reset/', views.PasswordResetView.as_view(template_name='authentication/password_reset_form.html'), name='password_reset'),
    path('password_reset/done',views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    path('password_change/',views.PasswordChangeView.as_view(), name='password_change'),
]
