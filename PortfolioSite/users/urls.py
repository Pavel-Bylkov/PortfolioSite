from users import views
from django.urls import path


urlpatterns = [
    path('register', views.SignUp.as_view(), name='signup'),
    path('logout', views.LogoutView.as_view(), name='logout')

]
