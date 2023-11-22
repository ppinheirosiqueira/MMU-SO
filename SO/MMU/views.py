from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, "MMU/home.html", {})

def process_json(request):
    if request.method == 'POST' and request.FILES.get('json_file'):
        json_file = request.FILES['json_file']
        
        # Faça o que quiser com o arquivo JSON. Aqui, apenas retornamos os dados para a página.
        data = {'status': 'success', 'message': 'Arquivo JSON recebido com sucesso.'}
        return JsonResponse(data)
    else:
        data = {'status': 'error', 'message': 'Erro ao processar o arquivo JSON.'}
        return JsonResponse(data)
