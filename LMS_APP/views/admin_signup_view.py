from django.views import View
from django.shortcuts import redirect,render
from LMS_APP.models.admin_log import Admin
from django.contrib import messages



class AdminSignupView(View):
    def get(self, request):
        return render(request, 'admin_signup.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if Admin.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            Admin.objects.create(name=name, email=email, password=password)
            messages.success(request, "Signup successful. Please log in.")
            return redirect('admin_login')
        return render(request, 'admin_signup.html')
