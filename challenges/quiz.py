questions = [
    {
        'Question': "Quanto é 2+2? ",
        'Options': ['1', '3', '4', '6'],
        'CorrectAnswer': '4'
    },
    {
        'Question': "Quanto é 5²? ",
        'Options': ['25', '20', '10', '50'],
        'CorrectAnswer': '25'
    },
            {
        'Question': "Qual a capital do Brasil? ",
        'Options': ['Corinthians', 'São Paulo', 'Rio de Janeiro', 'Brasilia'],
        'CorrectAnswer': 'Brasilia'
    },
                {
        'Question': "Quantos estados tem o nordeste brasileiro? ",
        'Options': ['10', '9', '11', '12'],
        'CorrectAnswer': '9'
    },
]

answers = []
dictMapOptionsAsLetters = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
}

def get_key_object_by_value(value: any, object: dict) -> str:
    for key in object.keys():
        if object[key] == value: return key
    
    return None    

for question in questions:
    print()
    print("Pergunta", question['Question'])
    for index, option in enumerate(question['Options']):
        print(f"{dictMapOptionsAsLetters[str(index + 1)]})", option)

    answer = input("Sua alternativa: ")
    answers.append(answer.upper())
        

print()
print(("-" * 10), "Resultado", ("-" * 10))

for index, option_selected in enumerate(answers):
    question_to_check_data = questions[index]
    INDEX_OPTION_SELECTED_BY_USER = int((get_key_object_by_value(option_selected, dictMapOptionsAsLetters))) - 1
    INDEX_CORRECT_ANSWER_IN_OPTIONS = int(question_to_check_data['Options'].index(question_to_check_data['CorrectAnswer']))
            
    if INDEX_CORRECT_ANSWER_IN_OPTIONS != INDEX_OPTION_SELECTED_BY_USER:
        print()
        print(f"Errou questão {question_to_check_data['Question']}")
        print(f"Respondeu {question_to_check_data['Options'][INDEX_OPTION_SELECTED_BY_USER]}")
        print(f"Mas a resposta era {question_to_check_data['CorrectAnswer']}")
    else:
        print()
        print(f"Acertou a questão {question_to_check_data['Question']}")

            
    