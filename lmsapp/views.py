
from re import L
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm,QuizForm
from .models import  login,quizmodel
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/dashboard")
    else:
        form= LoginForm()
    context={'form':form}
    return render(request,'lmsapp/index.html',context)

#logic for sign in 
def login_check(request):
    logins=login.object.all()
    form = LoginForm(request.POST)
    if form.username and form.password in logins:
        return redirect("/dashboard")
    else:
        return HttpResponse("<p>Error404</p>")

def second (request,id):
    logins=login.objects.get(id=id)
    form = LoginForm(request.POST,instance=logins)
    if form.is_valid():
        form.save()
        return redirect("/dashboard")
    else:
        form=LoginForm()
    
    context={"logins":logins,"form":form}
    return render(request,'lmsapp/second.html',context)

def table(request):
    logins=login.objects.all()
    context={"logins":logins}
    return render(request,'lmsapp/directory.html',context)

def dashboard(request):
    return render(request,'lmsapp/dashboard.html')

def delete(request,id):
    logins=login.objects.get(id=id)
    logins.delete()
    return redirect("/directory")

def result_display(request):
     print(request.method)
     if request.method == 'POST':
        questions =quizmodel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions :
            total+=1
            print(request.POST.get('{{q.question}}'))
            print(q.answer)
            print(request.POST.get('{{q.answer}}'))
            print()
            if q.question ==  request.POST.get('{{q.question}}'):
                
                score+=1
                correct+=1
            else:
                wrong+=1
                 
        else:
             percent = score/(total*10) *100
             context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
        }
        return render(request,'lmsapp/result.html',context)

def quiz_display(request):
        questions=quizmodel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'lmsapp/quiz.html',context)

def calendar_display(request):
    return render(request ,'lmsapp/calendar.html')

def module(request):
    return render(request,'lmsapp/modules.html')


    