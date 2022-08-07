from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# pages
from mainapp.forms import MyUserCreationForm
from mainapp.models import MyUser


def index_page(request):
    return render(request, 'mainapp/index.html')


def register_page(request):
    return render(request, 'mainapp/register.html')


# methods
def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect("main:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = MyUserCreationForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})
