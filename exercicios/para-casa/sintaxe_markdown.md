# Sintaxe do Markdown - Principais pontos

O Markdown é uma linguagem de marcação leve e fácil de usar para formatar textos de forma simples e rápida, sendo utilizada para escrever documentos, criar páginas da web, postar em fóruns e muito mais. A sintaxe do Markdown é projetada para ser legível e intuitiva, permitindo que os usuários formatem o texto sem a necessidade de conhecer HTML ou outras linguagens de marcação mais complexas.

## Títulos e subtítulos

Utilize o caracter "#" seguido de espaço para indicar títulos, subtítulos e subtópicos. A quantidade de # indica o nível do título, de 1 (maior) a 6 (menor). Exemplo:

> `# Título de nível 1`  
`## Título de nível 2`  
`### Título de nível 3`  
`#### Título de nível 4`   
`##### Título de nível 5`  
`###### Título de nível 6`    

Será exibido como:
# Título de nível 1
## Título de nível 2
### Título de nível 3
#### Título de nível 4 
##### Título de nível 5
###### Título de nível 6

## Parágrafo e quebra de linha

Para criar um novo parágrafo, simplesmente insira uma linha em branco entre os parágrafos. Para inserir uma quebra de linha, coloque dois espaços no final da linha.

## Ênfase

Use * ou _ para enfatizar o texto. Por exemplo:    
> `*itálico* ou _itálico_`  
`**negrito** ou __negrito__`

Será exibido como:  
*itálico* ou _itálico_  
**negrito** ou __negrito__

## Listas

Crie listas não ordenadas usando *, - ou + no início de cada linha de item. Para listas ordenadas, use números seguidos por um ponto. Exemplo:

> `* Item 1`  
`* Item 2`  
`1. Item A`  
`2. Item B`  
`2.1 Subitem 2.1`

Será exibido como:

* Item 1
* Item 2
1. Item A
2. Item B  
2.1 Subitem 2.1  

## Links:

Para criar links, coloque o texto do link entre colchetes [ ] e o URL entre parênteses ( ). Exemplo:

> `[Slack da Reprograma](https://reprograma.slack.com/archives/C05KZ787CJV)`

Será exibido como:  
[Slack da Reprograma](https://reprograma.slack.com/archives/C05KZ787CJV)

## Citações em Bloco:

Use o caractere > no início das linhas para criar citações em bloco. Exemplo:

> `> Exemplo de citação em bloco`

Será exibido como:

> Exemplo de citação em bloco

## Código Inline e em Bloco:
Para destacar código inline, use o caracter `. Para blocos de código, coloque três backticks (```) antes e depois do bloco, seguido pelo nome da linguagem (opcional) para realce de sintaxe. Exemplo:

> \`código inline`

Será exibido como:

`código inline`

Ou então:

> \```python  
def exemplo():  
    print("Olá, mundo!")  

Será exibido como:
```python
def exemplo():
    print("Olá, mundo!")