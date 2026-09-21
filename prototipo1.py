palavra_chave = 'AOT'

with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read().upper()
    for linha in arquivo:
        if palavra_chave in linha:
            print(linha.strip())
#print(conteudo)