from datetime import datetime


def saudacao():
    hora = datetime.now().hour

    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    return "Boa noite!"


def perguntas():
    print(
        """
Perguntas frequentes:

1. Como funciona o cadastro?
2. Quais informações são necessárias?
3. Como posso editar meu cadastro?
4. Como posso excluir meu cadastro?
5. Como funciona a política de privacidade?
"""
    )


def respostas(pergunta):
    respostas_por_opcao = {
        1: "Para se cadastrar, você precisa preencher um formulário com suas informações pessoais e criar uma senha.",
        2: "As informações necessárias para o cadastro incluem nome completo, endereço de e-mail, número de telefone e data de nascimento.",
        3: "Para editar seu cadastro, você precisa acessar sua conta e clicar na opção 'Editar Perfil'.",
        4: "Para excluir seu cadastro, você precisa acessar sua conta e clicar na opção 'Excluir Conta'.",
        5: "A política de privacidade explica como coletamos, usamos e protegemos suas informações pessoais. Você pode acessá-la no nosso site.",
    }
    return respostas_por_opcao.get(
        pergunta,
        "Desculpe, não entendi a pergunta. Por favor, escolha uma das opções acima.",
    )


def ler_pergunta():
    while True:
        entrada = input("Digite o número da sua pergunta (1 a 5): ").strip()
        try:
            pergunta = int(entrada)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if 1 <= pergunta <= 5:
            return pergunta
        print("Escolha uma opção de 1 a 5.")


def main():
    print(saudacao())
    print("Olá! Sou seu assistente virtual da Óculos Online.")
    print("Como posso ajudar você?")
    perguntas()

    pergunta = ler_pergunta()
    print("\nChatbot:", respostas(pergunta))


if __name__ == "__main__":
    main()
