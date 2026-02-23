from django.shortcuts import render
from django.contrib import messages
from managementApp.models import *

# Create your views here.
def signin(request):
    return render(request,'singin.html')

def login(request):
    return render(request,'Loginpage.html')

def home(request):
    return render(request,'Homepage.html')

def about(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contactus.html')

def placement(request):
    return render(request,'placement.html')

def campus(request):
    return render(request,'campus.html')

def depcou(request):
    return render(request,'depcou.html')

def ac(request):
    return render(request,'AC.html')

def contactdata(request):
    name=request.GET.get('nm')
    num=request.GET.get('mno')
    mail=request.GET.get('email')
    message=request.GET.get('msg')

    obj=contactinformation(uname=name,unumber=num,uemail=mail,umessage=message)
    if(obj.save()):
        messages.error(request, "Details Submission Error..")
        return render(request,'contactus.html')
    else:
        messages.success(request, "Your Information Submitted Successfully..")
        return render(request,'contactus.html')

def admissiondata(request):
    snm=request.GET.get('nm')
    fnm=request.GET.get('fname')
    mnm=request.GET.get('mname')
    mail=request.GET.get('mail')
    num=request.GET.get('mno')
    cty=request.GET.get('city')
    st=request.GET.get('state')
    dst=request.GET.get('dist')
    sdob=request.GET.get('dob')
    sadhar=request.GET.get('adhar')
    sedu=request.GET.get('education')
    scat=request.GET.get('cat')
    sgndr=request.GET.get('gndr')
    scrse=request.GET.get('crse')

    obj=admissioninfo(sname=snm,sfname=fnm,smname=mnm,smail=mail,snumber=num,scity=cty,sstate=st,sdistrict=dst,sdob=sdob,saadhar=sadhar,seducation=sedu,scategory=scat,sgender=sgndr,scourse=scrse)


    if(obj.save()):
        messages.error(request, "Details Submission Error..")
        return render(request,'AC.html')
    else:
        messages.success(request, "Your Information Submitted Successfully.. we will get back to You in sometimes ..")
        return render(request,'AC.html')


def registerdata(request):
    unm=request.GET['un']
    uem=request.GET['em']
    ucn=request.GET['cn']
    upwd=request.GET['pwd']

    # if(len(upwd)<6):
    #     messages.error(request, "Password must be of 6 characters...")
    #     return render(request,'singin.html')

    obj=userregister(rname=unm,remail=uem,rnumber=ucn,rpassword=upwd)
    if(obj.save()):
        messages.error(request, "Details Submission Error..")
        return render(request,'singin.html')
    else:
        messages.success(request, "Your Information Submitted Successfully.. Now you can LOGIN to Website")
        return render(request,'singin.html')
    
def check(request):
    un=request.GET['lnc']
    pdw=request.GET['lpc']

    obj=userregister.objects.all().filter(rname=un)

    for i in obj:
        if un==i.rname and pdw==i.rpassword:
            return render(request,'Homepage.html')

    messages.error(request, "Sorry Your are not Register....")
    return render(request,'Loginpage.html')   


def latest(request):
    return render(request,'forgetpassword.html')


def changepwd(request):
    unm=request.GET['un']
    upwd=request.GET['pwd']

    obj=userregister.objects.all()
    for i in obj:
        if i.rname==unm:
            obj = userregister.objects.get(rname=unm)
            obj.rname=unm
            obj.rpassword=upwd
            obj.save()
            messages.success(request, "Password has been update sucessfully .... ")
            return render(request,'forgetpassword.html')
        

    messages.error(request, "No User Found..")
    return render(request,'forgetpassword.html')

    


    










