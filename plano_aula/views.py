import pdfkit
from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import PlanoAulaForm
from .models import PlanoAula

config = pdfkit.configuration(
    wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


class PlanoAulaListView(ListView):
    model = PlanoAula
    template_name = "plano_de_aula/index.html"
    context_object_name = 'planos_aula'


class PlanoAulaDetailView(DetailView):
    model = PlanoAula
    template_name = "plano_de_aula/detail.html"
    context_object_name = 'plano_aula'


class PlanoAulaCreateView(CreateView):
    model = PlanoAula
    template_name = "plano_de_aula/create.html"
    form_class = PlanoAulaForm
    success_url = reverse_lazy('lista_planos_aula')


class PlanoAulaUpdateView(UpdateView):
    model = PlanoAula
    template_name = 'plano_de_aula/update.html'
    form_class = PlanoAulaForm
    success_url = reverse_lazy('lista_planos_aula')
    context_object_name = 'plano_aula'


def gerar_pdf_plano_aula(request, pk):
    plano_aula = get_object_or_404(PlanoAula, pk=pk)

    template = 'plano_de_aula/detail.html'
    context = {
        'debug': settings.DEBUG,
        'plano_aula': plano_aula,
        'is_pdf': True,  # Variável para indicar que é PDF
    }
    css_file_path ='static/css/style.css'
    html_string = render_to_string(template, context)

    try:
        options = {
            'enable-local-file-access': None,
            'no-outline': True,
            'encoding': 'UTF-8',
            'user-style-sheet': css_file_path,
        }
        pdf_file = pdfkit.from_string(html_string, False, options=options,configuration=config)
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="plano_aula_{}.pdf"'.format(
            plano_aula.titulo)
        return response
    except Exception as e:
        return HttpResponseServerError('Erro ao gerar PDF: {}'.format(e))
