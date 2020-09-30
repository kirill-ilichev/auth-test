
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from snippets.api.viewsets import SnippetViewSet

router = routers.DefaultRouter()
router.register('snippets', SnippetViewSet)

urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
