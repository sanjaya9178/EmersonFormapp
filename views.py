from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def item_show(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
    else:
        fm=UserForm()

    return render(request,'itemdisplay.html',{'form':fm})
