from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('lockscreen', views.auth_lockscreen, name='auth_lockscreen'),
    path('login', views.login_view, name='auth_login'),
    path('register', views.auth_register, name='auth_register'),
    path('logout',views.auth_logout,name='auth_logout'),
    path('password_change',views.auth_password_change,name='auth_password_change'),
    path('password_change/done',views.auth_password_change_done,name='auth_password_change_doone'),
    path('password_reset',views.auth_password_reset,name='auth_password_reset'),
    path('password_reset/done',views.auth_password_reset_done,name='auth_password_reset_done'),
    path('reset/<uidb64>/<token>',views.reset,name='auth_password_reset_confirm'),
    path('reset/complete',views.reset_complete,name='auth_password_reset_complete'),
]