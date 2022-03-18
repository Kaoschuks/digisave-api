
from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(title='DigiSaver Main')

urlpatterns = [
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
    path('schema/', schema_view),
    path('api/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/account/', include('users.urls')),
    path('api/files/', include("files.urls"))
]

if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
