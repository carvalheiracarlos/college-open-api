from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


schema_view = get_schema_view(
    openapi.Info(
        title='IMD College Open API',
        default_version='1.0',
        description='IMD College Open API',
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    #path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path("academic/", include("CollegeOpen.Academic.urls", namespace="Academic")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('disciplines/', include("CollegeOpen.Disciplines.urls", namespace="Disciplines")),
    ### API SWAGGER ###
    path(
        'swagger.<format>',  # format is json or yaml
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
