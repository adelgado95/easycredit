from django.conf.urls import include
from django.urls import path
from apps.api import views

from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [ 
	#JWT Auth Rest Framework
	path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair2'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]