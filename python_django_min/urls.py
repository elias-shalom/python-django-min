from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    # path('admin/', admin.site.urls),
    # Include other app URLs here
    path('', home, name='home'),
]