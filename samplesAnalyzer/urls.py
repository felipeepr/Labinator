from django.urls import path

from . import views

app_name = "samplesAnalyzer"
urlpatterns = [
    path("", views.index, name="index"),
    path("samples/create/", views.samples_create, name="samples_create"),
    path("samples/<int:sample_id>/edit/", views.samples_edit, name="samples_edit"),
    path("samples/<int:sample_id>/delete/", views.samples_delete, name="samples_delete"),
    path("sample_detail/<str:sample_name>", views.detail, name="detail"),
    path("<int:sample_id>/tested/", views.tested, name="tested"),
    path("sample_results/<int:sample_id>/results/<str:result>/", views.results, name="results"),
    path("results/finalResults", views.finalResults, name="finalResults"),
]