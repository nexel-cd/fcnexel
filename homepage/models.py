from django.db import models
from django.utils.text import slugify
los = (
    ("PG", "PG"),
    ("UG", "UG"),
)

# Create your models here.
class testmonial(models.Model):

    name = models.CharField( max_length=50)
    origin = models.CharField( max_length=50)
    discription = models.TextField()
    
    def __str__(self):
        return self.name
        

class videoTestmonial(models.Model):

    title = models.CharField( max_length=50)
    youtubelink = models.CharField(('youtube video code'), max_length=50)
    
    def __str__(self):
        return self.title

    
class Vlog(models.Model):

    title = models.CharField( max_length=50)
    youtubelink = models.CharField( max_length=50)
    discription = models.TextField()
    
    def __str__(self):
        return self.title
    
class blog(models.Model):

    title = models.CharField( max_length=120)
    image = models.ImageField(upload_to='blogimage',blank=True, null=True)
    discription = models.TextField()
    date = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class universities(models.Model):
    name = models.CharField(('University Name'),max_length=150 )
    Course = models.CharField(('Course'),max_length=250 )
    collegeimage = models.ImageField(upload_to='universityImage',blank=True, null=True)
    country = models.CharField(('Country'),max_length=150 )
    state = models.CharField(('State'),max_length=150 )
    los = models.CharField(('Level of Study'),choices=los,max_length=150 )
    duraction = models.CharField(('Duration'),max_length=150 )


class faq(models.Model):
    question = models.CharField(('Question'),max_length=250 )
    answer = models.CharField(('Question'),max_length=550 )

    def __str__(self):
        return self.question
    

class registration(models.Model):
    name = models.CharField(('Name'),max_length=250 )
    email = models.CharField(('Email'),max_length=250 )
    phono =models.CharField(('Phono'),max_length=250 )
    subject = models.CharField(('Subject'),max_length=250 )
    message = models.CharField(('Message'),max_length=250 )
    def __str__(self):
        return self.name

class mainregistration(models.Model):
    firstname = models.CharField(('First Name'),max_length=250 )
    lastname = models.CharField(('Last Name'),max_length=250 )
    phono = models.CharField(('Phono no'),max_length=250 )
    email =models.CharField(('Email'),max_length=250 )
    question =models.CharField(('Question'),max_length=250 )
    prefferedstudy = models.CharField(('Preffered Study'),max_length=250 )
    prefferedstudyyear =models.CharField(('Preffered Study Year'),max_length=250 )
    prefferedstudyintake = models.CharField(('Preffered study intake'),max_length=250 )
    message =models.CharField(('Any Message'),max_length=250 )
    def __str__(self):
        return self.firstname + self.lastname




class visasuccess(models.Model):
    name = models.CharField(("Name"), max_length=150)
    # title = models.CharField(("Origin"), max_length=150)
    # discripton = models.CharField(("Discription ( only 150 lines )"), max_length=150)
    img = models.ImageField(("Profile photo"), upload_to='visasuccess')
    def __str__(self):
        return self.name


class companytestmonial(models.Model):
    name = models.CharField(("Name"), max_length=150)
    origin = models.CharField(("Origin"), max_length=150)
    dis = models.CharField(("Discription"), max_length=250)
    img = models.ImageField(("Image"), upload_to='company Testmonial University image')
    def __str__(self):
        return self.name + "    " +self.origin
    

class newsletters(models.Model):
    email = models.EmailField(("Email"), max_length=254,null=True,blank=True)

    def __str__(self):
        return self.email