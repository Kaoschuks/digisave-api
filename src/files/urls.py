from django.urls import path, include 
from .views import FileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manage', FileView)
# urlpatterns = [
#   path('upload', FileView.as_view() ),
#   path('delete/<file>/<user_id>', delete_file)
# ]

urlpatterns =router.urls