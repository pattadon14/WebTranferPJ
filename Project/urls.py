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
    path('Collegepage/',views.Collegepage,name='Collegepage'),
    path('edit_collegepage/<college_id>',views.edit_college ,name='edit_college'),
    path('delete_collegepage/<college_id>',views.delete_college ,name='delete_college'),
    path('Facultys/',views.Facultys ,name='Facultys'),
    path('edit_Facultys/<Fac_id>', views.edit_Facultys, name = 'edit_Facultys'),
    path('delete_Facultys/<Fac_id>',views.delete_Facultys ,name='delete_Facultys'),
    #path('SearchFacultys/', views.SearchFacultys,name='SearchFacultys'),
    path('Collmajor/',views.Collmajor ,name='Collmajor'),
    path('SearchCollmajor/', views.SearchCollmajor,name='SearchCollmajor'),
    path('edit_Collmajor/<Collmajor_id>',views.edit_Collmajor ,name='edit_Collmajor'),
    path('delete_Collmajor/<Collmajor_id>',views.delete_Collmajor ,name='delete_Collmajor'),
    path('Major/',views.Majors ,name='Major'),
    path('Searchmajor/', views.Searchmajor,name='Searchmajor'),
    path('edit_Major/<Maj_id>', views.edit_Major, name = 'edit_Major'),
    path('delete_Major/<Maj_id>',views.delete_Major ,name='delete_Major'),
    path('Group/',views.Group ,name='Group'),
    path('edit_Group/<G_id>', views.edit_Group, name = 'edit_Group'),
    path('delete_Group/<G_id>', views.delete_Group, name = 'delete_Group'),
    path('Course/',views.Course ,name='Course'),
    path('EditCourse/',views.EditCourse ,name='EditCourse'),
    path('ModelTranfer/',views.ModelTranfer ,name='ModelTranfer'),
    path('Advisor/',views.Advisors ,name='Advisor'),
    path('edit_Advisor/<adv_id>/', views.edit_Advisor, name = 'edit_Advisor'),
    path('delete_Advisor/<adv_id>', views.delete_Advisor, name = 'delete_Advisor'),
    path('Admin/',views.Admin ,name='Admin'),
    path('edit_Admin/<ad_id>/', views.edit_Admin, name = 'edit_Admin'),
    path('delete_Admin/<ad_id>', views.delete_Admin, name = 'delete_Admin'),
    path('Tranfer/',views.Tranfer ,name='Tranfer'),
    path('Category/',views.Category ,name='Category'),
    path('edit_Category/<cg_id>/', views.edit_Category, name = 'edit_Category'),
    path('deleteCategory/<cg_id>', views.delete_Category, name = 'delete_Category'),
    
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
