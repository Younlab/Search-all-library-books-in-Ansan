from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
                  path('api-token-auth/', obtain_jwt_token),
                  path('admin/', admin.site.urls),
                  path('api/', include('config.api_urls'))
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
