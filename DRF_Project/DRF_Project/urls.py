

from django.contrib import admin
from django.urls import path,include

import APP





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APP.urls')),
]
