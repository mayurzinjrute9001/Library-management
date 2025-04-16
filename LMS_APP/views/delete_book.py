from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from LMS_APP.models.admin_log import Admin
from LMS_APP.models.book import Book
from django.contrib import messages

class DeleteBookView(View):
    def get(self, request, id):
        if 'admin_id' not in request.session:
            return redirect('admin_login')

        book = get_object_or_404(Book, id=id)
        book.delete()
        messages.success(request, 'Book deleted successfully.')
        return redirect('admin_dashboard')
