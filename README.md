Prof. MSc. Hugo Menezes Barra
Qualidade e Teste de Software
Atividade Prática: Auditoria de Acessibilidade
Instruções da Atividade: Escolha cinco sites reais de sua preferência (ex: portal da
universidade, e-commerce ou sites de notícias) e realize os 4 passos de auditoria
abaixo para cada um deles.
Questão 1 - Utilizando o VSCode e o Python, desenvolva e execute o script com a
biblioteca axe-selenium-python para varrer os cinco sites escolhidos. O script deve
gerar cinco arquivos distintos (um para cada site, ex: site1_acess.json,
site2_acess.json) com os resultados da análise.
Questão 2 - Abra os cinco arquivos gerados pelo seu script. Analise a chave de
violações ("violations") de cada relatório e liste 3 (três) tipos de problemas
diferentes apontados pelo robô para cada site (totalizando 15 problemas listados
no final). Para cada problema, você deve anotar:
 A descrição do erro (qual regra do WCAG foi quebrada).
 Em qual elemento de código (linha/tag HTML) o erro ocorreu.
Questão 3 - Nos mesmos cinco sites escolhidos, realize os dois testes abaixo e
anote suas observações para cada um deles:
A) Teste de Teclado: Guarde o mouse. Navegue por cada site do início ao fim
usando apenas a tecla Tab (avançar) e Shift + Tab (voltar).
o Responda (para cada site): O site possui o indicador de foco visível
(a borda indicando onde você está)? Você ficou preso em algum
menu oculto ou pop-up?
B) Teste de Zoom: Aplique 200% de zoom no navegador em cada site.
o Responda (para cada site): A tela se adaptou bem? Algum botão
importante "sumiu" ou ficou impossível de ser clicado?
Questão 4 - Ative o leitor de tela do seu sistema operacional (Ex: Narrador do
Windows pelo atalho Win + Ctrl + Enter). Feche os olhos ou desligue o monitor. Tente
encontrar o campo de busca desses sites ou ler os títulos principais ouvindo
apenas a voz sintetizada. Anote brevemente como foi a sua experiência geral e qual
foi a maior dificuldade ao navegar por esses ambientes.
Entregáveis Finais
Ao final da atividade, você deve enviar os seguintes arquivos:
1. Arquivos de Código: Os cinco arquivos .json gerados pelo seu script na
Questão 1.
2. Relatório de Análise (em PDF). Um documento contendo:
o As 3 violações descritas para cada um dos 5 sites (solicitadas na
Questão 2).
o As respostas sobre a experiência do Teste Manual separadas para
cada site (Questão 3, itens A e B).
o Um breve parágrafo (de 5 linhas) descrevendo como foi a sua
experiência prática geral de tentar usar a internet de "olhos fechados"
com o leitor de tela (Questão 4). 
