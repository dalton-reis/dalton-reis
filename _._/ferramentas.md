# Algumas ferramentas

Seguem algumas ferramentas usadas na montagem dos materiais das disciplinas.  

## Editar do Fluxogramas  

Usamos o "PlantUML" que uma notação de "texto plano" para UML.  
Site: <https://plantuml.com/>  

Existem editores online para PlantUML, tipo: <http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000>  
E muitos outros.  

Eu uso uma extensão dentro do VSCode: <https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml>  
É bem simples de usar.  
E na maioria das vezes gero os arquivos SVG (Source Vector Graphics) dos arquivos PlantUML para incluir dentro dos MarkDown e publicar no GitHub.  

Os arquivos do PlantUML podem ter várias extensões, para padronizar eu sempre uso a extensão ".wsd". Então se virem no nosso material do Git algum arquivo com a extensão ".wsd" ele é um PlantUML. Geralmente estão dentro das pastas "_._plantUML".  

Um exemplo pode ser visto em: <https://github.com/dalton-reis/disciplinaIpPrivado/blob/master/Unidade3/_._plantUML/Uni3Uri1001.wsd>  

## Diagramas e Desenhos

E também usamos diagramas e desenhos feitos no Draw.io. O Draw.io tem uma versão online e que pode ser instalada no PC.  
Ver comentário para online: <https://github.com/dalton-reis/disciplinaIpPrivado/blob/master/Unidade1/aulaAnotacoes.md#rabiscos>  
Eu uso uma outra extensão do VSCode: <https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio> que me permite editar o Draw.io direto dentro do VSCode.  

Os arquivos do Draw.io podem ter as extensões ".drawio" e ".drawio.svg".  
Eu uso sempre a ".drawio.svg", pois assim além de permitir usar o Draw.io em si, o arquivo já é do tipo SVG, e assim posso chamar direto no arquivo MarkDown.  
E, o motivo de usar um SVG e não PNG (ou outro) é porque o SVG é um arquivo vetorial e não raster como o PNG, e assim não se tem problemas de aliasing (eheh, "neura" de professor de CG).  

E, algumas vezes injeto chamadas para gerar o PlantUML direto do serve:  
![Diagrama de estados de uma rotina para achar o menor valor entre três valores](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/dalton-reis/disciplinaIpMatA/main/Unidade1/imgs/ExemploOrdenarTresValores.wsd  

Assim, usa o ".wsd" para gerar o SVG direto sem precisar ficar gerando o SVG a cada edição.  

## Notações matemáticas

Bom, e por fim, usamos o Latex para gerar as fórmulas/equações, ou seja, as notações matemáticas. Tipo:  
  /!/[\Large 3+4=x/]/(https://latex.codecogs.com/svg.latex?\Large&space;3+4=x/)  
A motivação é porque o Latex também é "texto plano" e Vetorial.  

Lembro, o uso  de "texto plano" fica prático para verificar as alterações no Github porque é fácil ver o que mudo, diferente de um arquivo PNG, DOCX etc.  

De tempo em tempo eu atualizo o que eu uso de extensões do VSCode aqui:  
<https://github.com/dalton-reis/dalton-reis#vscode>  

Sobre MarkDown:
<https://github.com/dalton-reis/dalton-reis#markdown>  

Sobre GitHub:
<https://github.com/dalton-reis/dalton-reis#github>  

Se tiverem alguma dúvida me avisem que eu ajudo a navegar por este lado "Darth Vader" da programação.  
