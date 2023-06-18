from django.contrib import admin
from django.urls import path,include
from .views import login,register,recieved,NoteViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note') #including notes viewset in router urls 

urlpatterns = [
    path("register", register.as_view(), name = "register"),#Registers the user
    path("login", login.as_view(), name = "login"),#logins the user
    path("inbox",recieved, name= "recieved"),#shows the json data of recieved posts
    path("api-auth/",include('rest_framework.urls'))
]
urlpatterns+=[
    path('api/', include(router.urls)), #include router urls in url patterns
]