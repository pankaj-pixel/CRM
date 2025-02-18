from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from leads.models import Leads
from client.models import Clients
from teams.models import Team


@login_required
def dashboardView(request):
    team = Team.objects.filter(created_by =request.user).first()
    lead = Leads.objects.filter(team=team,converted_to_client=False).order_by('-created_at')[:5]
    client =Clients.objects.filter(team=team).order_by('-created_at')[:5]
    return render(request,'dashboard/dashboard.html',{
        'leads':lead,
        'clients':client
    })


