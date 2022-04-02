from django.conf.urls.static import static
from django.urls import path

from exam9_project import settings
from webapp.views.pictures import (
    IndexView,
    PictureView,
    PictureCreateView,
    PictureUpdateView,
    PictureDeleteView
)

from webapp.views.albums import (
    AlbumDetailView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('picture/<int:pk>/', PictureView.as_view(), name='picture-view'),
    path('picture/create/', PictureCreateView.as_view(), name='picture-create'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(), name='picture-update'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='picture-delete'),

    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album-view'),
    path('album/create/', AlbumCreateView.as_view(), name='album-create'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
