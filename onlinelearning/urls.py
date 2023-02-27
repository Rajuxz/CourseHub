#-----[ Static File handling and URL Configuration goes here ]-----#
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('classhub.urls')),
    path('registration/',include('registration.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
