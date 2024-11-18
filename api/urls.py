from django.urls import path , include
from rest_framework_simplejwt.views import TokenRefreshView
from userauths import views as userauth_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = []

router

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
    path('auth/jwtlogin/', userauth_views.MyTokenObtainPairView.as_view()),
    path('auth/jwtlogout/', userauth_views.LogoutView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]