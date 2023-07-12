from django.urls import path  
from user_app import views as user_views
   
   
urlpatterns = [
    
    path("signup/", user_views.user_signup, name ="user_signup"),   # type: ignore
    path("login/", user_views.user_login, name= "user_login"),  # type: ignore
    path("logout", user_views.user_logout, name= "user_logout"),
]
 

    