from django.contrib import admin
from LMS_APP.models.admin_log import Admin
from LMS_APP.models.book import Book
from LMS_APP.models.student_log import Student

# Register your models here.


admin.site.register(Admin)
admin.site.register(Book)
admin.site.register(Student)

