from django.urls import path

from .views import *

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Lacrei Saúde",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('profissional', ProfissionalListAPIView.as_view()),
    path('consulta', ConsultaListAPIView.as_view()),
    path('consulta/<int:id_consulta>/', ConsultaDetailAPIView.as_view()),
    path('consulta/profissional/<int:id_profissional>/', ConsultaProfissionalDetailAPIView.as_view()),
    path('contato', ContatoListAPIView.as_view()),
    path('endereco', EnderecoListAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]