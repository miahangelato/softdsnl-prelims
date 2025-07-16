from django.urls import path
from ml_api.views import api

urlpatterns = [
    path("", api.urls),
]
