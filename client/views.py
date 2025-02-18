import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from . models import Clients,comments
from .forms import ClientForm,AddCommentsform,ClientFilesform
from teams.models import Team
from django.views import View
# Create your views here.

@login_required
def clients_list(request):
    query = Clients.objects.filter(created_by=request.user)
    return render(request,'client/client_list.html',{'clients':query})


@login_required
def clients_add_file(request,pk):
    client = get_object_or_404(Clients, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user).first()

    if request.method == 'POST':
        form = ClientFilesform(request.POST ,request.FILES)
        if form.is_valid():
            file =form.save(commit=False)
            file.team=team
            file.created_by =request.user
            file.client_id =pk
            file.save()

            return redirect('client_detail', pk=pk)
    return redirect('client_detail', pk=pk)    




@login_required
def client_detail(request, pk):
    query = get_object_or_404(Clients, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user).first()
    if request.method == 'POST':
        form = AddCommentsform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.client = query
            comment.save()
            return redirect('client_detail', pk=pk)
    else:
        form = AddCommentsform()

    return render(request, 'client/client_detail.html', {'client': query,'form': form,'fileform':ClientFilesform(),})



@login_required
def client_delete(request,pk):
    query = get_object_or_404(Clients,created_by=request.user,pk=pk)
    messages.success(request, "Client Deleted  Successfully !!!")
    query.delete()
    return redirect('clients_list')

@login_required
def add_client(request):
    team = Team.objects.filter(created_by=request.user).first()
    if request.method =='POST':
        form = ClientForm(request.POST) 
        print(form) 
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user).first()
            client= form.save(commit=False)
            client.created_by = request.user
            client.team = team
            
            client.save()
            messages.success(request, "Client Created Successfully !!!")
            return redirect('clients_list')
    else:
        form = ClientForm()

    return render(request, 'client/add_client.html', {
            'form': form,
            'team':team
        })    


@login_required
def client_edit(request,pk):
    query = get_object_or_404(Clients,created_by=request.user,pk=pk)
    if request.method =='POST':
        form = ClientForm(request.POST,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, "Client Edited Successfully !!!")
            return redirect('clients_list')
    else:
        form =ClientForm(instance=query)
    return render(request, 'client/edit_client.html', {
        'form': form
    })    
        



# Export CSV file as Description of Clients
@login_required
def client_description_report(request):
    clients = Clients.objects.filter(created_by=request.user)

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="client.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["client_name", "description", "created_by", "created_at"])
    for client in clients:
        writer.writerow([client.Name, client.description,client.created_by,client.created_at])

    return response






