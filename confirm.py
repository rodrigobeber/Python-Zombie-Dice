def confirm(mensagem):
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input(mensagem)
        answer = answer.upper()
    return answer == 'Y'