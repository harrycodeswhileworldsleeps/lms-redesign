from django.urls import path 
from .views import dashboard, delete,  login_view, module,second,table,quiz_display,result_display,calendar_display
urlpatterns=[
    path('',login_view,name="home"),
    path('second',login_view,name="second"),#for testing the addition of data 
    path('third/<int:id>',second,name="third"),
    path('directory',table ,name="directory"),
    path('dashboard',dashboard, name="dashboard"),
    path('delete/<int:id>',delete,name="delete"),
    path('quiz',quiz_display,name="quiz"),
    path('result',result_display,name="result"),
    path('calendar',calendar_display,name="calendar"),
    path('modules',module,name="modules")

]
