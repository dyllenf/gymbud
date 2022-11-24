
from django.contrib import admin
from django.urls import path, include


urlpatterns = [ #list of different url paths (home, about, contact,etc)
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
