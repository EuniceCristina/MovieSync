dados_pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Natal"
}
# Adicionando um novo dado
dados_pessoa["profissão"] = "Engenheira"

# Modificando um dado existente
dados_pessoa["idade"] = 29
print(dados_pessoa.get("idade", "Não informada"))