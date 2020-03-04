from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from patient.models import Patient

from .models import Medicine, MedicineCategory, Lot, Illness, FreeSample
from .forms import MedicineCategoryForm, IllnessForm, MedicineForm, LotForm, FreeSampleForm


class MedicineCategoryListView(LoginRequiredMixin, ListView):
    model = MedicineCategory
    template_name = 'medicine_category/list.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryListView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["categoryPage"] = "active"
        return context


class MedicineCategoryCreateView(LoginRequiredMixin, CreateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'medicine_category/form.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryCreateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["categoryPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('categories')


class MedicineCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'medicine_category/form.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineCategoryUpdateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["categoryPage"] = "active"
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
        context["illnessPage"] = "active"
        return context


class IllnessCreateView(LoginRequiredMixin, CreateView):
    model = Illness
    form_class = IllnessForm
    template_name = 'illness/form.html'

    def get_context_data(self, **kwargs):
        context = super(IllnessCreateView, self).get_context_data(**kwargs)
        context["illnessPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('illnesses')


class IllnessUpdateView(LoginRequiredMixin, UpdateView):
    model = Illness
    form_class = IllnessForm
    template_name = 'illness/form.html'

    def get_context_data(self, **kwargs):
        context = super(IllnessUpdateView, self).get_context_data(**kwargs)
        context["illnessPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('illnesses')


class IllnessDeleteView(LoginRequiredMixin, DeleteView):
    model = Illness

    def get_success_url(self):
        return reverse('illnesses')


class StockListView(LoginRequiredMixin, ListView):
    model = Lot
    template_name = 'stock/list.html'

    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["stockPage"] = "active"
        return context


class StockLotCreateView(LoginRequiredMixin, CreateView):
    model = Lot
    template_name = 'stock/form.html'
    form_class = LotForm

    def get_context_data(self, **kwargs):
        context = super(StockLotCreateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["stockPage"] = "active"
        return context

    def get_success_url(self):
        return reverse('stock')


class StockLotUpdateView(LoginRequiredMixin, UpdateView):
    model = Lot
    template_name = 'stock/form.html'
    form_class = LotForm

    def get_context_data(self, **kwargs):
        context = super(StockLotUpdateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["stockPage"] = "active"
        return context

    def get_initial(self):
        initial = super(StockLotUpdateView, self).get_initial()
        initial = initial.copy()
        lot = Lot.objects.get(pk=self.object.pk)
        initial['entry_date'] = lot.entry_date.strftime('%d-%m-%Y')
        initial['shelf_life_date'] = lot.shelf_life_date.strftime('%d-%m-%Y')
        return initial

    def get_success_url(self):
        return reverse('stock')


class StockLotDeleteView(LoginRequiredMixin, DeleteView):
    model = Lot

    def get_success_url(self):
        return reverse('stock')


class MedicineListView(LoginRequiredMixin, ListView):
    template_name = 'medicine/list.html'
    model = Medicine

    def get_context_data(self, **kwargs):
        context = super(MedicineListView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["medicinePage"] = "active"
        return context


class MedicineCreateView(LoginRequiredMixin, CreateView):
    template_name = 'medicine/form.html'
    model = Medicine
    form_class = MedicineForm

    def get_parameters(self):
        return {
            'medicine_name': self.request.GET.get('medicine_name'),
            'next': self.request.GET.get('next')
        }

    def get_context_data(self, **kwargs):
        context = super(MedicineCreateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["medicinePage"] = "active"
        return context

    def get_initial(self):
        initial = super(MedicineCreateView, self).get_initial()
        initial = initial.copy()
        medicine_name = self.get_parameters()['medicine_name']
        if medicine_name:
            initial['name'] = medicine_name
        return initial

    def get_success_url(self):
        next = self.get_parameters()['next']
        if next:
            return "{}?medicine={}".format(next, self.object.id)
        return reverse('medicines')


class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'medicine/form.html'
    model = Medicine
    form_class = MedicineForm

    def get_context_data(self, **kwargs):
        context = super(MedicineUpdateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["medicinePage"] = "active"
        return context

    def get_success_url(self):
        return reverse('medicines')


class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine

    def get_success_url(self):
        return reverse('medicines')


class MedicineDetailView(LoginRequiredMixin, DetailView):
    model = Medicine
    template_name = 'medicine/detail.html'

    def get_context_data(self, **kwargs):
        context = super(MedicineDetailView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["medicinePage"] = "active"
        return context


class FreeSampleListView(LoginRequiredMixin, ListView):
    model = FreeSample
    template_name = 'free_sample/list.html'

    def get_context_data(self, **kwargs):
        context = super(FreeSampleListView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["freeSamplePage"] = "active"
        return context


class FreeSampleCreateView(LoginRequiredMixin, CreateView):
    model = FreeSample
    form_class = FreeSampleForm
    template_name = 'free_sample/form.html'

    def get_parameters(self):
        return {
            'patient': self.request.GET.get('patient'),
            'medicine': self.request.GET.get('medicine')
        }

    def get_context_data(self, **kwargs):
        context = super(FreeSampleCreateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["freeSamplePage"] = "active"
        patient_id = self.get_parameters()['patient']
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            context["patient"] = patient
        medicine_id = self.get_parameters()['medicine']
        if medicine_id:
            medicine = Medicine.objects.get(id=medicine_id)
            context['medicine'] = medicine
        return context

    def get_success_url(self):
        return reverse('freesample_list')


class FreeSampleUpdateView(LoginRequiredMixin, UpdateView):
    model = FreeSample
    form_class = FreeSampleForm
    template_name = 'free_sample/form.html'

    def get_context_data(self, **kwargs):
        context = super(FreeSampleUpdateView, self).get_context_data(**kwargs)
        context["pharmacyMenu"] = "active"
        context["freeSamplePage"] = "active"
        return context

    def get_success_url(self):
        return reverse('freesample_list')


class FreeSampleDeleteView(LoginRequiredMixin, DeleteView):
    model = FreeSample

    def get_success_url(self):
        return reverse('freesample_list')
