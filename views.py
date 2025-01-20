from django.shortcuts import render, redirect
from .models import Receipe 
from django.contrib.auth.models import User# Ensure the Receipe model is imported
from django.contrib import messages
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url="/lgoin_page/")
def recepie(request):
    if request.method == "POST":
        # Get the form data
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
        )
        return redirect('/shop')
    queryset = Receipe.objects.all() 
    context = {'receipes': queryset}
    return render(request, 'recipe_list.html', context)
def new_recepie(request):
    if request.method == "POST":
        data = request.POST
       
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        # Save the new recipe to the database
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
        )
    
    queryset = Receipe.objects.all() 
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipes': queryset}
    return render(request, 'recipe_add.html', context)

@login_required(login_url="/login_page/")
def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)

    if request.method== "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image= receipe_image
        queryset.save()
        return redirect('/shop')
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', {'receipe': context})
@login_required(login_url="/login_page/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)  
    queryset.delete()  
    return redirect('/shop')

def login_page(request):
   if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if  not User.objects.filter(username=username).exists():
            messages.error(request,'Mismatched username')  
            return render(request, 'login.html')
    
        user = authenticate(username=username ,password=password)
        
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login_page')
        else:
            login(request, user)
            return redirect('/shop')
            
            
     
            
   return render (request,'login.html')

def register_page(request):
   if request.method=="POST":
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'user already taken')
            return redirect('/register_page') 
        

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'account created successfuly')
    
   return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login_page')

 
