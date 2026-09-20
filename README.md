# calculadora1.0
Calculadora em Python para o terminal Linux 
🧮 Projeto 1 — Calculadora de Terminal

Uma calculadora feita em Python que conversa com você direto no terminal Linux.

💡 A ideia

Este é o meu primeiro projeto prático de programação, feito para treinar Python e a rotina do terminal Linux (o que também faz parte do curso de Analista de Dados da EBAC).

Em vez de só "fazer conta", quis que o programa tivesse uma pequena interação: ele pergunta o seu nome, pede dois números e deixa você escolher a operação em um menu. Um script Bash cuida de abrir tudo com um único comando.

✨ O que ela faz
➕ Soma, ➖ subtração, ✖️ multiplicação e ➗ divisão
Cumprimenta o usuário pelo nome
Aceita vírgula ou ponto nos decimais (3,5 ou 3.5)
Pede o número de novo se você digitar algo inválido, sem travar
Avisa quando você tenta dividir por zero
Mostra 12 / 4 = 3 em vez de 3.0, para o resultado ficar limpo
🖥️ Exemplo de uso
================================
     PROJETO 1 - CALCULADORA
================================
Qual é o seu nome? Ana

Olá, Ana! Vamos calcular.

Digite o primeiro número: 12
Digite o segundo número: 4

Escolha a operação:
  1 - Soma (+)
  2 - Subtração (-)
  3 - Multiplicação (x)
  4 - Divisão (/)
Opção: 4

12 / 4 = 3
(Divisão realizada com sucesso, Ana!)
🧰 Ferramentas
Ferramenta	Para que serviu
Python 3	Lógica da calculadora
Shell Script (Bash)	Atalho para executar o programa
Linux / Ubuntu	Ambiente onde tudo roda
Git e GitHub	Controle de versão e publicação
Google Colab	Testes e experimentos iniciais
🚀 Como rodar
bash
git clone <URL-DO-REPOSITORIO>
cd projeto_1

# opção 1: pelo script Bash
bash calculadora/executar.sh

# opção 2: direto pelo Python
python3 calculadora/calculadora.py
🧩 Como adicionar um novo modo

Cada operação é uma função registrada no dicionário OPERACOES, e o menu é montado sozinho a partir dele. Para criar, por exemplo, a potência:

python
def potencia(a, b):
    return a ** b

OPERACOES["5"] = ("Potência", "^", potencia)
👤 Autor
Feito por<muryllo>
