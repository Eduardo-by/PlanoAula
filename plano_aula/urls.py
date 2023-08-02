from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.PlanoAulaListView.as_view(), name='lista_planos_aula'),
    path('adicionar/', views.PlanoAulaCreateView.as_view(),
         name='adicionar_plano_aula'),
    path('update/<int:pk>/', views.PlanoAulaUpdateView.as_view(),
         name='editar_plano_aula'),
    path('detail/<int:pk>/', views.PlanoAulaDetailView.as_view(),
         name='ver_plano_aula'),
    path('gerar_pdf/<int:pk>/', views.gerar_pdf_plano_aula,
         name='gerar_pdf_plano_aula'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
