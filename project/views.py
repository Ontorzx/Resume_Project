from django.shortcuts import render

# Create your views here.
def Projects(request):
    context={
        'projects':'active'
    }
    return render(request,'project/projects.html',context)

def Projects_details(request):

    return render(request,'project/project_details.html')