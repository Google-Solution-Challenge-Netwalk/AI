from django.contrib import admin
from django.urls import path, include
from model import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/', include('model.urls')),
]
