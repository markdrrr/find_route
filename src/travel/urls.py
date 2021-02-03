from django.contrib import admin
from django.urls import path, include

from travel.view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('', home, name='home'),
]