from django.urls import path
from django.shortcuts import render, redirect
from produtos.forms import ProdutoForm

def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def create_product(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')  # Redireciona para a página principal após o cadastro
    else:
        form = ProdutoForm()

    return render(request, 'create_product.html', {'form': form})