from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Material, Stock, Spirometry
from .forms import MaterialForm, MaterialStockForm, SpirometryForm


class MaterialListView(LoginRequiredMixin, ListView):
    template_name = 'material/list.html'
    model = Material

    def get_context_data(self, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)
        context["materialPage"] = "active"
        context["spirometryMenu"] = "active"
        return context


class MaterialCreateView(LoginRequiredMixin, CreateView):
    template_name = "material/form.html"
    model = Material
    form_class = MaterialForm

    def get_context_data(self, **kwargs):
        context = super(MaterialCreateView, self).get_context_data(**kwargs)
        context["materialPage"] = "active"
        context["spirometryMenu"] = "active"
        return context

    def get_success_url(self):
        return reverse('material_list')


class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "material/form.html"
    model = Material
    form_class = MaterialForm

    def get_context_data(self, **kwargs):
        context = super(MaterialUpdateView, self).get_context_data(**kwargs)
        context["materialPage"] = "active"
        context["spirometryMenu"] = "active"
        return context

    def get_success_url(self):
        return reverse('material_list')


class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material

    def get_success_url(self):
        return reverse('material_list')


class MaterialStockListView(LoginRequiredMixin, ListView):
    template_name = 'material_stock/list.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super(MaterialStockListView, self).get_context_data(**kwargs)
        context["stockPage"] = "active"
        context["spirometryMenu"] = "active"
        return context


class MaterialStockCreateView(LoginRequiredMixin, CreateView):
    template_name = "material_stock/form.html"
    model = Stock
    form_class = MaterialStockForm

    def get_context_data(self, **kwargs):
        context = super(MaterialStockCreateView, self).get_context_data(**kwargs)
        context["stockPage"] = "active"
        context["spirometryMenu"] = "active"
        return context

    def get_success_url(self):
        return reverse('material_stock_list')


class MaterialStockUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "material_stock/form.html"
    model = Stock
    form_class = MaterialStockForm

    def get_context_data(self, **kwargs):
        context = super(MaterialStockUpdateView, self).get_context_data(**kwargs)
        context["stockPage"] = "active"
        context["spirometryMenu"] = "active"
        return context

    def get_success_url(self):
        return reverse('material_stock_list')


class MaterialStockDeleteView(LoginRequiredMixin, DeleteView):
    model = Stock

    def get_success_url(self):
        return reverse('material_stock_list')


class SpirometryListView(LoginRequiredMixin, ListView):
    template_name = "spirometry/list.html"
    model = Spirometry

    def get_context_data(self, **kwargs):
        context = super(SpirometryListView, self).get_context_data(**kwargs)
        context["spirometryPage"] = "active"
        context["spirometryMenu"] = "active"
        return context


class SpirometryCreateView(LoginRequiredMixin, CreateView):
    template_name = "spirometry/form.html"
    model = Spirometry
    form_class = SpirometryForm

    def get_context_data(self, **kwargs):
        context = super(SpirometryCreateView, self).get_context_data(**kwargs)
        context["spirometryPage"] = "active"
        context["spirometryMenu"] = "active"
        return context

    def get_success_url(self):
        return reverse('spirometry_list')


class SpirometryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "spirometry/form.html"
    model = Spirometry
    form_class = SpirometryForm

    def get_context_data(self, **kwargs):
        context = super(SpirometryUpdateView, self).get_context_data(**kwargs)
        context["spirometryPage"] = "active"
        context["spirometryMenu"] = "active"
        return context

    def get_success_url(self):
        return reverse('spirometry_list')


class SpirometryDeleteView(LoginRequiredMixin, DeleteView):
    model = Spirometry

    def get_success_url(self):
        return reverse('spirometry_list')
