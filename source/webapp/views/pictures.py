from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
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


class PictureView(DetailView):
    template_name = "pictures/view.html"
    model = Picture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PictureCreateView(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'pictures/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:picture-view', kwargs={'pk': self.object.pk})


class PictureUpdateView(UpdateView):
    model = Picture
    form_class = PictureForm
    template_name = 'pictures/update.html'

    def get_success_url(self):
        return reverse('webapp:picture-view', kwargs={'pk': self.object.pk})


class PictureDeleteView(DeleteView):
    model = Picture
    template_name = 'pictures/delete.html'
    success_url = reverse_lazy('webapp:index')
