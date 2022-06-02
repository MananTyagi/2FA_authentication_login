from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login 
from codes.forms import Codeform
from users.models import CustomUser
from .utils import send_sms


@login_required
def home_view(request):
    return render(request, 'main.html', {})

def register_view(request):
    return render(request, 'register.html', {})

def auth_view(request):
    form = AuthenticationForm()
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk']=user.pk
            return redirect('verify_view')
        else:
            return redirect('register_view')
    return render(request, 'auth.html', {'form': form})

def verify_view(request):
    form= Codeform(request.POST or None)
    pk=request.session.get('pk')
    if pk:
        user=CustomUser.objects.get(pk=pk)
        code=user.code
        code_user=f" Hi!{user.username} :{user.code} "
        if  not request.POST:
            print(code_user)
            send_sms(code_user, user.phone_number)
        if form.is_valid():
            num=form.cleaned_data.get('number')

            
            if str(code)==num:
                code.save()
                login(request, user)
                return redirect('home_view')
            else:
                return redirect('login_view')
    return render(request,'verify.html',{'form':form})

        
                


    


