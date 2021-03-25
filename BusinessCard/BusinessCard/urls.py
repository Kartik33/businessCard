from django.contrib import admin
from django.urls import path

from user_profile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('users/<int:user_id>/', views.users, name='users'),
    path('signup/', views.sign_up, name='sign_up'),
    path('getToken/', views.getToken,name='getToken'),
    path('login/',views.login_user,name='login_user'),
    path('logout/', views.logout_user,name='logout_user'),
]
