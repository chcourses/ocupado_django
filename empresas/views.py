from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
from .models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = '__all__'


class EmpresaListView(ListView):
    model = Empresa
    context_object_name = 'empresas'
    ordering = ['lote']

    def get_queryset(self):
        queryset = Empresa.objects.all()
        field = self.request.GET.get('orderBy')
        sorting = self.request.GET.get('sort')
        if field and sorting == 'asc':
            queryset = queryset.order_by(self.request.GET.get('orderBy'))
        if field and sorting == 'desc':
            queryset = queryset.order_by(
                self.request.GET.get('orderBy')).reverse()
        return queryset


class EmpresaDetailView(DetailView):
    model = Empresa


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = '__all__'


class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('emp-list')
