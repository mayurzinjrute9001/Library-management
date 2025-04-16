from django.views import View
from django.shortcuts import redirect,render
from LMS_APP.models.admin_log import Admin
from django.contrib import messages

class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        try:
            admin = Admin.objects.get(email=email, password=password)
            request.session['admin_id'] = admin.id
            return redirect('admin_dashboard')
        except Admin.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'admin_login.html')

class AdminLogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('admin_login')