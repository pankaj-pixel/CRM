from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('',include('userprofile.urls')),
    path('dashboard/leads/',include('leads.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('client/',include('client.urls')),
    path('dashboard/teams/',include('teams.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
