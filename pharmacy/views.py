from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Medicine, MedicineCategory, Lote, Illness
from .forms import MedicineCategoryForm, IllnessForm


class MedicineCategoryListView(LoginRequiredMixin, ListView):
    model = MedicineCategory
    template_name = 'medicine_category/list.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryListView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context


class MedicineCategoryCreateView(LoginRequiredMixin, CreateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'medicine_category/form.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryCreateView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('categories')


class MedicineCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'medicine_category/form.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryUpdateView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('categories')


class MedicineCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = MedicineCategory

    def get_success_url(self):
        return reverse('categories')


class IllnessListView(LoginRequiredMixin, ListView):
    model = Illness
    template_name = 'illness/list.html'

    def get_context_data(self, **kwargs):
        context = super(IllnessListView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context


class IllnessCreateView(LoginRequiredMixin, CreateView):
    model = Illness
    form_class = IllnessForm
    template_name = 'illness/form.html'

    def get_context_data(self, **kwargs):
        context = super(IllnessCreateView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('illnesses')


class IllnessUpdateView(LoginRequiredMixin, UpdateView):
    model = Illness
    form_class = IllnessForm
    template_name = 'illness/form.html'

    def get_context_data(self, **kwargs):
        context = super(IllnessUpdateView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('illnesses')


class IllnessDeleteView(LoginRequiredMixin, DeleteView):
    model = Illness

    def get_success_url(self):
        return reverse('illnesses')


class StockListView(LoginRequiredMixin, ListView):
    model = Lote
    template_name = 'stock/list.html'

    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context


class MedicineListView(LoginRequiredMixin, ListView):
    template_name = 'medicine/list.html'
    model = Medicine

    def get_context_data(self, **kwargs):
        context = super(MedicineListView, self).get_context_data(**kwargs)
        context["pharmacyPage"] = "active"
        return context
