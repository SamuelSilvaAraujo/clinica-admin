from django.urls import path, include

from .views import *

urlpatterns = [

    path('', SpirometryListView.as_view(), name="spirometry_list"),
    path('espirometria/', include([
        path('cadastro/', SpirometryCreateView.as_view(), name="spirometry_create"),
        path('<int:pk>/', include([
            path('atualizar/', SpirometryUpdateView.as_view(), name="spirometry_update"),
            path('delete/', SpirometryDeleteView.as_view(), name="spirometry_delete"),
        ]))
    ])),

    path('materiais/', MaterialListView.as_view(), name="material_list"),
    path('material/', include([
        path('cadastro/', MaterialCreateView.as_view(), name="material_create"),
        path('<int:pk>/', include([
            path('atualizar/', MaterialUpdateView.as_view(), name="material_update"),
            path('excluir/', MaterialDeleteView.as_view(), name="material_delete"),
        ])),
    ])),


    path('estoque/', include([
        path('', MaterialStockListView.as_view(), name="material_stock_list"),
        path('cadastro/', MaterialStockCreateView.as_view(), name="material_stock_create"),
        path('<int:pk>/', include([
            path('atualizar/', MaterialStockUpdateView.as_view(), name="material_stock_update"),
            path('delete/', MaterialStockDeleteView.as_view(), name="material_stock_delete"),
        ]))
    ]))
]
