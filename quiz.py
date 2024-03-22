'''Declarar as perguntas, opções e respostas numa lista com dicionários
para que o código seja mais coeso e facilite o manejo e manutenção do
código'''

questions = [
	{
		'pergunta': 'Qual a estrela mais velha do Universo?',
		'opcoes': ['a) Proxima Centauri', 'b) Via Lactea', 'c) Matusalé\
m', 'd) Sol'],
		'resposta': 'c'
	},
	{
		'pergunta': 'Qual o único país com uma bandeira que não é um qu\
adrilátero?',
		'opcoes': ['a) Brasil', 'b) Polônia', 'c) Nepal', 'd) Suíça'],
		'resposta': 'c'
	},
	{
		'pergunta': 'Qual a língua que se fala na Holanda?',
		'opcoes': ['a) Holandês', 'b) Inglês', 'c) Francês', 'd) Chinês\
'],
		'resposta': 'a'
	}
]


# Função que apresenta perguntas e verifica respostas.
def jogar_quiz(questions):
	pontos = 0

	print('Quiz!')

	'''Iterar sobre cada index da lista. Ao fazer isso, podem ser
	acessados os dicionários dos index da lista
	Exemplo:
	(question['pergunta']) <-- Acessa o índice "pergunta" do dicionário
	em questão do index lido da lista questions'''
	
	for question in questions:
		
		'''Imprime a pergunta do index da lista'''
		print(question['pergunta'])
		
		for opcao in question['opcoes']:
			'''Imprime as opções de respostas do index da lista'''
			print(opcao)
		
		
		'''Solicita uma resposta do usuário de acordo com o listado.'''
		resposta_usuario = input('Escolha a opção correta (a, b, c, ou \
d): ').lower()


		'''Loop while para garantir que o usuário insira uma opção
		correta. O loop só é ignorado caso a resposta seja válida.'''
		while resposta_usuario not in ['a', 'b', 'c', 'd']:
			print('Por favor, escolha uma opção válida.')
			resposta_usuario = input('Escolha a opção correta (a, b, c,\
 ou d): ').lower()

		'''Verifica se o input do usuário equivale à resposta'''
		if resposta_usuario == question['resposta']:
			print('Resposta correta!\n')
			pontos += 1
		else:
			print('Resposta incorreta. A resposta correta é:',\
question['resposta'])
	print('Você fez', pontos, 'pontos de', len(questions))

# Chamada da função para iniciar o quiz.
jogar_quiz(questions)