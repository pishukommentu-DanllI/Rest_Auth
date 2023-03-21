from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('App.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/session/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls.authtoken'))
]
