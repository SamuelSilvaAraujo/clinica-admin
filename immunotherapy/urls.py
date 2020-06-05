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

    path('<int:immunotherapy_id>/adiconar/frasco/', BottleCreateView.as_view(), name='bottle_create'),
    path('<int:immunotherapy_id>/finalizar/frasco/<int:pk>/', BottleFinalizeView.as_view(), name='bottle_finalize'),
    path('<int:immunotherapy_id>/adiconar/aplicacao/', ApplicationCreateView.as_view(), name='application_create'),

]
