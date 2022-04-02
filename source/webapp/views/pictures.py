from uuid import uuid4

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy, resolve
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PictureForm
from webapp.models import Picture


class IndexView(ListView):
    model = Picture
    context_object_name = 'pictures'
    template_name = 'pictures/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_at")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class PictureView(LoginRequiredMixin, DetailView):
    template_name = "pictures/view.html"
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PictureCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'pictures/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:picture-view', kwargs={'pk': self.object.pk})


class PictureUpdateView(PermissionRequiredMixin, UpdateView):
    model = Picture
    form_class = PictureForm
    template_name = 'pictures/update.html'
    permission_required = 'webapp.change_picture'

    def get_success_url(self):
        return reverse('webapp:picture-view', kwargs={'pk': self.object.pk})


class PictureDeleteView(PermissionRequiredMixin, DeleteView):
    model = Picture
    template_name = 'pictures/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_picture'


class LinkGenerationView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        current_url = self.request.path
        TOKEN = str(uuid4().hex)
        full_url = current_url + TOKEN
        context = JsonResponse(
            {"full_url": full_url}
        )
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url
