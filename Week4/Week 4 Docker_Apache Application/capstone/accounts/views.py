from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from pages.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        # username = request.get('username')
        # password = request.get('password')

        if User.objects.filter(username = request.POST['username'], password= request.POST['password']).exists():
            user = User.objects.get(username = request.POST['username'], password= request.POST['password'])
            return render(request, 'pages/home.html',{'user': user})
        else:
            messages.error(request, 'Invalid username/password')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
    #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        question1 = request.POST['question1']
        question2 = request.POST['question2']
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        
        #Check to see if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'The username is taken.')
                return redirect('register')
            else:
                user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,password2=password2,question1=question1,question2=question2,answer1=answer1,answer2=answer2)
                # auth.login(request, user)
                user.save()
                messages.success(request, 'You have successfully registered.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
     if request.method == 'POST':
        auth.logout(request)
        return redirect('/')