from django.contrib.auth import login
from django.core.paginator import Paginator
from django.shortcuts import redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User

from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = self.object.pictures.all()
        albums = self.object.albums.all()

        context['pictures'] = pictures
        context['albums'] = albums
        print(context)
        return context
