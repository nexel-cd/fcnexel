
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/futurecounselors/nexelgroup/dashboard/', admin.site.urls),
    path('',include('homepage.urls'))
]
