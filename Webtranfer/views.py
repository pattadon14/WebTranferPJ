from django.shortcuts import render,redirect,HttpResponseRedirect
from Webtranfer.models import * 
from django.contrib import messages
from django.contrib.auth.models import User
from Webtranfer.forms import *
from django.db.models import Q

####Test#######

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
    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid():
            C_name = form.cleaned_data['C_name']
            if  College.objects.filter(C_name__contains=C_name).exists():
                messages.error(request, 'คุณกรอกข้อมูลซ้ำ')
                return redirect('/Collegepage/')
            else:
                form.save()
                messages.success(request,"บันทึกข้อมูลสำเร็จ")
                #all_college = College.objects.all()
                return redirect('/Collegepage/')
    else:
        form = CollegeForm()
        all_college = College.objects.all()
        return render(request,'Admin_Colleges.html',{'form': form,'all_college': all_college})


def edit_college(request,college_id):
    if request.method =="POST":
         college = College.objects.get(pk=college_id)
         form = CollegeForm(instance=college,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('/Collegepage/')
    else:
        college = College.objects.get(pk=college_id)
        form= CollegeForm(initial= college.__dict__)
    return render(request,'Admin_EditCollege.html',{"form":form})
   

def delete_college(request,college_id):
    data = College.objects.get(pk=college_id)
    data.delete()
    return redirect('/Collegepage/')


def Collmajor(request):
    if request.method == "POST":
        form = Coll_MajorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            all_Coll_Major = Coll_Major.objects.all()
            return redirect('/Collmajor/')
    else:
        form = Coll_MajorForm()
        all_Coll_Major = Coll_Major.objects.all()
    return render(request,'Admin_Coll_Major.html',{'form': form,'all_Coll_Major': all_Coll_Major})


def edit_Collmajor(request,Collmajor_id):
    if request.method =="POST":
         all_Coll_Major = Coll_Major.objects.get(pk=Collmajor_id)
         form = Coll_MajorForm(instance=all_Coll_Major,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('/Collmajor/')
    else:
        all_Coll_Major = Coll_Major.objects.get(pk=Collmajor_id)
        form= Coll_MajorForm(initial= all_Coll_Major.__dict__)
    return render(request,'Admin_EditCollMajor.html',{"form":form})


def delete_Collmajor(request,Collmajor_id):
    data = Coll_Major.objects.get(pk=Collmajor_id)
    data.delete()
    return redirect('/Collmajor/')


def SearchCollmajor(request):
    if request.method == 'POST':
        search_form = SearchCollege(request.POST)
        if search_form.is_valid():
            Coll_name = search_form.cleaned_data['Coll_name']
            datacollege = Coll_Major.objects.filter(Coll_name=Coll_name)
            return render(request, 'Admin_SearchCollmajor.html',{'search_form': search_form,'datacollege': datacollege})
    else:
        search_form = SearchCollege()
    return render(request, 'Admin_SearchCollmajor.html', {'search_form': search_form})


def Facultys(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            all_Facultys = Faculty.objects.all()
            return redirect('/Facultys/') 
    else:
        form = FacultyForm()
        all_Facultys = Faculty.objects.all()
    return render(request, 'Admin_Faculty.html', {'form': form,'all_Facultys':all_Facultys})


def edit_Facultys(request,Fac_id):
    if request.method =="POST":
         all_Facultys = Faculty.objects.get(pk=Fac_id)
         form = FacultyForm(instance=all_Facultys,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('Facultys')
    else:
        all_Facultys = Faculty.objects.get(pk=Fac_id)
        form= FacultyForm(initial= all_Facultys.__dict__)
    return render(request,'Admin_EditFaculty.html',{"form":form})


def delete_Facultys(request,Fac_id):
    all_Facultys = Faculty.objects.get(pk=Fac_id)
    all_Facultys.delete()
    return redirect('Facultys')


#def findFacultys(request):
    if request.method == 'POST':
        search_form = SearchFaculty(request.POST)
        if search_form.is_valid():
            Fac_Name = search_form.cleaned_data['Fac_Name']
            dataFacultys = Faculty.objects.filter(Fac_Name=Fac_Name)
            return render(request, 'Admin_FindFaculty.html',{'search_form': search_form,'dataFacultys': dataFacultys})
    else:
        search_form = SearchFaculty()
    return render(request, 'Admin_FindFaculty.html', {'search_form': search_form})


def Majors(request):
    if request.method == "POST":
        form = MajorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            all_Major = Major.objects.all()
            return redirect('/Major/')
    else:
        form = MajorForm()
        all_Major = Major.objects.all()
    return render(request,'Admin_Major.html',{'form': form,'all_Major': all_Major})


def Searchmajor(request):
    if request.method == 'POST':
        search_form = searchmajor(request.POST)
        if search_form.is_valid():
            Fac_name = search_form.cleaned_data['Fac_name']
            all_Major = Major.objects.filter(Fac_name=Fac_name)
            return render(request, 'Admin_SearchMajor.html', {'search_form': search_form,'all_Major': all_Major})
    else:
        search_form = searchmajor()
    
    return render(request, 'Admin_SearchMajor.html', {'search_form': search_form})


def edit_Major(request,Maj_id):
    if request.method =="POST":
         all_Major = Major.objects.get(pk=Maj_id)
         form = MajorForm(instance=all_Major,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('Major')
    else:
        all_Major = Major.objects.get(pk=Maj_id)
        form= MajorForm(initial= all_Major.__dict__)
    return render(request,'Admin_EditMajor.html',{"form":form})


def delete_Major(request,Maj_id):
    all_Major = Major.objects.get(pk=Maj_id)
    all_Major.delete()
    return redirect('Major')


def Group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            all_group = Groups.objects.all()
            return redirect('Group')
    else:
        form = GroupForm()
        all_group = Groups.objects.all()
    return render(request,'Admin_Group.html',{'form': form,'all_group': all_group})


def edit_Group(request,G_id):
    if request.method =="POST":
         all_group = Groups.objects.get(pk=G_id)
         form = GroupForm(instance=all_group,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('Group')
    else:
        all_group = Groups.objects.get(pk=G_id)
        form= GroupForm(initial= all_group.__dict__)
    return render(request,'Admin_EditGroup.html',{"form":form})


def delete_Group(request,G_id):
    all_group = Groups.objects.get(pk=G_id)
    all_group.delete()
    return redirect('Group')


def Advisors(request):
    if request.method == 'POST':
        form = AdvisorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"เพิ่มข้อมูล Advisor เรียบร้อย")
            all_Adv = Advisor.objects.all()
            return redirect('Advisor') 
    else:
        form = AdvisorForm()
        all_Adv = Advisor.objects.all()
    return render(request, 'Admin_Advisor.html', {'form': form,'all_Adv':all_Adv})

def edit_Advisor(request,adv_id):
    if request.method =="POST":
         all_Adv = Advisor.objects.get(pk=adv_id)
         form = AdvisorForm(instance=all_Adv,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('Advisor')
    else:
        all_Adv = Advisor.objects.get(pk=adv_id)
        form= AdvisorForm(initial= all_Adv.__dict__)
    return render(request,'Admin_EditAdvisor.html',{"form":form})

def delete_Advisor(request,adv_id):
    all_Adv = Advisor.objects.get(pk=adv_id)
    all_Adv.delete()
    return redirect('Advisor')



def Course(request):
    return render(request,'Admin_Course.html')


def EditCourse(request):
    return render(request,'Admin_Edit_Course.html')


def ModelTranfer(request):
    return render(request,'Admin_Model_Tranfer.html')


def Admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"เพิ่มข้อมูล Admin เรียบร้อย")
            all_Admin = Useradmin.objects.all()
            return redirect('Admin') 
    else:
        form = AdminForm()
        all_Admin = Useradmin.objects.all()
    return render(request, 'Admin.html', {'form': form,'all_Admin':all_Admin})

def edit_Admin(request,ad_id):
    if request.method =="POST":
         all_Admin = Useradmin.objects.get(pk=ad_id)
         form = AdminForm(instance=all_Admin,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('Admin')
    else:
       all_Admin = Useradmin.objects.get(pk=ad_id)
       form= AdminForm(initial= all_Admin.__dict__)
    return render(request,'Admin_EditAdmin.html',{"form":form})

def delete_Admin(request,ad_id):
    all_Admin = Useradmin.objects.get(pk=ad_id)
    all_Admin.delete()
    return redirect('Admin')



def Tranfer(request):
    return render(request,'Admin_Tranfer.html')

def Category(request):
    if request.method == 'POST':
        form = Cur_GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"เพิ่มข้อมูล Admin เรียบร้อย")
            all_Cur_Group = Cur_Group.objects.all()
            return redirect('Category') 
    else:
        form = Cur_GroupForm()
        all_Cur_Group = Cur_Group.objects.all()
    return render(request,'Admin_Category.html',{'form': form,'all_Cur_Group':all_Cur_Group})


def edit_Category(request,cg_id):
    if request.method =="POST":
         all_Cur_Group = Cur_Group.objects.get(pk=cg_id)
         form = Cur_GroupForm(instance=all_Cur_Group,data=request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"อัปเดตข้อมูลเรียบร้อย")
             return redirect('Category')
    else:
       all_Cur_Group = Cur_Group.objects.get(pk=cg_id)
       form= Cur_GroupForm(initial= all_Cur_Group.__dict__)
    return render(request,'Admin_EditCategory.html',{"form":form})

def delete_Category(request,cg_id):
    all_Cur_Group = Cur_Group.objects.get(pk=cg_id)
    all_Cur_Group.delete()
    return redirect('Category')


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