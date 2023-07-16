from django import forms
from Webtranfer.models import *

# class CollegeForm(forms.ModelForm):
#     class Meta:
#         model = College
#         fields ="__all__"
#         labels={
#             'C_name' :'ชื่อโรงเรียน'
#         }

class CollegeForm(forms.ModelForm):
    C_name = forms.CharField(label='ชื่อโรงเรียน', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'กรอกชื่อโรงเรียน'}))

    class Meta:
        model = College
        fields = "__all__"
        labels = {
            'C_name': 'ชื่อโรงเรียน'
        }


class Coll_MajorForm(forms.ModelForm):
    class Meta:
        model = Coll_Major
        Cmj_name = []
        fields =[
            'Coll_name',
            'Cmj_name'
        ]
        labels={
            'Coll_name': 'ชื่อโรงเรียน',
            'Cmj_name':'ชื่อสาขา'
        }



class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields ="__all__"
        labels={
            'Fac_Name':'ชื่อคณะ'
        }

class SearchCollege(forms.Form):
    Coll_name = forms.ModelChoiceField(queryset=College.objects.all(),label='ชื่อโรงเรียน')

class SearchFacultys(forms.Form):
    Fac_Name = forms.ModelChoiceField(queryset=Faculty.objects.all(),label='ชื่อคณะ')

class searchmajor(forms.Form):
    Fac_name = forms.ModelChoiceField(queryset=Faculty.objects.all(),label='ชื่อคณะ')


class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        Mj_Name = []
        fields =[
            'Fac_name',
            'Mj_Name'
        ]
        labels={
            'Fac_name':'ชื่อคณะ',
            'Mj_Name':'ชื่อสาขา'
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields =[
            'Fac_name',
            'Mj_Name',
            'G_Name'
        ]
        labels={
            'Fac_name':'ชื่อคณะ',
            'Mj_Name':'ชื่อสาขา',
            'G_Name':'ชื่อกลุ่ม'
        }

class AdminForm(forms.ModelForm):
    class Meta:
        model = Useradmin
        fields = [
            'Adm_Fname',
            'Adm_Lname',
            'Username', 
            'Password']
        labels={
            'Adm_Fname':'ชื่อ',
            'Adm_Lname':'นามสกุล',
            'Username':'ชื่อผู้ใช้', 
            'Password':'รหัสผ่าน'
        }
        widgets = {"Password": forms.PasswordInput()}


class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields =[
            'Fac_Name',
            'Mj_Name',
            'Adv_Fname',
            'Adv_Lname',
            'Username',
            'Password'
        ]
        labels={
            'Fac_Name':'ชื่อคณะ',
            'Mj_Name':'ชื่อสาขา',
            'G_Name':'ชื่อกลุ่ม',
            'Adv_Fname':'ชื่อ',
            'Adv_Lname':'นามสกุล',
        }
        widgets = {"Password": forms.PasswordInput()}

class Cur_GroupForm(forms.ModelForm):
    class Meta:
        model = Cur_Group
        fields ="__all__"
        labels={
            'CG_ID':'รหัสหมวด',
            'CG_Name':'ชื่อหมวด'}
        
