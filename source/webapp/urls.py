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

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('picture/<int:pk>/', PictureView.as_view(), name='picture-view'),
    path('picture/create/', PictureCreateView.as_view(), name='picture-create'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(), name='picture-update'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='picture-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
