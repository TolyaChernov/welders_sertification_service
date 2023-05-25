import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ptm import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("user/", include("users.urls")),
]


if settings.DEBUG:
    # import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
