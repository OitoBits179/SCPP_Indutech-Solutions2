SCPP — InduTech Solutions

Sistema de Controle de Pendências de Produção

O SCPP é uma aplicação desenvolvida para auxiliar no registro, na consulta e no acompanhamento de pendências relacionadas à produção.

O sistema permite organizar informações sobre produtos, operadores responsáveis e problemas identificados, acompanhar o status das pendências e gerar relatórios em PDF e Excel.

1. Objetivo do sistema

O objetivo do SCPP é facilitar o controle das pendências de produção, centralizando informações importantes em um único sistema.

Com ele, é possível:

- Cadastrar novas pendências.
- Consultar e pesquisar pendências registradas.
- Acompanhar pendências pendentes e resolvidas.
- Registrar a resolução de pendências pelo perfil Responsável.
- Exportar relatórios em PDF e Excel.
- Personalizar a aparência da interface.

2. Instalação e execução

2.1. Pré-requisitos

Para executar o sistema, é necessário ter:

- Windows 10 ou Windows 11.
- Python instalado.
- Acesso à internet para baixar o projeto e instalar as dependências.

Não é necessário instalar o Git para seguir este procedimento.

2.2. Instalar o Python

1. Acesse o site oficial: https://www.python.org/downloads/
2. Baixe uma versão estável do Python compatível com as dependências do projeto.
3. Execute o instalador.
4. No Windows, marque a opção Add Python to PATH, se estiver disponível.
5. Conclua a instalação.

Para verificar se o Python está instalado, abra o Prompt de Comando e execute:

python --version

Se esse comando não funcionar, tente:

py --version

2.3. Baixar o projeto

1. Acesse o repositório do SCPP: https://github.com/OitoBits179/SCPP_Indutech-Solutions2
2. Clique em Code.
3. Selecione Download ZIP.
4. Após o download, extraia os arquivos para uma pasta do computador.
5. Abra a pasta extraída que contém os arquivos "main.py" e "requirements.txt".

2.4. Abrir o terminal na pasta do projeto

Abra a pasta que contém o arquivo "main.py".

No Explorador de Arquivos do Windows:

1. Clique na barra de endereço.
2. Digite "cmd".
3. Pressione Enter.

O Prompt de Comando será aberto nessa pasta.

Para conferir os arquivos, execute:

dir

Verifique se "main.py" e "requirements.txt" aparecem na lista.

2.5. Criar e ativar o ambiente virtual

O ambiente virtual ajuda a manter as dependências do projeto organizadas e isoladas de outras aplicações Python.

Crie o ambiente virtual:

python -m venv venv

Ative-o no Windows:

venv\Scripts\activate

Se o comando "python" não funcionar, mas "py --version" funcionar, utilize "py" no comando de criação do ambiente virtual.

Após a ativação, normalmente aparecerá "(venv)" no início da linha do terminal.

2.6. Instalar as dependências

Com o ambiente virtual ativado e o terminal na pasta principal do projeto, execute:

python -m pip install -r requirements.txt

Esse comando instala automaticamente as bibliotecas listadas no arquivo "requirements.txt", sem a necessidade de instalar cada biblioteca separadamente.

Aguarde a conclusão da instalação antes de continuar.

O módulo "tkinter", utilizado na interface gráfica, também precisa estar disponível na instalação do Python.

Para verificar se as dependências foram instaladas sem conflitos identificados pelo "pip", execute:

python -m pip check

2.7. Executar o sistema

Após concluir a instalação, execute:

python main.py

Se o comando "python" não funcionar, tente:

py main.py

Se tudo estiver configurado corretamente, a tela de login do SCPP será apresentada.

3. Tela de login

Ao iniciar o sistema, o usuário poderá escolher entre dois perfis.

Funcionário

Permite acessar as funcionalidades de cadastro e consulta de pendências.

Responsável

Exige uma senha e permite utilizar a funcionalidade de resolução de pendências, além das demais funcionalidades disponíveis para esse perfil.

Importante: a versão atual utiliza uma senha de demonstração definida no código. Para uso real, recomenda-se implementar um mecanismo de autenticação mais seguro.

4. Funcionalidades do sistema

4.1. Tela inicial

A tela inicial apresenta um resumo das pendências registradas:

- Total: quantidade total de pendências.
- Pendentes: quantidade de pendências ainda não resolvidas.
- Resolvidas: quantidade de pendências concluídas.

4.2. Cadastrar pendência

Para cadastrar uma pendência:

