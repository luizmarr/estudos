# Estudos  v2

repositorio com os meus estudos

### Comandos

source .venv/Scripts/activate - ativar o ambiente virtual

## TO-DO:

- [X] colocar os prints de name, localName edate em funcoes, e tambem o country code.
- [X] Ter a opção de ver o feriado por mês, colocar no input o mês (1 - 12) mostrar na tela quais feriados tem naquele mês para cada país. (Criar arquivo ex_03.py) - CORRIGI o YEAR estava fixo
- [X] implementar a validação do código do país e do mês, para não deixar o usuário colocar um código que não existe ou um mês inválido. (Criar arquivo ex_04.py),

DICA: eu ja implementei a validação do ano, é só seguir o mesmo padrão. Para validar o código do país, você pode criar uma lista com os códigos de países válidos e verificar se o código inserido pelo usuário está nessa lista. Para validar o mês, você pode verificar se o número inserido está entre 1 e 12. se o usuario colocar algum valor errado, mostrar uma mensagem de erro e pedir para ele inserir novamente. (DICA: use um loop para isso)

[ ] Ajuste para que no output mostre o nome completo do mes e país.

EX:
ANTIGO:

Feriados em BR para o ano de 2027 e o mês de 12:
2027-12-25: Natal (Christmas Day)

NOVO:

Feriados no Brasil para o ano de 2027 e no mês de dezembro:
2027-12-25: Natal (Christmas Day)
