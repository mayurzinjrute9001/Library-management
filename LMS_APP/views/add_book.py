from django.views import View
from django.shortcuts import redirect,render
from LMS_APP.models.admin_log import Admin
from LMS_APP.models.book import Book
from django.contrib import messages


class AddBookView(View):
    def get(self, request):
        if not request.session.get('admin_id'):
            return redirect('admin_login')
        return render(request, 'admin_add_book.html')

    def post(self, request):
        if not request.session.get('admin_id'):
            return redirect('admin_login')

        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        pub_date = request.POST['publication_date']

        Book.objects.create(title=title, author=author, isbn=isbn, publication_date=pub_date)
        messages.success(request, 'Book added successfully.')
        return redirect('admin_dashboard')
