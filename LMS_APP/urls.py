"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views.add_book import AddBookView
from .views.admin_dashboard import AdminDashboardView
from .views.admin_login import AdminLoginView, AdminLogoutView
from .views.admin_signup_view import AdminSignupView
from .views.delete_book import DeleteBookView
from .views.student_login import StudentLoginView, StudentLogoutView
from .views.student_register import StudentRegisterView
from .views.student_view import StudentViewBooks
from .views.update_book import UpdateBookView

urlpatterns = [
    path('admin_signup/', AdminSignupView.as_view(), name='admin_signup'),
    path('admin_login/', AdminLoginView.as_view(), name='admin_login'),
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin_logout/', AdminLogoutView.as_view(), name='admin_logout'),

    path('books/add/', AddBookView.as_view(), name='add_book'),
    path('books/update/<int:id>/', UpdateBookView.as_view(), name='update_book'),
    path('books/delete/<int:id>/', DeleteBookView.as_view(), name='delete_book'),

    path('student/books/', StudentViewBooks.as_view(), name='student_view_books'),
path('student/register/', StudentRegisterView.as_view(), name='student_register'),
path('student/login/', StudentLoginView.as_view(), name='student_login'),
path('student/logout/', StudentLogoutView.as_view(), name='student_logout'),
]
