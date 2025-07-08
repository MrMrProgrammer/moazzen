from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .forms import Login
from .models import Users
import hashlib
from django.conf import settings
from django.contrib import messages
# Create your views here.

def login_user(request):
    context = {}
    if request.method == "POST":
            
            phone = request.POST.get("phone")
            password = request.POST.get("password")
            print(password)
            try: 
                user = Users.objects.get(phone_number=phone)
            except Users.DoesNotExist: 
                context["error_message"] = "چنین شماره همراهی ثبت نشده است "
                return render(request , "login.html" , context)
                # form.add_error("چنین شماره همراهی ثبت نشده است ")
            if  password == user.password :
                request.session["userid"] = user.id 
                return redirect("user_profile") 
                
                # form.add_error("password" , "رمز  عبور اشتباه است")
            else : 
                context["error_message"] = "رمز  عبور اشتباه است"
                return render(request , "login.html" , context)
   
    return render(request, "login.html" , context)



def user_profile(request):
    session_id = request.session.get("userid")
    if session_id  is None:  
        return redirect("login_user")
    
    user = Users.objects.get(id = session_id)
    context= {
        "user": user,  
        "media" : settings.MEDIA_URL
    }

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        if not " " in full_name: 
            context["error_message"] = "نام و نام خانوادگی خود را کامل وارد کنید"
        elif not phone.startswith("09") : 
            context["error_message"] = "تلفن همراه خود را به شکل صحیح وارد کنید "
        else : 
            first_name , last_name = full_name.split(maxsplit=1)
            user.first_name= first_name
            user.last_name = last_name
            user.phone_number = phone
            user.save()
            context["success_message"] = "با موفقیت ویرایش شد"


    return render(request , "user_profile.html" , context )


def logout(request):
    request.session.flush()
    return redirect("login_user")


def reset_password(request):
    session_id = request.session.get("userid")
    if session_id  is None:
        return redirect("login_user")
    
    user = Users.objects.get(id = session_id)
    context= {
        "user": user,  
        "media" : settings.MEDIA_URL
    }


    if request.method == "POST": 
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")
        if not new_pass == confirm_pass  : 
            context["error_message"] = "رمز عبور با تکرار آن یکسان نیست"  
        else : 
            user.password = new_pass 
            user.save()
            messages.success(request , "رمز عبور با موفقیت تغییر یافت")
            return redirect("user_profile")
    return render(request , "reset_pass.html" , context  )
    