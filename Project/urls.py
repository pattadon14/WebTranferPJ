from django.contrib import admin
from django.urls import path
from Webtranfer import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.Home ,),
    path('Home/',views.Home ,name='Home'),
    path('LoginStudent/',views.LoginStudent ,name='LoginStudent'),
    path('LoginAdvisor/',views.LoginAdvisor ,name='LoginAdvisor'),
    path('LoginAdmin/',views.LoginAdmin ,name='LoginAdmin'),
    path('Register/',views.Register ,name='Register'),
    
    #ADMIN
    path('collegepage/',views.Collegepage ,name='collegepage'),
    path('edit_collegepage/<college_id>',views.edit_college ,name='edit_college'),
    path('delete_college/<int:id>/',views.delete_college ,name='delete_college'),
    path('Faculty/',views.Facultys ,name='Faculty'),
    path('Collmajor/',views.CollMajor ,name='Collmajor'),
    path('Major/',views.Majors ,name='Major'),
    path('Group/',views.Group ,name='Group'),
    path('Course/',views.Course ,name='Course'),
    path('EditCourse/',views.EditCourse ,name='EditCourse'),
    path('ModelTranfer/',views.ModelTranfer ,name='ModelTranfer'),
    path('Advisor/',views.Advisors ,name='Advisor'),
    path('Admin/',views.Admin ,name='Admin'),
    path('Tranfer/',views.Tranfer ,name='Tranfer'),
    
    #ADVISOR
    path('AdvisorShowStudent/',views.AdvisorShowStudent ,name='AdvisorShowStudent'),
    path('AdvisorCheckTranfer/',views.AdvisorCheckTranfer ,name='AdvisorCheckTranfer'),
    
    
    #ADMIN + ADVISOR
    path('CheckCourse/',views.CheckCourse ,name='CheckCourse'),
    path('CheckSubject/',views.CheckSubject ,name='CheckSubject'),
    path('CheckSubjectCategory/',views.CheckSubjectCategory ,name='CheckSubjectCategory'),
    
    #STUDENT
    path('Stu_Tranfer/',views.Stu_Tranfer ,name='Stu_Tranfer'),
    path('Stu_GPA/',views.Stu_GPA ,name='Stu_GPA'),
    path('Stu_Edit/',views.Stu_Edit ,name='Stu_Edit'),
    path('Stu_checkcouse/',views.Stu_checkcouse ,name='Stu_checkcouse'),
    
    
    
]
