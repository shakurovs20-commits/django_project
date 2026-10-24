from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

handler404 = 'core.views.page_not_found'
from api.urls import router

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('api/', include(router.urls)),
    path('api/api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
