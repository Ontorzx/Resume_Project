from django.shortcuts import render

# Create your views here.
def Services(request):
    context={
        'services':'active'
    }
    return render(request,'services/service.html',context)