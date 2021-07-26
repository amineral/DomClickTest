from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    choices = [
        ('default', 'default'),
        ('registered', 'registered'),
        ('in_work', 'in_work'),
        ('done', 'done')
    ]
    title = models.CharField(max_length=30, blank=False, default='None')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=choices, default='default')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    text = models.TextField(blank=False, default=None)

    def __str__(self):
        return 'from ' + self.client.user.first_name + ' ' + self.client.user.last_name + ': ' + self.title

