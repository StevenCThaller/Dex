from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def home(request):
    
    return render(request, 'log_reg/index.html')

def register(request):

    return render(request, 'log_reg/reg.html')

def add_user(request):
    if request.method=='POST':
        errors = Users.objects.reg_validator(request.POST)

        if len(errors) > 0:
            for tag, value in errors.items():
                messages.error(request, value, extra_tags=tag)
            return redirect('/register')
        else:
            u_name = request.POST['u_name']
            email = request.POST['email']
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

            user = Users.objects.create(u_name=u_name, email=email, password=password.decode())

            request.session['user_id'] = user.id

            return redirect('/')
    return redirect('/')

def login(request):
    if request.method=='POST':
        errors = Users.objects.log_validator(request.POST)

        if len(errors) > 0:
            for tag, value in errors.items():
                messages.error(request, value, extra_tags=tag)
            return redirect('/register')
        else:
            
            return redirect('/pokedex/generation-vii')