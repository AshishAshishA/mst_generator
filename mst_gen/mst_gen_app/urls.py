from django.urls import path
from .views import my_graph_view,graph_with_mst

urlpatterns=[
    # path('2',my_graph_view,name="my_graph_view"),
    path('',graph_with_mst,name="graph_with_mst"),
]