from openai import OpenAI
client = OpenAI()

# Abrir o arquivo em modo de leitura ('r')
with open('txtRecortados/sumarios.json', 'r') as arquivo:
    # Ler o conteúdo do arquivo
    conteudo = arquivo.read()


#print(f'Você não responderá as questões, aqui está organizado os sumarios de 3 em um json de sumário, de acorodo com a pergunta qual é o `nomeDodocumento`e` `titulo` a `pagina` relacionado no json? os dados json para sua pesquisa estão aqui: {conteudo}')

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": f'Você não responderá as questões, aqui está organizado os sumarios de 3 em um json de sumário, de acorodo com a pergunta qual é o `nomeDodocumento`e` `titulo` a `pagina` relacionado no json? os dados json para sua pesquisa estão aqui: {conteudo}'},
        {
            "role": "user",
            "content": "onde encontro a resposta para a questão: Como calcular através das minhas notas se eu passei ou não?"
        }
    ]
)




print(completion.choices[0].message)