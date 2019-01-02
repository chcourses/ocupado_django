from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ProfileForm, ProfileEmailForm
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from empresas.models import Empresa
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/home.html', {'user': request.user})
    else:
        return redirect('login')


@method_decorator(login_required, name='dispatch')
class ProfileView(SuccessMessageMixin, UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = "accounts/profile_form.html"
    success_message = "Perfil salvo com sucesso!"

    def get_object(self):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
        return profile


class UserListView(DetailView):
    model = User
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context["fields"] = User._meta.get_fields()
        return context


class UsersListView(ListView):
    model = User
    template_name = 'accounts/profile_list.html'
    context_object_name = 'usuarios'
    ordering = ['first_name', 'last_name']
    paginate_by = 12

    def get_queryset(self):
        name = self.request.GET.get('name', '')
        empresa = self.request.GET.get('empresa', '')
        queryset = User.objects.filter(
            first_name__icontains=name) | User.objects.filter(last_name__icontains=name)
        if empresa != '':
            profiles = User.objects.filter(
                profile__empresas__nome__exact=empresa)
            return queryset.intersection(profiles)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        empresas = Empresa.objects.all()
        context['empresas'] = empresas
        name = self.request.GET.get('name', '')
        context['name'] = name
        selEmpresa = self.request.GET.get('empresa', '')
        context['selEmpresa'] = selEmpresa
        return context


@method_decorator(login_required, name='dispatch')
class ProfileEmailUpdate(UpdateView):
    form_class = ProfileEmailForm
    success_url = reverse_lazy('profile')
    template_name = "accounts/profile_email_form.html"
    success_message = "E-mail alterado com sucesso!"

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Novo e-mail'})
        return form
