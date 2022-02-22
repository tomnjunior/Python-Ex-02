#Foi criado uma função chamada concatenador que será utilizada
#para concatenar a primeira letra do nome, mais o sobrenome, mais os dois
#últimos números do RU e ao final de tudo concatenar a um endereço de email.

def concatenador(nome: str, sobrenome: str, ru: int):
    if len(nome) > 0 and len(sobrenome) > 0 and len(ru) > 0:
        # utilizei o len() para saber o numero de caracteres.
        email = nome[0].lower() + sobrenome.lower() + ru + '@algoritmos.com.br.'
        # o nome e o sobrenome foram transformados em letras minúsculas
        # e na posição 0 do nome foi retirado a primeira letra.
        # Tudo foi inserido em na variavel email para a criação do email
    return 'Sr. ' + nome + ' ' + sobrenome + ', seu email é: ' + email
    #será retornado a frase pronta


#programa principal
# O usuário deverá inserir o nome, sobrenome e os dois ultimos digitos do RU para
# ser impresso em tela a frase com o email de forma concatenada através da função criada.
nome = input('Nome: ').lower().capitalize().strip()
sobrenome = input('Sobrenome: ').lower().capitalize().strip()
ru = input('Dois últimos números do RU:').strip()
print(concatenador(nome, sobrenome, ru))
# dentro do print foi inserido o comando que chama a função concatenador que foi criada acima.
