from django.shortcuts import render,redirect,HttpResponse
from recipes.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def get_data(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        type=request.POST.get("type")
        recipe.objects.create(name=name,description=description,type=type)
        messages.success(request,"recipe has been added")
        return redirect('/add-recipe/')
    query_set=recipe.objects.all()
    return render(request,'recipe.html',context={"data":query_set})

def delete_recipe(request,id):
    query_set=recipe.objects.get(id=id)
    query_set.delete()
    messages.success(request,"recipe has been Deleted")
    return redirect('/add-recipe/')

def update_recipe(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        type=request.POST.get("type")
        r=recipe.objects.get(id=id)
        r.name=name
        r.description=description
        r.type=type
        r.save()
        messages.success(request,"recipe has been Updated")
        return redirect('/add-recipe/')
    query_set=recipe.objects.get(id=id)
    return render(request,'update_recipe.html',context={"data":query_set})
    
def search_recipe(request):
    if request.method=="POST":
        searched=request.POST.get("searched")
        r=recipe.objects.filter(name__icontains=searched)
        if len(r)==0:
            messages.error(request, "No search results found")
            return redirect("/add-recipe/")
        else:
            context={"searched":r}
            return render(request,"recipe.html",context)
    return render(request,"recipe.html")

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not exists")
            return redirect("/login/")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "wrong password")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect("/add-recipe/")
    return render(request,"login.html")

def signup_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "This username already exists, please choose another username")
            redirect("/signup/")
        else:
            user=User.objects.create(first_name=first_name,username=username)
            user.set_password(password)
            user.save()
            messages.success(request,"yayyy! You have successfully registered")
            redirect("/signup/")
        
    return render(request,"signup.html")


def logout_page(request):
    logout(request)
    return redirect("/login/")