from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from AuthReg.models import User
from WebDes.models import zayavka, main_tovar
from AuthReg.forms import UserLoginForm, RegistrationForm, User_ProfileForm, forma_otpr, Add_Tovar
from django.contrib import auth
from django.urls import reverse
from WebDes.models import *
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password, username=username)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('AuthReg:user_profile'))

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'auto.html', context)
def registration(request):
    if request.method=="POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AuthReg:login'))
    else:
        form=RegistrationForm()
    context={'form': form}

    return render(request, 'reg.html', context)
def user_profile(request):
    form = User_ProfileForm(instance=request.user)
    context = {'title': 'Профиль', 'form':form}
    return render(request, "user_cabinet.html", context)
def auth_check(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return HttpResponseRedirect(reverse('AuthReg:ADMIN_panel'))
        else:
            return HttpResponseRedirect(reverse('AuthReg:user_profile'))
    else:
        return HttpResponseRedirect(reverse('AuthReg:login'))

def Zayavka(request):
    if request.method=="POST":
        form = forma_otpr(data=request.POST)
        if form.is_valid():
            zayavkka = form.save()
            zayavkka.User_ID = request.user
            zayavkka.save()

            return HttpResponseRedirect(reverse('AuthReg:auth_check'))
    else:
        form=forma_otpr()
    context={'form': form}

    return render(request, 'forma.html', context)
def admins_panel(request):
    tovari = main_tovar.objects.all()
    zayavki = zayavka.objects.all()
    return render(request, "admin.html", {"tovari": tovari, "zayavki": zayavki})
def deleteTovar(request, id):
    record = get_object_or_404(main_tovar, pk=id)
    if request.method == "POST":
        record.delete()
        return HttpResponseRedirect(reverse('AuthReg:ADMIN_panel'))
    else:
        pass
def Add_Tovars(request):
    if request.method=="POST":
        form = Add_Tovar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('AuthReg:add_tovars'))
    else:
        form=Add_Tovar()
    context={'form': form}

    return render(request, 'Add_Tovar.html', context)
def deleteZayavka(request, id):
    record = get_object_or_404(zayavka, pk=id)
    if request.method == "POST":
        record.delete()
        return HttpResponseRedirect(reverse('AuthReg:ADMIN_panel'))
    else:
        pass
def AcceptZayavka(request, id):
    record = get_object_or_404(zayavka, pk=id)
    if request.method == "POST":
        record.Status = True
        record.save()
        return HttpResponseRedirect(reverse('AuthReg:ADMIN_panel'))
    else:
        pass