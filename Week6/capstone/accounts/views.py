from django.contrib import messages, auth
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from pages.models import Users

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username = username, password = password)
        
        if User.objects.filter(username = request.POST['username']).exists():
            
            if User.objects.filter(username = request.POST['username'], password= request.POST['password']).exists():
                user = User.objects.get(username = request.POST['username'], password= request.POST['password'])
                auth.login(request, user)    
                return redirect ('dashboard')
                     
            else:
                messages.error(request, 'Invalid username/password')
                return redirect('login')
        else: 
            messages.error(request, 'User not found')
            return redirect('register')
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
                user = Users.objects.create(first_name=first_name,last_name=last_name,username=username,password=password,password2=password2,question1=question1,question2=question2,answer1=answer1,answer2=answer2)
                user = User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password)
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

def forgot_password(request):
    if request.method == 'POST':
    #Get form values
        username = request.POST['username']
                
        qs = Users.objects.all()
        for data in qs:
            # username = data.username    
            user_found = Users.objects.get(username=username)
                        
            if user_found.question1 == 'Q1':
                new_question1 = "What is your favorite color?"
            if user_found.question1 == 'Q2':
                new_question1 = "Your childhood nickname?"
            if user_found.question1 == 'Q3':
                new_question1 = "Your High School Mascot?"
            if user_found.question2 == 'Q1':
                new_question2 = "What is your favorite color?"
            if user_found.question2 == 'Q2':
                new_question2 = "Your childhood nickname?"
            if user_found.question2 == 'Q3':
                new_question2 = "Your High School Mascot?"    
            return render(request, 'accounts/security_questions.html', {'found_user': user_found, 'username':username,'question1':new_question1,'question2':new_question2})
    else:       
        return render(request, 'accounts/forgot_password.html')
    
def security_questions(request):
    return render(request, 'accounts/security_questions.html')

def ck_security_questions(request):
    if request.method == 'POST':
    #Get form values
        username = request.POST['username']
        question1 = request.POST['question1']
        question2 = request.POST['question2']
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        
        if question1 == 'What is your favorite color?':
            new_question1 = "Q1"
        if question1 == 'Your childhood nickname?':
            new_question1 = "Q2"
        if question1 == 'Your High School Mascot?':
            new_question1 = "Q3"
        if question2 == 'What is your favorite color?':
            new_question2 = "Q1"
        if question2 == 'Your childhood nickname?':
            new_question2 = "Q2"
        if question2 == 'Your High School Mascot?':
            new_question2 = "Q3" 

        if Users.objects.filter(username=username, question1=new_question1, question2=new_question2, answer1=answer1,answer2=answer2).exists():
            return render(request, 'accounts/reset_password.html', {'username':username})
        else:       
            messages.error(request, 'Invalid answers. Try again. ')
            return render(request, 'accounts/security_questions.html', {'username':username,'question1':question1,'question2':question2})
    else:       
        return render(request, 'accounts/forgot_password.html')

def reset_password(request):
    if request.method == 'POST':
    #Get form values
        
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
                
        #Check to see if passwords match
        if password == password2:
            user = Users.objects.filter(username=username).update(password=password,password2=password2)
            user = User.objects.filter(username=username).update(password=password)
            messages.success(request, 'You have successfully updated password.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/reset_password.html', {'username':username})
    else:
        return render(request, 'accounts/reset_password.html')
    