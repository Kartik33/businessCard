from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .auth import validate_user
from django.views.decorators.http import require_http_methods


def home(request):
    return HttpResponse('<p>home view</p>')

@login_required()
@require_http_methods(['GET','DELETE','POST'])
def users(request,user_id):
    validate_user(request,user_id)
    user = request.user
    pathMapping = {'GET':detailed_user,
                   'DELETE':delete_user,
                   'POST':update_user}
    return pathMapping[request.method](request,user_id)

#do not call this fucntion directly come from users()
def detailed_user(request,user_id):
    user = Profile.objects.get(user__username=request.user.username)
    if user:
        return JsonResponse({"Status":"PASS",
                    "Status code":200,
                    "user_id":user.longFormat()}) 
    else:
        return error('404',"The user was not found")

#do not call this fucntion directly come from users()
def delete_user(request,user_id):
    user = Profile.objects.get(user__id=user_id)
    logout(request)
    try:
        user.delete()
    except:
        return error(500,"Server internal error")
    return JsonResponse({"Status":"Pass",
        "Status_code":204,
        "message":"User delete",
        "username":request.user.username})



#do not calls this fucntion directly come from users()
def update_user(request,user_id):
    profile = Profile.objects.get(user__id=user_id)
    image = request.POST.get('image',None)
    name = request.POST.get('name',None)
    #age = request.PATCH.get('age',None)
    #birthday = request.PATCH.get('birthday',None)
    #employer = request.PATCH.get('employer',None)
    #location = request.PATCH.get('location'None)
    #phone = request.PATCH.get('phone',None)
    #jobtitle = request.PATCH.get('jobtitle',None)

    if image and name:# and age and birthday and employer and location\
            #and phone and jobtitle:
        profile.user.name = name
        profile.image = image
        #uuser.age = requ
        #uuser.birthday =
        #uuser.employer =
        #uuser.location =
        #uuser.phone = re
        #uuser.jobtitle =
        profile.user.save()
        return redirect(f"/users/{user_id}/") 

    return error(400, "Failed to update the user") 


@require_http_methods(['POST'])
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    return JsonResponse({"kartik":"kartik"})
    if user:
        login(request,user)
        return redirect(f"/users/{user.id}/") 
    else:
        form = UserCreationForm()

    return HttpResponse(form) 

@require_http_methods(['POST'])
def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.image=form.cleaned_data.get('image')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username,password=raw_password)
        login(request,user)
        return redirect(f"/users/{user.id}/") 
    else:
        form = UserCreationForm()

    return HttpResponse(form) 

@require_http_methods(['DELETE'])
@login_required()
def logout_user(request):
    user_name = request.user.username
    logout(request)
    return JsonResponse({"Status_code":200,
        "Status":"PASS",
        "username":user_name,
        "message":"Logout was successful"})
    
def getToken(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken":csrf_token,
        "sessionid":request.session.session_key})

def error(code,msg):
    return JsonResponse({"Status":"Fail",
            "Status_code":code,
            "message":msg})
