from django.shortcuts import render, redirect
from .models import User, Role
from .forms import UserForm, RoleForm

def main(request):
    return render(request, 'base.html', {'page': 'main'})

#страница со списком пользователей
def users(request):
    #получим всех пользователей из базы
    users = User.objects.all()
    return render(request, 'users.html', {'users': users, 'page': 'users'})

# Create your views here.
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = UserForm()
    return render(request, "add_user.html", {'form': form, 'page': 'users'})

    
def add_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = RoleForm()
    return render(request, "add_role.html", {'form': form, 'page': 'add_role'})