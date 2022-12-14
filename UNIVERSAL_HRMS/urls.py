from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/hrms_user/', include('hrms_users.urls')),
    path('api/organizations/', include('organizations.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
