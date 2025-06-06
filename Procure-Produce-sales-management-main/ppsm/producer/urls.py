
from django.urls import path
from . import views

urlpatterns=[

    path ("",views.producer,name="producer"),
    path("login/",views.login,name="login"),
    path("signup/",views.signUp,name="signup")
   
]