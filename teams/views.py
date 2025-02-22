from django.shortcuts import render,get_list_or_404,redirect
from django.shortcuts import render ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Team
from .forms import Teamsform
from django.contrib import messages




@login_required
def edit_team(request,pk):
    team = get_object_or_404(Team,created_by=request.user,pk=pk)

    if request.method=='POST':
        form =Teamsform(request.POST,instance=team)
    
        if form.is_valid():
            form.save()
            messages.success(request, "Team Edited Successfully !!! ")
            return redirect('myaccount')
    else:
        form =Teamsform(instance=team)
    return render(request,'teams/edit_team.html',{
        'team':team,
        'form':form
    })