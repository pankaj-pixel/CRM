"""from .models import Team

def active_team(request):
    team = Team.objects.filter(created_by=request.user).first()
    print(team)
    return {'active_team':team}"""