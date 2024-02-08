from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
# Create your views here.
def hsignup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password1']
        password_confirm=request.POST['password2']
        if password!=password_confirm:
            messages.warning(request,'incorect password')
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.warning(request,'already a user')
                return render(request,'signup.html')
        except Exception as identifire:
            pass
        user=User.objects.create_user(email,email,password)
        user.save()
        messages.info(request,'user created')
        return redirect('/auth/login')
    return render(request,'signup.html')



def hlogin(request):
    if request.method=="POST":
        user_email=request.POST['email']
        user_password=request.POST['password1']
        my_user = authenticate(username=user_email,password=user_password)
        if my_user is not None:
            login(request,my_user)
            messages.success(request,'logged in')
            return redirect('profile')
        else:
            messages.error(request,'failed to log in')
            return redirect('/auth/login')
    
    return render(request,'login.html')

def hlogout(request):
    logout(request)
    messages.success(request,'logged out')
    return redirect('/auth/login')
