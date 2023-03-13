from django.shortcuts import render,redirect
from . models import universities
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect
from .models import registration, mainregistration,blog,testmonial,videoTestmonial,companytestmonial,newsletters,faq
from .models import visasuccess as visasuccessstory
# Create your views here. 


def newsletter(request):
    if request.method == "POST":
        emails = request.POST.get('newsletter')
        obj, created = newsletters.objects.get_or_create(email=emails)
        if not created:
            print('Object already exists in the database')
            messages.success(request, 'Email Already Exits')
        else:
            obj.save()
            messages.success(request, 'Email submitted successfully.')
            return redirect('homepage')

@csrf_exempt
def homepage(request):
    newsletter(request)
    testmonials=testmonial.objects.all()
    videotestmonials = videoTestmonial.objects.all()
    context = {
        'testmonial':testmonials,
        'videotestmonials':videotestmonials
    }
    return render(request,'index.html',context)

def disclaimer(request):
    newsletter(request)
    return render(request,'Disclaimer.html')

def faqview(request):
    newsletter(request)
    allfaq = faq.objects.all()
    return render(request,'faq.html',{'faq':allfaq})


def visasuccess(request):
    newsletter(request)
    visa = visasuccessstory.objects.all()
    context={'visa':visa}
    return render(request,'visasuccess.html',context)

def privacypolicy(request):
    newsletter(request)
    return render(request,'Privacy Policy.html') 

def testprep(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
    return render(request,'testprep.html')

def testprep_toefl(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
    return render(request,'toefl.html')

def testprep_ielts(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
    return render(request,'ielts.html')

def testprep_pte(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
    return render(request,'pte.html')

def testprep_gre(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
    return render(request,'gre.html')

def companyprofile(request):
    newsletter(request)
    testmonial = companytestmonial.objects.all()

    return render(request,'companyprofile.html', {'testmonial':testmonial})

def service(request):
    newsletter(request)
    return render(request,'services.html')




def uk(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'ukpage.html')


def usa(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'usa.html')
    
def canada(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'canada.html')

def australia(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'australia.html')
def newzealand(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'newzealand.html')
def ireland(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'ireland.html')
def europe(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'europe.html')
def asia(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'asia.html')
def africa(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'africa.html')

def france(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'france.html')

def germany(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        registeremail = request.POST.get('registeremail')
        registerphono = request.POST.get('registerphono')
        question = request.POST.get('question')
        if request.POST.get('firstname'):
            prestudy = request.POST['prestudy']
            studyyear = request.POST['studyyear']
            studyintake = request.POST['studyintake']
        mainmessage = request.POST.get('mainmessage')

        if firstname and lastname and registeremail and registerphono and question and prestudy and studyyear and studyintake and mainmessage:
            mainregistration.objects.create(firstname=firstname,lastname=lastname,phono=registerphono, email=registeremail, question=question, prefferedstudy=prestudy, prefferedstudyyear=studyyear, prefferedstudyintake=studyintake, message=mainmessage)
            
    return render(request,'germany.html')






def university(request):
    newsletter(request)
    university = universities.objects.all()
    paginator = Paginator(university, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'university': page_obj}
    return render(request,'searchuniversity.html',context)


def UniversityViewSearch(request):
    newsletter(request)
    query = request.GET['query']
    UniversitySearch = universities.objects.filter(Q(name__icontains = query) | Q(Course__icontains = query) | Q(country__icontains = query)| Q(los__icontains = query)| Q(state__icontains = query))
    paginator = Paginator(UniversitySearch, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'university': page_obj,'query':query}
    return render(request,'filteruniversity.html',context)






def allblog(request):
    newsletter(request)
    blogs = blog.objects.all().order_by("-id")
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blog':page_obj}
    return render(request,'blog.html',context)


def singleblog(request, pk):
    newsletter(request)
    blogs = blog.objects.all().order_by("?")[0:3]
    viewblog = blog.objects.filter(slug=pk)
    context={'blogdetail':viewblog,'blogs':blogs}
    return render(request,'singleblog.html',context)


def contactus(request):
    newsletter(request)
    return render(request,'contact.html')


def franchise(request):
    newsletter(request)
    return render(request,'franchise/index.html')


def footer(request):
    newsletter(request)
    blogs = blog.objects.all().order_by("?")[0:3]
    context={'mainblogs':blogs}
    return (context)


def popupregister(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phono = request.POST.get('phono')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phono and subject and message:
            registration.objects.create(name=name,email=email,phono=phono,subject=subject,message=message)
 
    return render(request,'registerpopup/registerform.html')  




def landingpage(request):
    newsletter(request)
    return render(request,'landingpage/index.html')

def landingpageform(request):
    newsletter(request)
    return render(request,'landingpage/form.html')