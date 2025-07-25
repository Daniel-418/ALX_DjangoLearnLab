from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

# Create your views here.
def list_books(request):
    books = {"books" : Book.objects.all()}
    x = "UserCreationForm()"

    return render(request, "relationship_app/list_books.html", books)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

