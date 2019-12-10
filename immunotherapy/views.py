from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Immunotherapy, Bottle
from .forms import ImmunotherapyForm, BottleForm


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


class ImmunotherapyDetailView(LoginRequiredMixin, DetailView):
    model = Immunotherapy
    template_name = 'immunotherapy/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ImmunotherapyDetailView, self).get_context_data(**kwargs)
        context["immunotherapyPage"] = "active"
        return context


class BottleCreateView(LoginRequiredMixin, CreateView):
    model = Bottle
    template_name = 'bottle/form-modal.html'
    form_class = BottleForm

    def get_immunotherapy(self):
        immunotherapy_id = self.kwargs['immunotherapy_id']
        immunotherapy = Immunotherapy.objects.get(id=immunotherapy_id)
        return immunotherapy

    def get_context_data(self, **kwargs):
        context = super(BottleCreateView, self).get_context_data(**kwargs)
        context["immunotherapy"] = self.get_immunotherapy()
        return context

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(BottleCreateView, self).get_form_kwargs()
        form_kwargs["immunotherapy"] = self.get_immunotherapy()
        return form_kwargs

    def form_valid(self, form):
        form.instance.immunotherapy = self.get_immunotherapy()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('immunotherapy_detail', kwargs={'pk': self.kwargs['immunotherapy_id']})
