from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page_view(request):
    return render(request, 'MyApps1/home.html')


@login_required
def java_exams_view(request):
    return render(request, 'MyApps1/javaexams.html');


@login_required
def python_exams_view(request):
    return render(request, 'MyApps1/pythonexams.html');


@login_required
def aptitude_exams_view(request):
    return render(request, 'MyApps1/aptitudeexams.html');


def logout_view(request):
    return render(request, 'MyApps1/logout.html')
from MyApps1.forms import SignUpForm
from django.http import HttpResponseRedirect
def signup_view(request):
    formobj=SignUpForm()
    if request.method=="POST":
        formobj=SignUpForm(request.POST)
        user=formobj.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'MyApps1/signup.html', {'formobj':formobj})
