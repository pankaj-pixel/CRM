from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,"core/index.html")
    
def about(request):
    return render(request,"core/about.html")    

