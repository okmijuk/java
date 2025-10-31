# Para instalar as bibliotecas necessárias, execute os seguintes comandos no seu terminal:
# pip install googlesearch-python
# pip install requests
# pip install WeasyPrint

import os
import requests
import re
from googlesearch import search
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

def limpar_nome_para_arquivo(nome):
    """
    Limpa o nome para que seja um nome de arquivo válido, removendo caracteres inválidos.
    """
    nome_limpo = re.sub(r'[\\/*?:"<>|]', "", nome)
    nome_limpo = nome_limpo.replace(" ", "_")
    return nome_limpo

def encontrar_e_baixar_perfis_pdf(nomes, pasta_destino):
    """
    Pesquisa por perfis no Escavator, baixa o conteúdo e salva como arquivo PDF.
    """
    try:
        os.makedirs(pasta_destino, exist_ok=True)
        print(f"Pasta de destino '{pasta_destino}' pronta.")
    except OSError as e:
        print(f"Erro ao criar a pasta de destino: {e}")
        return

    font_config = FontConfiguration()
    # Estilo CSS para ajudar na renderização e evitar erros de fontes não encontradas
    css = CSS(string='''
        @page { size: A4; margin: 1cm; }
        body { font-family: sans-serif; }
    ''', font_config=font_config)

    for nome in nomes:
        query = f'"{nome}" site:escavator.com.br'
        print(f"\nBuscando por: '{nome}' no Escavator...")

        try:
            primeiro_resultado = next(search(query, num=1, stop=1, pause=2), None)

            if not primeiro_resultado:
                print(f"  -> Nenhum perfil encontrado para '{nome}'.")
                continue

            print(f"  -> Perfil encontrado: {primeiro_resultado}")
            print(f"  -> Baixando e convertendo para PDF...")

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(primeiro_resultado, headers=headers)

            if response.status_code == 200:
                nome_arquivo = f"{limpar_nome_para_arquivo(nome)}.pdf"
                caminho_completo = os.path.join(pasta_destino, nome_arquivo)

                # Converte o HTML baixado para PDF
                html = HTML(string=response.text, base_url=primeiro_resultado)
                html.write_pdf(caminho_completo, stylesheets=[css], font_config=font_config)

                print(f"  -> Perfil salvo com sucesso em: {caminho_completo}")
            else:
                print(f"  -> Falha ao baixar o perfil. Status code: {response.status_code}")

        except Exception as e:
            print(f"  -> Ocorreu um erro ao processar '{nome}': {e}")

        print("-" * 20)

if __name__ == "__main__":
    pasta_destino_windows = "C:\\Users\\okmij\\Pictures\\FCA - FACULDADE DE\\teste de escavator"

    lista_de_nomes = [
        "Fernando de la Rúa",
        "Luiz Inácio Lula da Silva",
        "Dilma Rousseff",
    ]

    encontrar_e_baixar_perfis_pdf(lista_de_nomes, pasta_destino_windows)
