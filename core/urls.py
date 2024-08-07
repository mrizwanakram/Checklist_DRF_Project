from django.urls import path
from .views import CheckListApiView, CheckListAPIView, CheckListItemCreateAPIView, CheckListItemAPIView
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api/checklists/', CheckListApiView.as_view(), name='checklist-list'),
    path('api/checklists/<int:pk>/', CheckListAPIView.as_view(), name='checklist-detail'),
    path('api/checklistItems/create/', CheckListItemCreateAPIView.as_view(), name='checklistItems-detail'),
    path('api/checklistItems/<int:pk>/', CheckListItemAPIView.as_view(), name='checklistItems-detail'),
 
    path(
        "openapi",
        get_schema_view(
            title="CheckList", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),

    path(
        "",
        TemplateView.as_view(
            template_name="doc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="api_doc",
    ),
]
