from search import search_prompt

def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    pergunta = input("Digite sua pergunta: ")

    resposta = search_prompt(pergunta)

    print("\nResposta:")
    print(resposta)

if __name__ == "__main__":
    main()