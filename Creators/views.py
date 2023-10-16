from django.http import FileResponse
import os

caminho_absoluto = 'C:\\Users\\IFMA\\GIT\\Django-React\\templates\\CreatorsStatic\\meia_talha.jpg'

def index(request):
    # Abra o arquivo de imagem em modo de leitura binária
    with open(caminho_absoluto, 'rb') as image_file:
        # Crie uma resposta de arquivo para a imagem
        response = FileResponse(image_file)

    return response
