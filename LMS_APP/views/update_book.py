from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from LMS_APP.models.admin_log import Admin
from LMS_APP.models.book import Book
from django.contrib import messages


class UpdateBookView(View):
    def get(self, request, id):
        if 'admin_id' not in request.session:
            return redirect('admin_login')

        book = get_object_or_404(Book, id=id)
        return render(request, 'admin_update_book.html', {'book': book})

    def post(self, request, id):
        if 'admin_id' not in request.session:
            return redirect('admin_login')

        book = get_object_or_404(Book, id=id)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.publication_date = request.POST['publication_date']
        book.save()
        messages.success(request, 'Book updated successfully.')
        return redirect('admin_dashboard')
