from django.shortcuts import render, redirect
from store.models import *
# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("This is a test.")
def index(request):
    return render(request, 'index.html')
def text(request):
    return render(request, 'text.html')
def fibo(request):
    n1, n2 = 0, 1
    fib_sequence = []
    for _ in range(int(request.GET['n'])):
        fib_sequence.append(n1)
        n1, n2 = n2, n1 + n2
    return HttpResponse(f"Fibonacci sequence: {', '.join(map(str, fib_sequence))}")
def cal(request):
    return render(request, 'cal.html')
def calculate(request):
    try:

        num1 = int(request.GET['a'])
        num2 = int(request.GET['b'])
        if 'add' in request.GET:
            result = num1 + num2
        elif 'subtract' in request.GET:
            result = num1 - num2
        elif 'multiply' in request.GET:
            result = num1 * num2
        elif 'divide' in request.GET:
            result = num1 / num2 if num2 else "Undefined (division by zero)"
        # operation = request.GET['operation']
        # if operation == 'add':
        #     result = num1 + num2
        # elif operation == 'subtract':
        #     result = num1 - num2
        # elif operation == 'multiply':
        #     result = num1 * num2
        # elif operation == 'divide':
        #     result = num1 / num2 if num2 else "Undefined (division by zero)"
            # return HttpResponse("Invalid operation.")
            
        return render(request, 'cal.html', {'result': result})
    except ValueError:
        return HttpResponse("Invalid input. Please enter numeric values.")
def insert(request):
    return render(request, 'insert.html') 
def ins(request):
    u = user()

    u.name = request.GET['username']
    u.email = request.GET['email']
    u.phno = request.GET['ph']
    u.pwd = request.GET['password']
    u.age = request.GET['age']
    u.save()
    return render(request, 'insert.html')
    
def student_view(request):
    return render(request, 'student.html')
def insstud(request):
    s = student()
    s.fname = request.GET['fname']
    s.lname = request.GET['lname']
    s.age = request.GET['age']
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
    return redirect('../store/student')

def show(request):
    u= user.objects.all()
    return render(request, 'show.html', {'data':u})
def dele(request, id):
    u = user.objects.get(id=id)
    u.delete()
    return redirect('/store/show')
def edit(request, id):
    u = user.objects.get(id=id)
    return render(request, 'edit.html', {'data':u})
def update(request, id):
    u = user.objects.get(id=id)
    u.name = request.GET['name']
    u.email = request.GET['email']
    u.phno = request.GET['phno']
    u.pwd = request.GET['pwd']
    u.age = request.GET['age']
    u.save()
    return redirect('/store/show')
