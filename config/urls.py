
from django.contrib import admin
from django.urls import path, re_path

from rest_framework.routers import DefaultRouter

from short.views import UrlListViewSet, UrlShortener, UrlExport, UrlView



router = DefaultRouter()
router.register('list', UrlListViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('shortener/(?P<origin_uri>.+)', UrlShortener.as_view()),
    path('export/', UrlExport.as_view()),
    re_path('(<hash>.+)', UrlView.as_view())

]


urlpatterns += router.urls
