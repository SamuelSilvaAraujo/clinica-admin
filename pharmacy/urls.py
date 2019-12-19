from django.urls import path, include

from .views import *

urlpatterns = [
    path('remedios/', MedicineListView.as_view(), name='medicines'),
    path('remedio/', include([
        path('criar/', MedicineCreateView.as_view(), name='medicine_create'),
        path('<int:pk>/', include([
            path('', MedicineDetailView.as_view(), name='medicine_detail'),
            path('editar/', MedicineUpdateView.as_view(), name='medicine_update'),
            path('excluir/', MedicineDeleteView.as_view(), name='medicine_delete'),
        ])),

        path('categorias/', MedicineCategoryListView.as_view(), name='categories'),
        path('categoria/', include([
            path('criar/', MedicineCategoryCreateView.as_view(), name='category_create'),
            path('<int:pk>/', include([
                path('editar/', MedicineCategoryUpdateView.as_view(), name='category_update'),
                path('excluir/', MedicineCategoryDeleteView.as_view(), name='category_delete'),
            ]))
        ])),

        path('estoque/', include([
            path('', StockListView.as_view(), name='stock'),
            path('lote/', include([
                path('adcionar/', StockLotCreateView.as_view(), name='lot_create'),
                path('<int:pk>/', include([
                    path('editar/', StockLotUpdateView.as_view(), name='lot_update'),
                    path('excluir/', StockLotDeleteView.as_view(), name='lot_delete'),
                ])),
            ])),
        ])),
    ])),

    path('doencas/', IllnessListView.as_view(), name='illnesses'),
    path('doenca/criar/', IllnessCreateView.as_view(), name='illness_create'),
    path('doenca/editar/<int:pk>/', IllnessUpdateView.as_view(), name='illness_update'),
    path('doenca/excluir/<int:pk>/', IllnessDeleteView.as_view(), name='illness_delete'),
]
