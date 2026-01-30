from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('registration', views.registration, name='registration'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('sdetails', views.sdetails, name='sdetails'),
    path('insstud', views.insstud, name='insstud'),
    path('insertdata', views.insertdata, name='insertdata'),
    path('insabout', views.insabout, name='insabout'),
    path('inscontact', views.inscontact, name='inscontact'),
    path('dele/<int:id>', views.dele, name='dele'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('second', views.second, name='second'),
    path('search', views.search, name='search'),
    path('searchdata', views.searchdata, name='searchdata'),
    path('searchdatakol', views.searchdatakol, name='searchdatakol'),
    path('userreg', views.userreg, name='userreg'),
    path('register_user', views.register_user, name='register_user'),
    path('login/', views.login, name='login'),
    path('islogin', views.islogin, name='islogin'),
    path('logout', views.logout, name='logout'),
    path('privilage', views.view_privilage, name='privilage'),
    path('setprivilage', views.setprivilage, name='setprivilage'),
    path('send_mail', views.send_email, name='send_mail'),
    path('send-500-emails', views.send_500_emails, name='send_500_emails')
]