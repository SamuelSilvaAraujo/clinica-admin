from django.urls import path, include

from .views import *

urlpatterns = [

    path('', ImmunotherapyListView.as_view(), name='immunotherapy'),
    path('criar/', ImmunotherapyCreateView.as_view(), name='immunotherapy_create'),
    path('<int:pk>/', include([
        path('editar/', ImmunotherapyUpdateView.as_view(), name='immunotherapy_update'),
        path('excluir/', ImmunotherapyDeleteView.as_view(), name='immunotherapy_delete'),
        path('detalhe/', ImmunotherapyDetailView.as_view(), name='immunotherapy_detail'),
        path('finalizar/', ImmunotherapyFinisheView.as_view(), name='immunotherapy_finishe'),
    ])),

    path('<int:immunotherapy_id>/', include([
        path('adiconar/aplicacao/', ApplicationCreateView.as_view(), name='application_create'),
        path('editar/aplicacao/<int:pk>/', ApplicationUpdateView.as_view(), name='application_update'),
        path('delete/aplicacao/<int:pk>/', ApplicationDeleteView.as_view(), name='application_delete')
    ])),

    path('<int:immunotherapy_id>/imprimir/etiqueta/', OpenTagModal.as_view(), name='tag_pdf'),
    path('criar/etiqueta/', create_pdf_tag, name="create_pdf_tag"),

]
