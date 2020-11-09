from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('corporate',views.corporate,name='corporate'),
    path('wedding',views.wedding,name='wedding'),
    path('package1',views.package1,name='package1'),
    path('registration',views.registration,name='registration'),
    path('dcorporate',views.dcorporate,name='dcorporate'),
    path('add',views.add,name='add'),
    path('dwedding',views.dwedding,name='dwedding'),
    path('addd',views.addd,name='addd'),
    path('birthday',views.birthday,name='birthday'),
    path('dbirthday',views.dbirthday,name='dbirthday'),
    path('adddd',views.adddd,name='adddd'),
    path('handlespecialupload',views.handlespecialupload,name='handlespecialupload'),
    path('dreview',views.dreview,name='dreview'),
    path('addddd',views.addddd,name='addddd'),
    path('show',views.show,name='show'),
    path('dlogin',views.dlogin,name='dlogin'),
    path('action',views.action,name='action'),
    path('ac',views.ac,name='ac'),
    path('about',views.about,name='about'),
    path('registerr',views.registerr,name='registerr'),
    path('registeradmin',views.registeradmin,name='registeradmin'),
    path('addadmin',views.addadmin,name='addadmin'),
    path('addregi',views.addregi,name='addregi'),
    path('index',views.index,name='index'),
]
