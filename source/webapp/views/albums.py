from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumDetailView(DetailView):
    template_name = 'albums/view.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = self.object.pictures.all()
        context['pictures'] = pictures
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/create.html'

    def get_success_url(self):
        return reverse('webapp:album-view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/update.html'
    permission_required = 'webapp.change_album'

    def get_success_url(self):
        return reverse('webapp:album-view', kwargs={'pk': self.object.pk})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_album'
