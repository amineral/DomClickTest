from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Client, Agent, Task
from .forms import AuthenticationForm, CreateTaskForm
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return redirect("/main/")

    form_auth = AuthenticationForm()
    context = {
        "form_auth" : form_auth,
    }

    return render(request, "crm/index.html", context=context)

def proceed_auth(request):
    form = AuthenticationForm(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/main/")

    return redirect("index")

def proceed_logout(request):
    logout(request)
    return redirect("index")

def main_page(request):
    if not request.user.is_authenticated:
        return redirect("index")
    form = CreateTaskForm()
    agent = Agent.objects.get(user=6)
    new_tasks = Task.objects.filter(agent=agent)
    context = {
        "user" : request.user,
        "role" : None,
        "form" : form,
        "new_tasks" : new_tasks,
    }
    if request.user.groups.filter(name='Agent').exists():
        context["role"] = "Agent"
    elif request.user.groups.filter(name='Client').exists():
        context["role"] = "Client"
    else:
        context["role"] = "Admin"
    return render(request, 'crm/main.html', context=context)

def clients(request):
    if request.user.is_staff:
        clients = Client.objects.all()
    else:
        clients = Client.objects.filter(agent=Agent.objects.get(user=request.user))
    context = {
        'clients' : clients,
    }
    return render(request, 'crm/clients.html', context=context)

def agents(request):
    agents = Agent.objects.all()
    context = {
        'agents' : agents
    }

    return render(request, 'crm/agents.html', context=context)

def tasks(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    elif request.user.groups.filter(name='Client').exists():
        tasks = Task.objects.filter(client=Client.objects.get(user=request.user))
    else:
        tasks = Task.objects.filter(agent=Agent.objects.get(user=request.user))
    context = {
        'tasks' : tasks
    }

    return render(request, 'crm/tasks.html', context=context)

def details(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task' : task,
        'role' : None
    }
    if request.user.groups.filter(name='Client').exists():
        context["role"] = "Client"
    return render(request, 'crm/details.html', context=context)

def task_in_work(request, id):
    task = Task.objects.get(id=id)
    print(task)
    if task.status == 'registered':
        task.status = 'in_work'
    elif task.status == 'in_work':
        task.status = 'done'
    task.save()
    return redirect("tasks")

def create_task(request):
    form = CreateTaskForm(request)
    title = request.POST.get('title')
    text = request.POST.get('text')
    client = Client.objects.get(user=request.user)
    agent = Agent.objects.get(user=6)
    new_task = Task(title=title, client=client, status='registered', agent=agent, text=text)
    new_task.save()
    return redirect("main")
        

