from django.views import View
from LMS_APP.models.book import Book
from django.shortcuts import render,redirect

class StudentViewBooks(View):
    def get(self, request):
        # Only allow if logged in as student
        if not request.session.get('student_id'):
            return redirect('student_login')
        books = Book.objects.all()
        return render(request, 'student/view_books.html', {'books': books})
