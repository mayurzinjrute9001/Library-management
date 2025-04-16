from django.views import View
from LMS_APP.models.student_log import Student
from django.shortcuts import render,redirect
from django.contrib import messages
class StudentLoginView(View):
    def get(self, request):
        return render(request, 'student/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        student = Student.objects.filter(email=email, password=password).first()
        if student:
            request.session['student_id'] = student.id
            request.session['student_name'] = student.name
            return redirect('student_view_books')
        messages.error(request, 'Invalid credentials')
        return redirect('student_login')


class StudentLogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('student_login')