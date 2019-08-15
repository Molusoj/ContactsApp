from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .models import Contact
from django.contrib.auth.models import User

# Create your views here.


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact/home.html'
    context_object_name = 'contacts'
    ordering = ['name']

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)  # Acess the filter contacts according to manager


def cover(request):
    return render(request, 'contact/cover.html')


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'contact/contact_detail.html'


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'phone_number', 'email', 'gender']

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['image', 'name', 'phone_number', 'email', 'gender']

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.manager:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):  # Required For UserPassesTestMixin
        contact = self.get_object()

        if self.request.user == contact.manager:
            return True
        return False
