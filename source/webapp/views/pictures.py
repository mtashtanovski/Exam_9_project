from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from webapp.models import Picture


class IndexView(ListView):
    model = Picture
    context_object_name = 'pictures'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_at")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context
