from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Medicine


class MedicineListView(LoginRequiredMixin, ListView):
    template_name = 'medicine/list.html'
    model = Medicine

    def get_context_data(self, **kwargs):
        context = super(MedicineListView, self).get_context_data(**kwargs)
        context["medicinePage"] = "active"
        return context
