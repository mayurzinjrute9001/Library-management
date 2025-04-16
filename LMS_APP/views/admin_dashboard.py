from django.views import View
from django.shortcuts import redirect,render
from LMS_APP.models.admin_log import Admin
from LMS_APP.models.book import Book
from django.contrib import messages

class AdminDashboardView(View):
    def get(self, request):
        if 'admin_id' not in request.session:
            return redirect('admin_login')

        books = Book.objects.all()
        return render(request, 'admin_dashboard.html', {'books': books})
