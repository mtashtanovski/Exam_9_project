from django.conf.urls.static import static
from django.urls import path

from exam9_project import settings
from webapp.views.pictures import (
    IndexView,
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
