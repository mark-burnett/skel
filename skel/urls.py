from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
import importlib

APP_URLS = importlib.import_module('%s.urls' % settings.SKEL_APP_MODULE)

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static_views.serve),
] + APP_URLS.urlpatterns
