from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    max_leads = models.IntegerField()
    max_clients = models.IntegerField()

    def __str__(self):
        return self.name

    
class Team(models.Model):
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,related_name='teams')
    Name = models.CharField(max_length=100)
    member = models.ManyToManyField(User,related_name='team_member')
    created_by = models.ForeignKey(User,related_name='created_team',on_delete=models.CASCADE)
    def __str__(self):
        return self.Name

    
