# Para instalar a biblioteca necessária, execute o seguinte comando no seu terminal:
# pip install googlesearch-python

from googlesearch import search

def encontrar_perfis_escavator(nomes):
    """
    Pesquisa por perfis no Escavator para uma lista de nomes e imprime a URL do primeiro resultado.
    """
    for nome in nomes:
        query = f'"{nome}" site:escavator.com.br'
        print(f"Buscando por: '{nome}' no Escavator...")
        try:
            # A pesquisa retorna um gerador, pegamos o primeiro resultado
            primeiro_resultado = next(search(query, num=1, stop=1, pause=2), None)
            if primeiro_resultado:
                print(f"  -> Perfil encontrado: {primeiro_resultado}")
            else:
                print(f"  -> Nenhum perfil encontrado para '{nome}'.")
        except Exception as e:
            print(f"  -> Ocorreu um erro ao buscar por '{nome}': {e}")
        print("-" * 20)

if __name__ == "__main__":
    # Lista de nomes para buscar
    lista_de_nomes = [
        "Fernando de la Rúa",
        "Luiz Inácio Lula da Silva",
        "Dilma Rousseff",
        # Adicione mais nomes aqui conforme necessário
    ]

    encontrar_perfis_escavator(lista_de_nomes)
