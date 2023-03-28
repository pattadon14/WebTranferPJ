from django.shortcuts import render,redirect,HttpResponse
from .models import College,Coll_Major,Faculty,Major,Groups,User,Advisor,Student,Cur_Group,Cur_Head,Cur_Detail
from django.contrib import messages
from django.contrib.auth.models import User


####### Normal #######

def Home(request):
    return render(request,'Home.html')

def Register(request):
    return render(request,'Register.html')

def LoginStudent(request):
    return render(request,'Login_Stu.html')

def LoginAdvisor(request):
    return render(request,'Login_Advisor.html')

def LoginAdmin(request):
    return render(request,'Login_Admin.html')


#######  ADMIN  #######

def Collegepage(request):
    context = {}
    if request.method == "POST":
        data = request.POST.copy()
        C_name = data.get('C_name')
        
        newcollege = College()
        newcollege.C_name = C_name
        newcollege.save()
        context['status'] = 'Success'
        
    #Query Data from database
    data = College.objects.all()
    return render(request, 'Admin_Colleges.html',{'colleges': data})

def edit_college(request,college_id):
    if request.method == "POST":
        data = College.objects.get(id=college_id)
        data.C_name = request.POST["C_name"]
        data.save()
        return redirect('collegepage')
    else:
        data = College.objects.get(id=college_id)
        return render(request,'Edit_College.html',{'colleges': data})
    
def delete_college(request,college_id):
    data = College.objects.get(id=college_id)
    data.delete()
    return redirect('collegepage')

def CollMajor(request):
    context = {}
    if request.method == "POST":
        data = request.POST.copy()
        Cmj_name = data.get('Cmj_name')
        Coll_name = data.get('Coll_name')
        
        newCmjcolleeg = Coll_Major()
        newCmjcolleeg.Cmj_name = Cmj_name
        newCmjcolleeg.Coll_name_id = Coll_name
        newCmjcolleeg.save()
        context['status'] = 'Success'
        
    data = College.objects.all()
    all_Coll_Majors = Coll_Major.objects.all()
    return render(request,'Admin_Coll_Major.html',{'all_Coll_Majors': all_Coll_Majors,'colleges': data})


def Facultys(request):
    context = {}
    if request.method == "POST":
        all_Facultys = request.POST.copy()
        Fac_Name = all_Facultys.get('Fac_Name')
        
        newfacultys = Faculty()
        newfacultys.Fac_Name = Fac_Name
        newfacultys.save()
        context['status'] = 'Success'
        
    all_Facultys = Faculty.objects.all()
    return render(request,'Admin_Faculty.html',{'all_Facultys': all_Facultys})


def Majors(request):
    context = {}
    if request.method == "POST":
        all_Majors = request.POST.copy()
        Mj_name = all_Majors.get('Mj_name')
        Fac_name = all_Majors.get('Fac_Name')
        
        newmajor = Major()
        newmajor.Mj_Name = Mj_name
        newmajor.Fac_name_id = Fac_name
        newmajor.save()
        context['status'] = 'Success'

    all_Facultys = Faculty.objects.all()
    all_Majors = Major.objects.all()
    return render(request,'Admin_Major.html',{'all_Majors': all_Majors,'all_Facultys':all_Facultys})


def Group(request):
    context = {}
    if request.method == "POST":
        all_Groups = request.POST.copy()
        G_name = all_Groups.get('G_name')
        Mj_name = all_Groups.get('Mj_name')
        Fac_name = all_Groups.get('Fac_Name')
        
        newgroup = Groups()
        newgroup.G_Name = G_name
        newgroup.Mj_Name_id  = Mj_name
        newgroup.Fac_name_id = Fac_name
        newgroup.save()
        context['status'] = 'Success'  

    all_Majors = Major.objects.all()
    all_Facultys = Faculty.objects.all()
    all_Groups = Groups.objects.all()
    return render(request,'Admin_Group.html',{'all_Groups': all_Groups,'all_Majors':all_Majors,'all_Facultys':all_Facultys})


def Advisors(request):
    return render(request,'Admin_Advisor.html')

def Course(request):
    return render(request,'Admin_Course.html')

def EditCourse(request):
    return render(request,'Admin_Edit_Course.html')

def ModelTranfer(request):
    return render(request,'Admin_Model_Tranfer.html')

def Admin(request):
    return render(request,'Admin.html')

def Tranfer(request):
    return render(request,'Admin_Tranfer.html')


#ADVISOR
def AdvisorShowStudent(request):
    return render(request,'Advisor_Show_Student.html')

def AdvisorCheckTranfer(request):
    return render(request,'Advisor_Check_Tranfer.html')



 #ADMIN + ADVISOR

def CheckSubject(request):
    return render(request,'Check_Subject.html')

def CheckSubjectCategory(request):
    return render(request,'Check_Subject_Category.html')

def CheckCourse(request):
    return render(request,'Check_Course.html')


#STUDENT

def Stu_Tranfer(request):
    return render(request,'Student_SaveTranfer.html')

def Stu_GPA(request):
    return render(request,'Student_SaveGPA.html')

def Stu_Edit(request):
    return render(request,'Student_EditProfile.html')

def Stu_checkcouse(request):
    return render(request,'Stedent_CheckCouse.html')