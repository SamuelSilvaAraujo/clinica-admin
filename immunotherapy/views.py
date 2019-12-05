from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Immunotherapy
from .forms import ImmunotherapyForm


class ImmunotherapyListView(LoginRequiredMixin, ListView):
    model = Immunotherapy
    template_name = 'immunotherapy/list.html'

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyListView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context


class ImmunotherapyCreateView(LoginRequiredMixin, CreateView):
    model = Immunotherapy
    template_name = 'immunotherapy/form.html'
    form_class = ImmunotherapyForm

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyCreateView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context

    def form_valid(self, form):
        form.instance.status = Immunotherapy.IN_PROGRESS
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('immunotherapy')


class ImmunotherapyUpdateView(LoginRequiredMixin, UpdateView):
    model = Immunotherapy
    template_name = 'immunotherapy/form.html'
    form_class = ImmunotherapyForm

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyUpdateView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('immunotherapy')


class ImmunotherapyDeleteView(LoginRequiredMixin, DeleteView):
    model = Immunotherapy

    def get_success_url(self):
        return reverse('immunotherapy')
