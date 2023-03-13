
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('faq',views.faqview,name="faq"),
    path('fcdisclaimer',views.disclaimer,name="disclaimer"),
    path('visasuccess',views.visasuccess,name="visasuccess"),
    path('fcprivacypolicy',views.privacypolicy,name="privacypolicy"),
    path('english-proficiency-test',views.testprep,name="testprep"),
    path('english-proficiency-test/toefl',views.testprep_toefl,name="testprep_toefl"),
    path('english-proficiency-test/ielts',views.testprep_ielts,name="testprep_ielts"),
    path('english-proficiency-test/gre',views.testprep_gre,name="testprep_gre"),
    path('english-proficiency-test/pte',views.testprep_pte,name="testprep_pte"),
    path('aboutus',views.companyprofile,name="companyprofile"),
    path('universities',views.university,name="university"),
    path('search', views.UniversityViewSearch,name="search"),
    path('service', views.service,name="service"),
    path('study-in-uk', views.uk,name="uk"),
    path('study-in-africa', views.africa,name="africa"),
    path('study-in-asia', views.asia,name="asia"),
    path('study-in-australia', views.australia,name="australia"),
    path('study-in-canada', views.canada,name="canada"),
    path('study-in-europe', views.europe,name="europe"),
    path('study-in-ireland', views.ireland,name="ireland"),
    path('study-in-new-zealand', views.newzealand,name="newzealand"),
    path('study-in-usa', views.usa,name="usa"),
    path('study-in-france', views.france,name="france"),
    path('study-in-germany', views.germany,name="germany"),
    path('blog', views.allblog,name="blog"),
    path('blog/<pk>', views.singleblog,name="singleblog"),
    path('contact-us', views.contactus,name="contactus"),
    path('partner-franchise', views.franchise,name="franchise"),
    path('register/', views.popupregister, name='register'),
    path('future-counselor-landing', views.landingpage, name='landingpage'),
    path('future-counselor-landing/form', views.landingpageform, name='landingpageform'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)