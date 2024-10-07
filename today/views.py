from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, TaskForm
# Create your views here.
from .decorators import custom_login_required
from .models import Task
from django.shortcuts import get_object_or_404


@custom_login_required
def home(request):
    return render(request, 'today/home.html')

def unauthorized_access(request):
    return render(request, 'today/unauthorized.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'today/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')  # Redirect to home after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid login details.')
    else:
        form = UserLoginForm()
    
    return render(request, 'today/login.html', {'form': form})
    
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def upload_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)  # Handle both text data and files
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to a task list view after submission
    else:
        form = TaskForm()
    return render(request, 'today/upload_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'today/task_list.html',{'tasks':tasks})

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)  # Get the task object by ID
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()  # Save the changes to the task
            return redirect('task_list')  # Redirect to the list of tasks (you can modify the redirect path as needed)
    else:
        form = TaskForm(instance=task)  # Pre-populate the form with existing task data
    return render(request, 'today/edit_task.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)  # Get the task object by ID
    if request.method == 'POST':
        task.delete()  # Delete the task
        return redirect('task_list')  # Redirect to the list of tasks
    return render(request, 'today/delete_task.html', {'task': task})