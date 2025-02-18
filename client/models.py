from django.db import models
from django.db import models
from django.contrib.auth.models import User
from teams.models import Team




class Clients(models.Model):
    team = models.ForeignKey(Team,related_name='clients',on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    created_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='clients')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    class Meta:
        ordering=('Name',)
        verbose_name_plural ='clients'

    def __str__(self):
        return self.Name    


class comments(models.Model):
    team = models.ForeignKey(Team, related_name='client_comment', on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.created_by    
    
class ClientFiles(models.Model):
    team = models.ForeignKey(Team, related_name='client_files', on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, related_name='files', on_delete=models.CASCADE)
    files = models.FileField(upload_to='clientfiles')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_files')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username    

