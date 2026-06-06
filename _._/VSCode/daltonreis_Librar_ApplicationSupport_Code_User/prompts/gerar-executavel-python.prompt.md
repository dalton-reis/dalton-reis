---
name: "Gerar executável Python"
description: "Use quando quiser automatizar a geração de executável de um projeto Python com PyInstaller, incluindo notebooks, scripts, OpenCV, arquivos extras e build para Windows Linux macOS."
agent: "python-executable-packager"
argument-hint: "Ex.: preparar este projeto para gerar executável em Windows, Linux e macOS"
---

Analise o workspace atual e automatize o processo de empacotamento do projeto Python com PyInstaller.  

Siga estas prioridades:

1. Descubra o entrypoint correto do projeto.
2. Se o projeto principal estiver em notebook, gere um `.py` apropriado para distribuição.
3. Crie automação reutilizável no próprio projeto, preferindo scripts e configurações simples.
4. Inclua arquivos de dados e recursos necessários no build.
5. Se o projeto precisar de distribuição em Windows, Linux e macOS, prepare o caminho para builds separados por sistema operacional e, quando fizer sentido, CI com matriz.
6. Entregue o resultado ja implementado no projeto atual, com uma explicação curta de como rodar.
