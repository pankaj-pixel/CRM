
from .forms import Leadsform
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Leads
from client.models import Clients
from teams.models import Team
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView,UpdateView
from .models import Leads,comments
from django.urls import reverse_lazy
from django.views import View
from .forms import AddCommentsform,LeadFilesform

class LeadListview(LoginRequiredMixin,ListView):
    model = Leads()
    def get_queryset(self):
        queryset =Leads.objects.filter(created_by = self.request.user,converted_to_client = False)
        return queryset
    


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Leads
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentsform()
        context['fileform'] = LeadFilesform()

        lead = context['lead']
        context['comments'] = comments.objects.filter(lead=lead)  # Filter comments based on the current lead

        return context


    def get_queryset(self):
        # Ensure that only leads created by the current user are returned
        return Leads.objects.filter(created_by=self.request.user)


@login_required
def add_lead(request):
    team = Team.objects.filter(created_by=request.user).first()
    form = Leadsform()  
    if request.method == 'POST':
        form = Leadsform(request.POST)  
        try:
            if form.is_valid():
                team = Team.objects.filter(created_by=request.user).first()
                lead = form.save(commit=False)  # Don't save yet, because we need to set created_by
                lead.created_by = request.user  # Set the current user as the creator
                lead.team = team
                messages.success(request, "Lead Created Successfully !!! ")
                lead.save()  # Now save the lead to the database 
                return redirect('dashboard')
            else: 
                pass
                #messages.ERROR(request, 'Invalid form submission.')
                #messages.ERROR(request, form.errors)
        except Exception as e:
            form.add_error(None, f"An error occurred: {str(e)}")
    return render(request, 'leads/add_lead.html', {
        'form': form,
        'team':team
    })


class DelteteLeadView(LoginRequiredMixin,DeleteView):
    model = Leads
    template_name = 'leads\leads_confirm_delete.html'
    success_url =reverse_lazy('leads_list')


class EditLeadView(LoginRequiredMixin,UpdateView):
    model =Leads
    fields =('Name','email','description','priority','status',)
    success_url = reverse_lazy('leads_list')

    def get_queryset(self):
        queryset = super(EditLeadView,self).get_queryset()
        return queryset.filter(created_by = self.request.user,pk=self.kwargs.get('pk'))
    

class AddFileView(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        form = LeadFilesform(request.POST ,request.FILES)
        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user).first()
            file =form.save(commit=False)
            file.team=team
            file.created_by =request.user
            file.lead_id =pk
            file.save()
        return redirect('lead_detail',pk=pk)



class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        
        pk = self.kwargs.get('pk')

        form = AddCommentsform(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user).first()
            comment = form.save(commit=False)
            comment.team=team
            comment.created_by =request.user
            comment.lead_id =pk 
            print(comment.lead_id)
            comment.save()
        return redirect('lead_detail',pk=pk)


class ConverToClientView(View):
      def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lead = get_object_or_404(Leads,created_by =request.user,pk=pk)
        team =Team.objects.filter(created_by=request.user).first()
        client = Clients.objects.create(Name =lead.Name,
                                    email =lead.email,
                                    description=lead.description,
                                    created_by=request.user,team=team)
        lead.converted_to_client = True
        lead.save()
        messages.success(request, "Client Created Succeessfully !!!! ")
        return redirect('leads_list')









