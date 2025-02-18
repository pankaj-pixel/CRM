from django.shortcuts import render,redirect
from django.views import View
from . models import UserProfile
from django.contrib.auth import logout

#create user form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from teams.models import Team

class Signup(View):
    form = UserCreationForm()

    def get(self,request,):
        return render(request,"userprofile/signup.html",{'form':self.form})
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            team = Team.objects.create(name='The team name',created_by= request.user)
            team.member.add(request.user)
            team.save()



            print("User Created Successfully!!!!")
            return redirect('login')
        
        else:
            print("InvalidUser cannot save")
            return render(request, "userprofile/signup.html", {
                'form': self.form
            })

class CustomLogoutView(View):
    def get(self, request):
        logout(request)  # Log the user out
        return redirect('/') 

@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user).first()
    return render(request,"userprofile/myaccount.html",{
        'team':team
    })