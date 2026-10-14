
import json
import os

ARQUIVO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "banco_dados.json"
)


def carregar_dados():
    """Carrega as pendências salvas no arquivo JSON."""
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados if isinstance(dados, list) else []

    except (json.JSONDecodeError, OSError):
        return []


def salvar_dados(dados):
    """Salva as pendências no arquivo JSON."""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii=False,
                indent=4
            )
        return True

    except OSError as erro:
        print(f"Erro ao salvar os dados: {erro}")
        return False
