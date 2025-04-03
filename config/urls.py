from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls")),  # dev_1
    path("accounts/", include("accounts.urls")),  # dev_1
    path("cart/", include("cart.urls")),  # dev_1
]

# dev_2
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
