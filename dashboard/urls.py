from django.urls import path
from .views import dashboardView
from leads.views import LeadDetailView


urlpatterns = [
    path('',dashboardView,name='dashboard'),
    path('<int:pk>/',LeadDetailView.as_view(),name='lead_detail')
]
