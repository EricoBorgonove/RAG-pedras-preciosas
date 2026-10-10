from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

pasta_saida = Path("base_pedras/pdfs")
pasta_saida.mkdir(parents=True, exist_ok=True)

pedras = [
    {"arquivo":"diamante.pdf","titulo":"Diamante","texto":"""O diamante é uma forma cristalina do carbono.\n\nÉ conhecido principalmente por sua elevada dureza, atingindo valor 10 na escala de Mohs.\n\nOs diamantes podem ser incolores ou apresentar diferentes tonalidades.\n\nNa gemologia, características como cor, pureza, corte e peso são utilizadas na avaliação dos diamantes.\n\nApesar de possuir elevada dureza, o diamante pode sofrer fraturas quando submetido a impactos."""},
    {"arquivo":"rubi.pdf","titulo":"Rubi","texto":"""O rubi é uma variedade vermelha do mineral coríndon.\n\nSua coloração vermelha está relacionada principalmente à presença de cromo.\n\nO rubi possui dureza 9 na escala de Mohs.\n\nEssa elevada dureza torna o rubi uma gema adequada para utilização em diferentes tipos de joias.\n\nRubi e safira pertencem à mesma espécie mineral, conhecida como coríndon."""},
    {"arquivo":"safira.pdf","titulo":"Safira","texto":"""A safira pertence ao grupo mineral do coríndon.\n\nA safira azul é a variedade mais conhecida, mas também existem safiras amarelas, verdes, rosadas e violetas.\n\nSua dureza é 9 na escala de Mohs.\n\nRubi e safira apresentam a mesma composição mineral básica, diferenciando-se principalmente pelas características de cor."""},
    {"arquivo":"esmeralda.pdf","titulo":"Esmeralda","texto":"""A esmeralda é uma variedade verde do mineral berilo.\n\nSua coloração está relacionada principalmente à presença de determinados elementos na estrutura cristalina.\n\nA dureza da esmeralda fica aproximadamente entre 7,5 e 8 na escala de Mohs.\n\nInclusões internas são frequentemente observadas em esmeraldas naturais.\n\nA água-marinha também pertence ao grupo do berilo."""},
    {"arquivo":"agua_marinha.pdf","titulo":"Água-marinha","texto":"""A água-marinha é uma variedade do mineral berilo.\n\nNormalmente apresenta tonalidades que variam entre azul claro e azul esverdeado.\n\nSua dureza está aproximadamente entre 7,5 e 8 na escala de Mohs.\n\nCristais de água-marinha podem atingir dimensões consideráveis.\n\nEsmeralda e água-marinha pertencem ao mesmo grupo mineral."""},
    {"arquivo":"ametista.pdf","titulo":"Ametista","texto":"""A ametista é uma variedade de quartzo.\n\nSua característica mais conhecida é a coloração roxa.\n\nSua composição está baseada principalmente em dióxido de silício.\n\nA ametista apresenta dureza 7 na escala de Mohs.\n\nO Brasil possui importantes ocorrências naturais de ametista."""},
    {"arquivo":"topazio.pdf","titulo":"Topázio","texto":"""O topázio é um mineral que pode apresentar diferentes cores.\n\nExistem exemplares incolores, amarelos, azuis, rosados e alaranjados.\n\nO topázio apresenta dureza 8 na escala de Mohs.\n\nApesar de sua boa resistência a riscos, o mineral apresenta planos de clivagem que podem facilitar determinadas fraturas."""},
    {"arquivo":"turmalina.pdf","titulo":"Turmalina","texto":"""A turmalina representa um grupo de minerais com composição química complexa.\n\nPode ser encontrada em praticamente todas as cores.\n\nSua dureza geralmente varia entre 7 e 7,5 na escala de Mohs.\n\nAlgumas variedades brasileiras de turmalina apresentam tonalidades intensas de azul e verde."""},
    {"arquivo":"peridoto.pdf","titulo":"Peridoto","texto":"""O peridoto é a variedade gemológica do mineral olivina.\n\nSua coloração normalmente varia entre verde e verde amarelado.\n\nSua dureza fica aproximadamente entre 6,5 e 7 na escala de Mohs.\n\nMinerais semelhantes à olivina também podem ser encontrados em alguns meteoritos."""},
    {"arquivo":"opala.pdf","titulo":"Opala","texto":"""A opala é formada principalmente por sílica hidratada.\n\nPode apresentar diversas cores.\n\nAlgumas variedades apresentam um fenômeno óptico conhecido como jogo de cores.\n\nSua dureza normalmente varia aproximadamente entre 5 e 6,5 na escala de Mohs.\n\nA organização microscópica da sílica influencia os efeitos ópticos observados em determinadas opalas."""}
]

estilos = getSampleStyleSheet()

for pedra in pedras:
    caminho = pasta_saida / pedra["arquivo"]
    documento = SimpleDocTemplate(str(caminho), pagesize=A4)
    elementos = [Paragraph(pedra["titulo"], estilos["Title"]), Spacer(1, 20)]
    for paragrafo in pedra["texto"].strip().split("\n\n"):
        elementos.append(Paragraph(paragrafo.strip(), estilos["BodyText"]))
        elementos.append(Spacer(1, 12))
    documento.build(elementos)
    print("Criado:", caminho)

print("\nTodos os PDFs foram criados.")
