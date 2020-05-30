from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.files.storage import FileSystemStorage
import base64

from .models import Pessoas
# Create your views here.

class proprio_usuarioMixin(object):
	model = Pessoas
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id = id)
		return obj



class Pessoa_loginView(proprio_usuarioMixin, View):
	template_name = "login.html"
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		logado = request.COOKIES.get
		print(request.session)
		#x = base64.b64decode(request.session[logado])
		
		print(logado)
		if logado in request.session:
			#decodificar id para localizar no banco de dados
			return redirect("../pessoas/1")
		else:
			return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		
		context = {}
		obj = self.get_object()



class Proprio_usuarioView(proprio_usuarioMixin, View):
	template_name = "detalhe_das_pessoas.html"
	def get(self, request, id=None, *args, **kwargs):

		context = {'object' : self.get_object()}
		return render(request, self.template_name, context)		

class proprio_usuarioDeleteView(proprio_usuarioMixin, View):
	template_name = "detalhe_das_pessoas_delete.html"
	def get(self, request, id=None, *args, **kwargs):
		context ={}
		obj = self.obj.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			#return redirect('') em construção
		return render(request, self.template_name, context)

class Create_pessoaView(proprio_usuarioMixin, View):
	template_name = "criar_pessoas.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		nome = request.POST.get('nome')
		apelidio = request.POST.get('apelidio')
		uploaded_file = request.FILES['foto']
		#print(uploaded_file.name)
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		Pessoas.objects.create(nome=nome,apelidio=apelidio,foto=name)
		#uploaded_file = request.FILES['document']
		#fs = FileSystemStorage()
		#fs.save(uploaded_file.name, uploaded_file)


		return redirect('../pessoas')

class Delete_pessoaView(proprio_usuarioMixin, View):
	template_name = "deletar_pessoas.html"

	def get(self, request, id=None, *args, **kwargs):
		context= {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):

		context= {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			return redirect("../pessoas/login")# falta o redirect

		return render(request, self.template_name, context)
	