from django.contrib import admin
from .models import Agent, Client, Task

admin.site.register(Agent)
admin.site.register(Client)
admin.site.register(Task)