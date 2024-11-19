from django.urls import path , include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from userauths import views as userauth_views
from chatbot.views import ChatApiView
router = DefaultRouter()
urlpatterns = []

router.register('chat' , ChatApiView , basename='chat')

urlpatterns += [
    path('auth/login/', userauth_views.MyTokenObtainPairView.as_view()),
    path('auth/jwtlogout/', userauth_views.LogoutView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]