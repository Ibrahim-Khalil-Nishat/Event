from django.shortcuts import render,redirect
from .forms import DcorporateForm,DweddingForm,DbirthdayForm,specialuploadform,ReviewForm,registerform,adminregisterform
from .models import specialupload,Review,register, Dwedding,Dcorporate,Dbirthday,adminregister
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
#from django.contrib.auth import authenticate, login
#from .models import registe
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.models import Permission



# Create your views here.
def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def corporate(request):
    return render(request,'corporate.html')


def wedding(request):
    return render(request,'wedding.html')


def package1(request):
    return render(request,'package1.html')

def registration(request):
    return render(request,'registration.html')
#corporate section
def dcorporate(request):
    form=DcorporateForm
    return render(request,'dcorporate.html',{'form':form})


def add(request):
     if request.method=="POST":
        name=request.POST['name']
        Details=request.POST['Details']
        date=request.POST['date']
        address=request.POST['address']
        contact=request.POST['contact']
        Email=request.POST['Email']
       # password=request.POST['password']
        if Dcorporate.objects.filter(contact=contact).exists():
            messages.success(request,"Try another number")
            return redirect('dcorporate')
    
        else:
            form=DcorporateForm(request.POST)
           # if form.is_valid():
            form.save()
            return redirect('index')

     else:
        return redirect("Dcorporate")

"""
    form=DcorporateForm(request.POST)
    form.save()
    return redirect("/")
"""
#wedding section

def dwedding(request):
    form=DweddingForm
    return render(request,'dwedding.html',{"form":form})

def addd(request):
    if request.method=="POST":
        name=request.POST['name']
        package=request.POST['package']
        date=request.POST['date']
        address=request.POST['address']
        contact=request.POST['contact']
        Email=request.POST['Email']
       # password=request.POST['password']
        if  Dwedding.objects.filter(contact=contact).exists():
            messages.info(request,"Try another number")
            return redirect('dwedding')
        elif Dwedding.objects.filter(Email=Email).exists():
            messages.info(request,"Try another one")
            return redirect('dwedding')
        else:
            form=DweddingForm(request.POST)
           # if form.is_valid():
            form.save()
            return redirect('index')

    else:
        return redirect("dwedding")


    """
    form=DweddingForm(request.POST)
    form.save()
    return redirect('index')
    """

#birthday section

def birthday(request):
    return render(request,'birthday.html')

def dbirthday(request):
    form=DbirthdayForm
    return render(request,'dbirthday.html',{'form':form})
    

def adddd(request):
        if request.method=="POST":
            name=request.POST['name']
            Details=request.POST['Details']
            date=request.POST['date']
            address=request.POST['address']
            contact=request.POST['contact']
            Email=request.POST['Email']
       # password=request.POST['password']
            if Dbirthday.objects.filter(contact=contact).exists():
                messages.info(request,"Try another number")
                return redirect('dbirthday')
            elif Dbirthday.objects.filter(Email=Email).exists():
                messages.info(request,"Try another one")
                return redirect('dbirthday')
            else:
                form=DbirthdayForm(request.POST)
           # if form.is_valid():
                form.save()
                return redirect('index')

        else:
            return redirect("dbirthday")









"""
    form=DbirthdayForm(request.POST)
    form.save()
    return redirect('index')
"""


def handlespecialupload(request):
    if request.method=='POST':
        form=specialuploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('handlespecialupload')
    else:
      form=specialuploadform()
    uploads = specialupload.objects.all
    return render(request,'gallery.html',{'form':form,'uploads': uploads})

def dreview(request):
    form=ReviewForm
    return render(request,'review.html',{'form':form})

def addddd(request):
    form=ReviewForm(request.POST)
    form.save()
    return redirect('show')


def show(request):
    review=Review.objects.all
    return render(request,'show.html',{'review':review})

#Login part

def dlogin(request):
    if request.method=='POST':
        """
        form=registerform(data=request.POST)
        if form.is_valid():
           #password=request.POST['password']
           #number=request.POST['number']
           user = user.objects.get_for_model(register)
           login(request,user)
           return redirect('/')

        else:
            form=registerform()
            return redirect('registerr')

    else:
        return render(request,'login.html')
        """
        #password=request.POST['password']
        number= request.POST['number']
        #form=registerform()
        #x=register.authenticate(request,password=password,number=number)
        x=register.objects.filter(number=number).exists()
        if x  :
            #login(request,x)
            
            return redirect('index')
        else: 
            messages.error(request,'invalid')
            return redirect('dlogin')
        
    else:
        return render(request,'login.html')



#Email part Exercise

def action(request):
    #if request.method=="POST":
       # message=request.POST['message']
        send_mail('contact form',
            'hey i am nishat',
            'ibrahimnishat1057@gmail.com',
            ['ibrahimnishat714786@gmail.com'],
            fail_silently=False,
            )
        return render(request,'email.html')

def ac(request):
    subject="real programmer"
    meg="congration for email"
    to='ibrahimnishat1057@gmail.com'
    res=send_mail(subject,meg,settings.EMAIL_HOST_USER,[to])
    if (res==1):
        msg="message sent"
    else:
        meg="message not sent"
    return HttpResponse(msg)


    #About page
def about(request):
    return render(request,'about.html')

def registerr(request):
    form=registerform
    return render(request,'register.html',{'form':form})

def addregi(request):
    if request.method=="POST":
        name=request.POST['name']
        number=request.POST['number']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if register.objects.filter(number=number).exists():
            messages.info(request,"Number Matching! Try another ")
            return redirect('registerr')
        elif register.objects.filter(password=password).exists():
            messages.info(request,"password matching! Try another")
            return redirect('registerr')
        else:
            form=registerform(request.POST)
           # if form.is_valid():
            form.save()
            return redirect('dlogin')

    else:
        return redirect("register")
    """
    ########
        user=register.objects.get(name=name,number=number,username=username,email=email,password=password)
        user.save()
        print("user created")
        return redirect('/')

    else:
        return render(request,'register.html')

       
        if register.objects.get(number==number).exists():
            print("username taken")
        else:
            form=registerform(request.POST)
           # if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=registerform()
    #return render(request,'')



    if request.method=="POST":
        name=request.POST['name']
        number=request.POST['number']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user=register.objects.create_user(name=name,number=number,username=username,email=email,password=password1)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request,'register.html')
 """
def registeradmin(request):
    form=adminregisterform
    return render(request,'adminregi.html',{'form':form})

def addadmin(request):
    if request.method=="POST":
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        if adminregister.objects.filter(number=number).exists():
            messages.info(request,"Number Matching!Try another")
            return redirect('registeradmin')
        elif adminregister.objects.filter(password=password).exists():
            messages.info(request,"Password Matching!Try another")
            return redirect('registeradmin')
        else:
            form= adminregisterform(request.POST)
           # if form.is_valid():
            form.save()
            return redirect('/')

    else:
        return redirect("registeradmin")
