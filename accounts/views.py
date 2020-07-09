from django.shortcuts import render

# Create your views here.
from accounts.forms import StudentRegistrationForm, StudentChangeForm


def Reg(request):
    f= StudentChangeForm
    context={
        'f':f
    }
    return render(request,'index.html',context)