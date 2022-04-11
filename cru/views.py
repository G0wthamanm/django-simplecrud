from django.shortcuts import render,redirect
from .models import crud
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserAddForm,UserLogin
from django.views.decorators.cache import cache_control

#dashboard
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        first=request.POST['first']
        last=request.POST['last']
        phone=request.POST['phone']
        address=request.POST['address']
        id=None
        obj=crud(id,first,last,phone,address)
        obj.save() 
    return render(request,'index.html')
#view table
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def read(request):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        obj=crud.objects.all()
    except crud.DoesNotExist:
        obj=None
    return render(request,'view.html',{'key':obj})
#register page
def register_view(request):
    if request.method=='POST':
        form=UserAddForm(data=request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            username=form.cleaned_data['username']
            messages.success(request,'New User Created Successfully')
            return redirect('login')
        else:
            messages.error(request,'invalid')
    form = UserAddForm()
    dataset=dict()
    dataset['form']=form
    return render(request,'register.html',dataset)
#logout page
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout_view(request):
    logout(request)
    return redirect('login')
#login
@cache_control(no_cache=True, must_revalidate=True)
def login_view(request):
    login_usr=request.user
    if request.method=='POST':
        form=UserLogin(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if login_usr.is_authenticated:
                    messages.success(request,'Logged In Successfully')
                    return redirect('create')
                else:
                    messages.error(request,'invalid')
                    return redirect('login')
        else:
            return HttpResponse('invalid')
    dataset=dict()
    form = UserLogin()
    dataset['form']=form
    return render(request,'login.html',dataset)
#form update
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def update(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        first_name = request.POST['first']
        last_name = request.POST['last']
        phone=request.POST['phone']
        address=request.POST['address']
        obj1 = crud.objects.get(id=id)
        obj1.first = first_name
        obj1.last = last_name
        obj1.phone=phone
        obj1.address=address
        obj1.save()
        return redirect('dashboard')
    else:
        try:
            obj = crud.objects.get(id=id)
        except crud.DoesNotExist:
            obj = None

        return render(request,'edit.html',{'key':obj})

# Delete 
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        obj = crud.objects.get(id=id)
    except crud.DoesNotExist:
        obj = None
    
    obj.delete()
    return redirect('dashboard')