1. Acesse Cadastrar pendência no menu lateral.
2. Informe o produto.
3. Informe o operador responsável.
4. Descreva a natureza da pendência.
5. Clique em Registrar pendência.

Todos os campos são obrigatórios. Após o cadastro, o sistema gera um identificador, registra a data e a hora e define o status inicial como Pendente.

4.3. Consultar pendências

Acesse Consultar pendências para visualizar os registros.

A pesquisa permite localizar informações por ID, produto, operador, natureza, data, hora ou status.

4.4. Resolver pendência

Essa funcionalidade está disponível somente para o perfil Responsável.

1. Acesse Resolver pendência.
2. Selecione a pendência desejada.
3. Clique em Resolver pendência selecionada.
4. Aguarde a confirmação.

Após a resolução, o status passa para Resolvida, e a data e a hora da resolução são registradas.

4.5. Exportar relatórios

O sistema permite exportar os registros em dois formatos.

PDF: clique em Exportar PDF, escolha o local de destino e salve o documento.

Excel: clique em Exportar Excel, escolha o local de destino e salve a planilha.

Os relatórios apresentam informações das pendências, incluindo seus identificadores, produtos, operadores, natureza, datas, horários e status. A exportação não remove os registros armazenados.

4.6. Alterar o tema

A opção Tema da interface permite selecionar os temas Claro, Escuro ou Sistema, conforme as opções disponíveis na aplicação.

4.7. Sair ou trocar de usuário

Clique em Sair / Trocar usuário e confirme a operação para retornar à tela de login e selecionar outro perfil.

5. Armazenamento dos dados

As pendências são armazenadas localmente no arquivo "banco_dados.json", localizado na pasta principal do projeto.

Os registros incluem informações como:

- Identificador da pendência.
- Produto.
- Operador responsável.
- Natureza da pendência.
- Data e hora do cadastro.
- Status.
- Data e hora da resolução, quando aplicável.

O sistema utiliza esse arquivo para recuperar os registros quando é iniciado novamente.

Recomendação: faça cópias de segurança do arquivo "banco_dados.json" para evitar a perda dos registros.

6. Solução de problemas

- O Python não é reconhecido: verifique a instalação e tente o comando "py --version".
- O arquivo "requirements.txt" não foi encontrado: confira se o terminal está na pasta correta do projeto.
- Uma biblioteca está ausente: execute novamente "python -m pip install -r requirements.txt" com o ambiente virtual ativado.
- Uma imagem não aparece: confira se os arquivos estão na pasta "assets" e se seus nomes estão corretos.
- Os dados não são salvos: verifique se o programa tem permissão para gravar arquivos na pasta do projeto.
- O sistema não inicia: confira a mensagem de erro exibida no terminal e verifique se o Python e as dependências foram instalados corretamente.

7. Tecnologias utilizadas

- Python: linguagem de programação.
- CustomTkinter: criação da interface gráfica.
- Tkinter e ttk: componentes adicionais da interface.
- Pillow: carregamento e tratamento das imagens.
- ReportLab: geração de relatórios em PDF.
- OpenPyXL: criação de planilhas do Excel.
- JSON: armazenamento local dos registros.

8. Organização do projeto

A estrutura principal do projeto é organizada da seguinte forma:

SCPP_Indutech-Solutions2/
├── main.py
├── banco_dados.json
├── requirements.txt
├── README.md
├── assets/
│   ├── logo_login.png
│   ├── logo_claro.png
│   └── logo_escuro.png
└── modulos/
    ├── interface.py
    └── persistencia.py

Descrição dos arquivos e diretórios:

- "main.py": inicia a aplicação.
- "modulos/interface.py": reúne as telas e funcionalidades do sistema.
- "modulos/persistencia.py": realiza o carregamento e o salvamento dos dados.
- "assets/": contém as imagens utilizadas na interface.
- "requirements.txt": lista as bibliotecas necessárias para executar o sistema.
- "README.md": contém a documentação e as instruções de instalação e utilização.
- "banco_dados.json": armazena os registros das pendências e pode ser criado automaticamente pela aplicação.

9. Considerações finais

O SCPP — InduTech Solutions foi desenvolvido com o propósito de tornar o acompanhamento das pendências de produção mais organizado e acessível.

Ao reunir cadastro, consulta, resolução e exportação de relatórios em uma única aplicação, o sistema contribui para a visualização das informações e o acompanhamento das atividades relacionadas à produção.
