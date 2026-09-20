"""Projeto 1 - Calculadora simples executada pelo terminal.

Para adicionar um novo modo, basta:
  1. criar uma função nova (ex.: def potencia(a, b): ...)
  2. registrar essa função no dicionário OPERACOES logo abaixo.
O menu é montado automaticamente a partir do dicionário.
"""


# ---------- Operações ----------
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None  # divisão por zero
    return a / b


# ---------- Registro das operações (o menu nasce daqui) ----------
# "opção": ("Nome", "símbolo", função)
OPERACOES = {
    "1": ("Soma", "+", somar),
    "2": ("Subtração", "-", subtrair),
    "3": ("Multiplicação", "x", multiplicar),
    "4": ("Divisão", "/", dividir),
}


# ---------- Funções auxiliares ----------
def ler_numero(mensagem):
    """Pede um número até o usuário digitar um valor válido."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Valor inválido. Digite apenas números (ex.: 10 ou 3,5).")


def formatar(numero):
    """Mostra 5 em vez de 5.0, mas mantém 2.5 como 2.5."""
    if float(numero).is_integer():
        return str(int(numero))
    return str(round(numero, 6))


def mostrar_menu():
    print("\nEscolha a operação:")
    for chave, (nome, simbolo, _) in OPERACOES.items():
        print(f"  {chave} - {nome} ({simbolo})")


# ---------- Programa principal ----------
def main():
    print("=" * 32)
    print("     PROJETO 1 - CALCULADORA")
    print("=" * 32)

    nome = input("Qual é o seu nome? ").strip()
    print(f"\nOlá, {nome}! Vamos calcular.\n")

    a = ler_numero("Digite o primeiro número: ")
    b = ler_numero("Digite o segundo número: ")

    mostrar_menu()
    opcao = input("Opção: ").strip()

    if opcao not in OPERACOES:
        print("\nOpção inválida. Encerrando o programa.")
        return

    nome_op, simbolo, funcao = OPERACOES[opcao]
    resultado = funcao(a, b)

    if resultado is None:
        print("\nErro: não é possível dividir por zero.")
    else:
        print(f"\n{formatar(a)} {simbolo} {formatar(b)} = {formatar(resultado)}")
        print(f"({nome_op} realizada com sucesso, {nome}!)")


if __name__ == "__main__":
    main()
