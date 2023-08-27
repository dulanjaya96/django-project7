from django.urls import path
from first_app import views

#TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    # path('',views .user,name='user'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')

]