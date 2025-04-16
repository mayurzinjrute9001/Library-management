from django.views import View
from LMS_APP.models.student_log import Student
from django.shortcuts import render,redirect
from django.contrib import messages

class StudentRegisterView(View):
    def get(self, request):
        return render(request, 'student/register.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('student_register')

        Student.objects.create(name=name, email=email, password=password)
        messages.success(request, 'Registered successfully. Please login.')
        return redirect('student_login')