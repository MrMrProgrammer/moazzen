from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from accounts.models import CustomUser
from actions.models import Azan
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import check_password 
from django.contrib.auth import authenticate , login , update_session_auth_hash , logout
import datetime
# Create your views here.

def login_user(request):
    context = {}
    if request.method == "POST":
            phone = request.POST.get("phone")
            password = request.POST.get("password")
            try: 
                user = CustomUser.objects.get(phone_number=phone)
            except CustomUser.DoesNotExist: 
                context["error_message"] = "چنین شماره همراهی ثبت نشده است "
                return render(request , "login.html" , context)
                # form.add_error("چنین شماره همراهی ثبت نشده است ")
            if  check_password(password  , user.password)  :
                user_obj = authenticate(request , username = phone , password = password )
                if user_obj is not None:
                    login(request , user_obj)
                    return redirect("user_profile") 
                else: 
                    context["error_message"] = "رمز  عبور اشتباه است"
                    return render(request , "login.html" , context)
                
                # form.add_error("password" , "رمز  عبور اشتباه است")
            else : 
                context["error_message"] = "رمز  عبور اشتباه است"
                return render(request , "login.html" , context)
   
    return render(request, "login.html" , context)


@login_required
def user_profile(request):
    context ={}
    user = request.user
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        name_parts = full_name.split(maxsplit=1)
        if not " " in full_name or len(name_parts) < 2 or not name_parts[1].strip(): 
            context["error_message"] = "نام و نام خانوادگی خود را کامل وارد کنید"
        elif not phone.startswith("09") : 
            context["error_message"] = "تلفن همراه خود را به شکل صحیح وارد کنید "
        else : 
            first_name = name_parts[0]
            last_name = name_parts[1] 
            user.first_name= first_name
            user.last_name = last_name
            user.phone_number = phone
            user.save()
            context["success_message"] = "با موفقیت ویرایش شد"
    today = datetime.date.today()
    today_tasks = Azan.objects.filter(user = user , date = today)

    context["today_tasks"] = today_tasks
    return render(request , "user_profile.html" , context )

@login_required
def reset_password(request):
    context = {}
    user = request.user
    if request.method == "POST": 
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")
        if not new_pass == confirm_pass  : 
            context["error_message"] = "رمز عبور با تکرار آن یکسان نیست"  
        else : 
            user.set_password(new_pass)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request , "رمز عبور با موفقیت تغییر یافت")
            return redirect("user_profile")
    return render(request , "reset_pass.html" , context  )


@login_required
def logout_view(request):
    logout(request)
    return redirect("login_user")



@login_required
def show_all_tasks(request):
    all_tasks = Azan.objects.filter(user = request.user, is_verified=True)
    return render(request , "all_tasks.html" , context={"all_tasks":all_tasks})
