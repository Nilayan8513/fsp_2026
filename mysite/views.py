
from django.shortcuts import render, redirect
from mysite.models import *
from django.http import HttpResponse

def index(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    return render(request, 'home.html')
def registration(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_student_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    return render(request, 'registration.html')
# def about(request):
#     return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')

def sdetails(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.view_student_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    s= studentdata.objects.all()
    return render(request, 'sdetails.html',{'data':s})
def about(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    ab= aboutus.objects.all()
    # return render(request, 'show.html', {'data':u})
    return render(request, 'about.html',{'data':ab})
def contact(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    cu= contactus.objects.all()
    # return render(request, 'show.html', {'data':u})
    return render(request, 'contact.html',{'data':cu})
def insstud(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_student_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    s = studentdata()
    s.fname = request.GET['fname']
    s.lname = request.GET['lname']
    s.age = request.GET['age']
    s.dept = request.GET['dept']
    s.addrs = request.GET['addr']
    s.pincode = request.GET['pincode']
    s.city = request.GET['city']
    s.state = request.GET['state']
    s.fathers_name = request.GET['father']
    s.mothers_name = request.GET['mother']
    s.email = request.GET['email']
    s.phno = request.GET['ph']
    s.aadhar_no = request.GET['aadhaar']
    s.save()
    return redirect('../mysite/sdetails')

def insertdata(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_student_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    return render(request, 'insertdata.html')
def insabout(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_aboutus != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    a = aboutus()
    a.about = request.GET['about']
    a.save()
    return redirect('../mysite/about')
def inscontact(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_contactus != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    c = contactus()
    c.phno = request.GET['phone']
    c.email = request.GET['email']
    c.addr = request.GET['address']
    c.save()
    return redirect('../mysite/contact')
def dele(request, id):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.delete_students_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    s = studentdata.objects.get(id=id)
    s.delete()
    return redirect('/mysite/sdetails')
def edit(request, id):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_student_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    s = studentdata.objects.get(id=id)
    return render(request, 'edit.html', {'data':s})
def update(request, id):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.edit_student_details != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    s = studentdata.objects.get(id=id)
    s.fname = request.GET['fname']
    s.lname = request.GET['lname']
    s.age = request.GET['age']
    s.dept = request.GET['dept']
    s.addrs = request.GET['addr']
    s.pincode = request.GET['pincode']
    s.city = request.GET['city']
    s.state = request.GET['state']
    s.fathers_name = request.GET['father']
    s.mothers_name = request.GET['mother']
    s.email = request.GET['email']
    s.phno = request.GET['ph']
    s.aadhar_no = request.GET['aadhaar']
    s.save()
    return redirect('/mysite/sdetails')
def second(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    if request.session.get('role') != 'super-admin':
        return HttpResponse("You are not authorized to access this page.")
    return render(request, 'second.html')
def search(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.search_students_information != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    return render(request, 'search.html')
def searchdata(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.search_students_information != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    key = request.GET['branch']
    sd = studentdata.objects.filter(dept__contains=key)
    return render(request, 'search.html', {'data':sd})
def searchdatakol(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.search_students_information != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    city = request.GET['city']
    dept = request.GET['branch']
    sd = studentdata.objects.filter(city__contains=city, dept__contains=dept)
    return render(request, 'search.html', {'data':sd})
def userreg(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.manage_users != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    return render(request, 'userreg.html')
def register_user(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.manage_users != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    u = users()
    u.name = request.GET['name']
    u.email = request.GET['email']
    u.age = request.GET['age']
    u.pwd = request.GET['pwd']
    u.phno = request.GET['phno']
    u.role = request.GET['role']
    u.save()
    return redirect('../mysite/login')
def login(request):
    return render(request, 'login.html')
def islogin(request):

    email = request.GET['email']
    password = request.GET['password']
    try:
        u = users.objects.get(email=email, pwd=password)
        request.session['user'] = u.name
        request.session['role'] = u.role
        return render(request, 'home.html')
    except users.DoesNotExist:
        return HttpResponse("Invalid Credentials")
    
def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect('../mysite/login')
def view_privilage(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.manage_privileges != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    # p = privilage.objects.all()
    return render(request, 'privilage.html')
def setprivilage(request):
    if 'user' not in request.session:
        return redirect('../mysite/login')
    role = request.session.get('role')
    if role != 'super-admin':
        try:
            priv = privilage.objects.get(role=role)
            if priv.manage_privileges != 'yes':
                return HttpResponse("You are not authorized to access this page.")
        except privilage.DoesNotExist:
            return HttpResponse("You are not authorized to access this page.")
    r = request.GET['role']
    # Convert checkbox values: if present (value="yes"), set to "yes", otherwise "no"
    edit_aboutus = 'yes' if request.GET.get('edit_aboutus') else 'no'
    edit_contactus = 'yes' if request.GET.get('edit_contactus') else 'no'
    edit_student_details = 'yes' if request.GET.get('edit_student_details') else 'no'
    delete_students_details = 'yes' if request.GET.get('delete_students_details') else 'no'
    view_student_details = 'yes' if request.GET.get('view_student_details') else 'no'
    search_students_information = 'yes' if request.GET.get('search_students_information') else 'no'
    manage_users = 'yes' if request.GET.get('manage_users') else 'no'
    manage_privileges = 'yes' if request.GET.get('manage_privileges') else 'no'
    try:
        p = privilage.objects.get(role=r)
        p.edit_aboutus = edit_aboutus
        p.edit_contactus = edit_contactus
        p.edit_student_details = edit_student_details
        p.delete_students_details = delete_students_details
        p.view_student_details = view_student_details
        p.search_students_information = search_students_information
        p.manage_users = manage_users
        p.manage_privileges = manage_privileges
        p.save()
    except privilage.DoesNotExist:
        p = privilage()
        p.role = r
        p.edit_aboutus = edit_aboutus
        p.edit_contactus = edit_contactus
        p.edit_student_details = edit_student_details
        p.delete_students_details = delete_students_details
        p.view_student_details = view_student_details
        p.search_students_information = search_students_information
        p.manage_users = manage_users
        p.manage_privileges = manage_privileges
        p.save()
    return redirect('../mysite/privilage')