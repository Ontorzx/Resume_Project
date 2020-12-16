from django.shortcuts import render

# Create your views here.
def Skill(request):
    context={
        'skill':'active'
    }
    return render(request,'education/skill.html',context)