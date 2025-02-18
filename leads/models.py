from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

class Leads(models.Model):
    LOW ='low'
    MEDIUM ='medium'
    HIGH ='high'

    PRIORITY_CHOICE =(
        (LOW,'low'),
        (MEDIUM,'Medium'),
        (HIGH,'High')
        )
    
    NEW ='new'
    CONTACTED ='contacted'
    WON ='won'
    LOST ='lost'

    LEAD_STATUS =(
        (NEW ,'new'),
        (CONTACTED ,'contacted'),
        (WON ,'won'),
        (LOST ,'lost')
    )

    team = models.ForeignKey(Team,related_name='lead',on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    priority =models.CharField(max_length=10,choices=PRIORITY_CHOICE,default=MEDIUM)
    status = models.CharField(max_length=50,choices=LEAD_STATUS,default=NEW)
    converted_to_client = models.BooleanField(default=False)
    created_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='leads')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    class Meta:
        ordering=('Name',)
        verbose_name_plural ='Leads'

    def __str__(self):
        return self.Name    
    

class LeadFiles(models.Model):
    team = models.ForeignKey(Team, related_name='lead_files', on_delete=models.CASCADE)
    lead = models.ForeignKey(Leads, related_name='files', on_delete=models.CASCADE)
    files = models.FileField(upload_to='leadfiles')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lead_files')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username    





class comments(models.Model):
    team = models.ForeignKey(Team, related_name='lead_comment', on_delete=models.CASCADE)
    lead = models.ForeignKey(Leads, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lead_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.created_by.username    
    