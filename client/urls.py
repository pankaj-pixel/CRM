from django.urls import path
from .views import clients_list,client_detail,client_delete,add_client,client_edit,clients_add_file,client_description_report
urlpatterns = [
    path('',clients_list,name='clients_list'),
    path('<int:pk>/',client_detail,name='client_detail'),
    path('export/',client_description_report,name='client_report'),
    path('<int:pk>/delete',client_delete,name='client_delete'),
    path('add-client/',add_client,name='add_client'),
    path('<int:pk>/edit',client_edit,name='client_edit'),
    path('<int:pk>/add-file/',clients_add_file,name='add-file'),
    path('<int:pk>/add-comment/',client_detail ,name='add-comment'),


]