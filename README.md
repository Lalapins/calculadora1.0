# 🧮 Projeto 1 — Calculadora de Terminal

> Uma calculadora feita em Python que conversa com você direto no terminal Linux.

## 💡 A ideia

Este é o meu primeiro projeto prático de programação, feito para treinar Python e a rotina do terminal Linux (o que também faz parte do curso de Analista de Dados da EBAC).

Em vez de só "fazer conta", quis que o programa tivesse uma pequena interação: ele pergunta o seu nome, pede dois números e deixa você escolher a operação em um menu. Um script Bash cuida de abrir tudo com um único comando.

## ✨ O que ela faz

- ➕ Soma, ➖ subtração, ✖️ multiplicação e ➗ divisão
- Cumprimenta o usuário pelo nome
- Aceita vírgula ou ponto nos decimais (`3,5` ou `3.5`)
- Pede o número de novo se você digitar algo inválido, sem travar
- Avisa quando você tenta dividir por zero
- Mostra `12 / 4 = 3` em vez de `3.0`, para o resultado ficar limpo

## 🖥️ Exemplo de uso

```
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
```

## 🧰 Ferramentas

| Ferramenta | Para que serviu |
|---|---|
| Python 3 | Lógica da calculadora |
| Shell Script (Bash) | Atalho para executar o programa |
| Linux / Ubuntu | Ambiente onde tudo roda |
| Git e GitHub | Controle de versão e publicação |
| Google Colab | Testes e experimentos iniciais |

## 🚀 Como rodar (resumo)
> ⚠️ Se o Windows bloquear o `executar.bat` (aviso do "Controle de Aplicativo Inteligente"), abra um terminal na pasta do projeto e rode: `python calculadora\calculadora.py`
> 
Você precisa ter o **Python 3** instalado (confira com `python3 --version`).

- **Linux:** `bash calculadora/executar.sh` (detalhes na próxima seção)
- **Windows:** dê duplo clique no `executar.bat`
- **Direto pelo Python:** `python3 calculadora/calculadora.py`

Para baixar o projeto, clone pelo Git ou use o botão verde **Code → Download ZIP** (e extraia o ZIP antes de rodar):

```bash
git clone https://github.com/<seu-usuario>/calculadora1.0.git
cd calculadora1.0
```

## 📜 Como executar o arquivo `.sh`

O arquivo `calculadora/executar.sh` é um **script Shell (Bash)**. Ele existe para você abrir a calculadora com um único comando, de qualquer pasta, sem precisar lembrar onde o código Python está.

### O que tem dentro do script

```bash
#!/bin/bash
cd "$(dirname "$0")" || exit 1
python3 calculadora.py
```

| Linha | O que faz |
|---|---|
| `#!/bin/bash` | Avisa ao sistema que o arquivo deve ser interpretado pelo Bash. |
| `cd "$(dirname "$0")" \|\| exit 1` | `$0` é o caminho do próprio script e `dirname` extrai a pasta dele. O `cd` entra nessa pasta, então o script funciona mesmo se você o chamar de outro lugar. Se não conseguir entrar, o `exit 1` encerra com erro. |
| `python3 calculadora.py` | Executa o programa em Python. |

### Passo a passo para executar

1. Abra o terminal na pasta do projeto.
2. Dê permissão de execução ao script (só é preciso na primeira vez):
   ```bash
   chmod +x calculadora/executar.sh
   ```
3. Execute:
   ```bash
   ./calculadora/executar.sh
   ```
   Se preferir não mexer nas permissões, também funciona assim:
   ```bash
   bash calculadora/executar.sh
   ```

> Se aparecer `Permission denied`, o script está sem permissão de execução: rode o `chmod +x` do passo 2. Se aparecer `python3: command not found`, instale o Python 3 (no Ubuntu: `sudo apt install python3`).

## 🐍 Explicação do código Python

O código está em `calculadora/calculadora.py` e é dividido em partes pequenas, cada uma com uma responsabilidade.

### 1. Funções das operações

```python
def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        return None  # divisão por zero
    return a / b
```

Há uma função para cada operação (`somar`, `subtrair`, `multiplicar`, `dividir`). Todas recebem dois números e devolvem o resultado. A `dividir` devolve `None` quando o divisor é zero, para o programa saber que houve um erro em vez de quebrar.

### 2. Dicionário `OPERACOES`

```python
OPERACOES = {
    "1": ("Soma", "+", somar),
    "2": ("Subtração", "-", subtrair),
    "3": ("Multiplicação", "x", multiplicar),
    "4": ("Divisão", "/", dividir),
}
```

Cada opção do menu (a chave, como `"1"`) guarda uma tupla com o **nome**, o **símbolo** e a **função** da operação. Como funções também podem ser guardadas em variáveis, o programa escolhe a operação só consultando o dicionário, sem precisar de vários `if`.

### 3. `ler_numero(mensagem)`

Pede um número ao usuário dentro de um `while True`, e só sai do laço quando o valor é válido. O texto passa por `strip()` (remove espaços) e `replace(",", ".")` (aceita vírgula), e depois por `float()`. Se o usuário digitar letras, o `float()` gera um `ValueError`, que é capturado pelo `try/except`. O programa avisa e pergunta de novo.

### 4. `formatar(numero)`

Usa `is_integer()` para saber se o número é inteiro. Se for, mostra sem casa decimal (`3` em vez de `3.0`). Se não for, arredonda para até 6 casas com `round()`.

### 5. `mostrar_menu()`

Percorre o dicionário com `for chave, (nome, simbolo, _) in OPERACOES.items()` e imprime uma linha para cada operação. O menu é gerado automaticamente a partir do dicionário.

### 6. `main()`

É o fluxo principal do programa:

1. Mostra o cabeçalho e pergunta o **nome** do usuário.
2. Lê os **dois números** com `ler_numero`.
3. Mostra o menu e lê a **opção**.
4. Se a opção não existir no dicionário, avisa e encerra.
5. Busca a função em `OPERACOES`, calcula com `funcao(a, b)` e mostra o resultado (ou o erro de divisão por zero).

### 7. `if __name__ == "__main__":`

Garante que o `main()` só rode quando o arquivo é executado diretamente (por exemplo, pelo `executar.sh`), e não quando ele é apenas importado por outro código Python.

## 🧩 Como adicionar um novo modo

Cada operação é uma função registrada no dicionário `OPERACOES`, e o menu é montado sozinho a partir dele. Para criar, por exemplo, a potência:

```python
def potencia(a, b):
    return a ** b

OPERACOES["5"] = ("Potência", "^", potencia)
```

## 📂 Organização das pastas

```
calculadora1.0/
├── calculadora/
│   ├── calculadora.py    # código principal
│   └── executar.sh       # script que roda o programa (Linux)
├── executar.bat          # duplo clique para rodar no Windows
├── README.md             # este arquivo
└── codigos_usados.txt    # comandos usados durante o projeto
```

## 👤 Autor

Feito por **<seu nome>**.
