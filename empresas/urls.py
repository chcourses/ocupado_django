from django.urls import path

from .views import EmpresaCreateView, EmpresaListView, EmpresaDeleteView, EmpresaDetailView, \
    EmpresaUpdateView

urlpatterns = [
    path('create/', EmpresaCreateView.as_view(), name='emp-create'),
    path('', EmpresaListView.as_view(), name='emp-list'),
    path('detail/<int:pk>/', EmpresaDetailView.as_view(), name='emp-detail'),
    path('update/<int:pk>/', EmpresaUpdateView.as_view(), name='emp-update'),
    path('delete/<int:pk>/', EmpresaDeleteView.as_view(), name='emp-delete'),
]
