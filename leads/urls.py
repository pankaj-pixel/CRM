from django.urls import path
from .views import add_lead,LeadListview,LeadDetailView,DelteteLeadView,EditLeadView,ConverToClientView,AddCommentView,AddFileView




urlpatterns = [
    path('add-lead/',add_lead,name='add_lead'),
    path('',LeadListview.as_view(),name='leads_list'),
    path('<int:pk>/',LeadDetailView.as_view(),name='lead_detail'),
    path('<int:pk>/delete',DelteteLeadView.as_view(),name='Delete_lead'),
    path('<int:pk>/convert',ConverToClientView.as_view(),name='convert_to_client'),
    path('<int:pk>/add-comment/',AddCommentView.as_view(),name='add-comment'),
    path('<int:pk>/add-file/',AddFileView.as_view(),name='add-file'),
    path('<int:pk>/edit',EditLeadView.as_view(),name='edit_lead')
]
