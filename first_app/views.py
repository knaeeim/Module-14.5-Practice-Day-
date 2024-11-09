from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def home(request):
    form = FormEx()
    model = User()
    if request.method == "POST":
        form = FormEx(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, "home.html", {"form": form , "model" : model })

def model(request):
    if request.method == "POST":
        model = Prac(request.POST)
        if model.is_valid():
            model.save()
    else:
        model = Prac()
    return render(request, 'model.html', {'model' : model})

