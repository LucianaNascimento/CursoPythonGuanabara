"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)
Adicione tambeem as docstrings da função
"""


def notas(*args, situacao=False):
    """Funcão para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return dicionário com várias informações sobre a situação da turma.
    """
    info = dict()
    info['total'] = len(args)
    info['maior'] = max(args)
    info['menor'] = min(args)
    info['media'] = sum(args)/len(args)

    if situacao:
        if info['media'] >= 7:
            info['situacao'] = 'BOA'
        elif info['media'] >= 5:
            info['situacao'] = 'RAZOÁVEL'
        else:
            info['situacao'] = 'RUIM'
        return info


# Programa principal:
resp = notas(5.5, 2.5, 1.5, situacao=True)
print(resp)
#help(notas)