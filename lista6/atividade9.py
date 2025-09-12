class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        return self.media() >= 6


class Turma:
    def __init__(self):
        self.alunos = []  

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def media_turma(self):
        notas_turma = [nota for aluno in self.alunos for nota in aluno.notas]
        media = sum(notas_turma) / len(notas_turma)
        return media

aluno1 = Aluno("João", [8, 7, 9])
aluno2 = Aluno("Maria", [6, 5, 7])
aluno3 = Aluno("Pedro", [9, 8, 9])

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

print(f"Média da turma: {turma.media_turma():.2f}")