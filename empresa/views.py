from django.shortcuts import render
from .form import DadosForm
def template_cad (request):

    data={}
    data['form']=DadosForm()
    data['link_form']="{% url 'accounts:index'%}"
    data['nome']='Voltar'
    data['titulo']='Cadastro Empresa'
    return render(request,'../../empresa/templates/cad_em.html',data)
# Create your views here.
