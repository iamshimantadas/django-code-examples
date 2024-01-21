from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.generators import SchemaGenerator

class CustomSchemaGenerator(SchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema["info"]["title"] = "Your Custom Title"
        return schema