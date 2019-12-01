from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Medicine, MedicineCategory, Lote


class MedicineCategoryListView(LoginRequiredMixin, ListView):
    model = MedicineCategory
    template_name = 'medicine_category/list.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryListView, self).get_context_data(**kwargs)
        context["medicinePage"] = "active"
        return context


class StockListView(LoginRequiredMixin, ListView):
    model = Lote
    template_name = 'stock/list.html'

    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        context["medicinePage"] = "active"
        return context


class MedicineListView(LoginRequiredMixin, ListView):
    template_name = 'medicine/list.html'
    model = Medicine

    def get_context_data(self, **kwargs):
        context = super(MedicineListView, self).get_context_data(**kwargs)
        context["medicinePage"] = "active"
        return context
