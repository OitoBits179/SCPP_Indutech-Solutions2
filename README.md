SCPP — InduTech Solutions
Sistema de Controle de Pendências de Produção
O SCPP (Sistema de Controle de Pendências de Produção) é uma aplicação desenvolvida para auxiliar no registro, na consulta e no acompanhamento de pendências relacionadas à produção.
O sistema permite organizar informações sobre produtos, operadores responsáveis e problemas identificados, além de acompanhar o status das pendências e gerar relatórios.
1. Objetivo do sistema
O objetivo do SCPP é facilitar o controle das pendências de produção, centralizando informações importantes em um único sistema.
Com ele, é possível:
• Cadastrar novas pendências.
• Consultar e pesquisar pendências registradas.
• Acompanhar pendências pendentes e resolvidas.
• Registrar a resolução de pendências por meio do perfil Responsável.
• Exportar relatórios em PDF e Excel.
• Personalizar a aparência da interface.
2. Instalação e execução do sistema
Para executar o SCPP, é necessário ter o Python instalado no computador e baixar os arquivos do projeto.
2.1. Pré-requisitos
Instale o Python pelo site oficial:
https://www.python.org/downloads/
Durante a instalação no Windows, marque a opção Add Python to PATH, se ela estiver disponível.
Não é necessário instalar o Git para seguir estas instruções.
2.2. Baixar o projeto
1. Acesse o repositório do SCPP no GitHub:
2. https://github.com/OitoBits179/SCPP_Indutech-Solutions2
3. Clique no botão Code.
4. Selecione Download ZIP.
5. Aguarde o download do arquivo.
6. Extraia o conteúdo do ZIP para uma pasta do computador.
2.3. Abrir o terminal na pasta do projeto
Entre na pasta extraída, onde estão os arquivos main.py e requirements.txt.
Abra o terminal nessa pasta. No Windows, você pode abrir a pasta no Explorador de Arquivos, clicar na barra de endereço, digitar cmd e pressionar Enter.
2.4. Criar um ambiente virtual
Recomenda-se criar um ambiente virtual para manter as bibliotecas do projeto organizadas.
bash
python -m venv venv

Para ativar o ambiente virtual no Windows:
bash
venv\Scripts\activate

No Linux ou macOS:
bash
source venv/bin/activate

2.5. Instalar as dependências
Com o terminal aberto na pasta principal do projeto e o ambiente virtual ativado, execute:
bash
python -m pip install -r requirements.txt

Esse comando instala automaticamente as bibliotecas listadas no arquivo requirements.txt, sem a necessidade de instalar cada biblioteca separadamente.
O arquivo requirements.txt precisa estar na pasta principal do projeto.
O módulo tkinter, utilizado na interface gráfica, também precisa estar disponível na instalação do Python.
2.6. Executar a aplicação
Após concluir a instalação das dependências, execute:
bash
python main.py

A tela de login será apresentada para que o usuário selecione seu perfil.
3. Tela de login
Ao iniciar o sistema, o usuário poderá escolher entre dois perfis:
Funcionário
Permite acessar a interface para cadastrar e consultar pendências.
Responsável
Exige uma senha para entrar e permite utilizar a função de resolução de pendências, além das demais funcionalidades disponíveis.
Importante: a senha configurada no código atual é uma senha fixa de demonstração. Para uso real, recomenda-se implementar um mecanismo de autenticação mais seguro.
4. Tela inicial
Após entrar no sistema, o usuário visualizará a tela inicial, que apresenta uma mensagem de boas-vindas e orientações para utilizar o menu lateral.
Na parte superior da interface, há um resumo com três informações:
• Total: quantidade de pendências registradas.
• Pendentes: quantidade de pendências que ainda não foram resolvidas.
• Resolvidas: quantidade de pendências que já foram concluídas.
Esses números são atualizados conforme as pendências são cadastradas ou resolvidas.
5. Cadastrar pendência
Para registrar uma nova pendência:
1. Clique em Cadastrar pendência, no menu lateral.
2. Informe o nome do produto.
3. Digite o nome do operador responsável.
4. Descreva a natureza da pendência, explicando o problema identificado.
5. Clique em Registrar pendência.
Todos os campos são obrigatórios.
Após o registro, o sistema gera um identificador para a pendência, registra a data e a hora do cadastro e define seu status inicial como Pendente.
Se o registro for salvo corretamente, uma mensagem de confirmação será exibida.
6. Consultar pendências
Para visualizar os registros:
1. Clique em Consultar pendências.
2. Consulte as informações apresentadas na tabela.
3. Se desejar localizar um registro específico, digite um termo no campo de pesquisa.
A pesquisa pode ser realizada por:
• ID da pendência.
• Produto.
• Operador responsável.
• Natureza da pendência.
• Data ou hora.
• Status.
A tabela é atualizada conforme o usuário digita, facilitando a localização das informações.
7. Resolver pendência
A funcionalidade de resolução está disponível somente para o perfil Responsável.
Para resolver uma pendência:
1. Entre no sistema utilizando o perfil Responsável.
2. Clique em Resolver pendência.
3. Localize a pendência desejada na tabela.
4. Selecione o registro.
5. Clique em Resolver pendência selecionada.
6. Aguarde a mensagem de confirmação.
Após a operação, o status passa de Pendente para Resolvida, e a data e a hora da resolução são registradas.
As pendências já resolvidas não aparecem na lista de registros disponíveis para resolução.
8. Exportar relatórios
O SCPP permite exportar os registros cadastrados para dois formatos de arquivo.
Relatório em PDF
1. Clique em Exportar PDF.
2. Escolha o local onde deseja salvar o arquivo.
3. Confirme o nome do relatório.
4. Salve o documento.
O relatório apresenta informações das pendências, incluindo ID, produto, operador, natureza, data, hora, status e data da resolução.
Relatório em Excel
1. Clique em Exportar Excel.
2. Escolha a pasta de destino.
3. Confirme o nome do arquivo.
4. Salve a planilha.
O arquivo pode ser aberto em programas compatíveis com planilhas do Excel, permitindo consultar e organizar os dados.
A exportação não remove as pendências do sistema. Caso não existam registros cadastrados, será exibida uma mensagem informativa.
9. Alterar o tema da interface
No menu lateral, a opção Tema da interface permite selecionar uma das seguintes configurações:
• Claro: utiliza cores claras na área principal.
• Escuro: utiliza cores escuras na área principal.
• Sistema: acompanha a configuração de aparência do sistema operacional, quando suportada.
A tela de login permanece clara, independentemente do tema escolhido para a interface principal.
10. Sair ou trocar de usuário
Para retornar à tela de login:
1. Clique em Sair / Trocar usuário, no menu lateral.
2. Confirme a operação na mensagem exibida.
O sistema retornará à tela de login, permitindo selecionar outro perfil.
11. Armazenamento dos dados
As pendências são armazenadas localmente no arquivo banco_dados.json, localizado na pasta principal do projeto.
Os dados incluem informações como:
• Identificador da pendência.
• Produto.
• Operador responsável.
• Natureza da pendência.
• Data e hora do cadastro.
• Status.
• Data e hora da resolução, quando aplicável.
O sistema utiliza esse arquivo para recuperar os registros quando é iniciado novamente.
Recomendação: faça cópias de segurança do arquivo banco_dados.json para evitar a perda dos registros. Não apague nem edite esse arquivo enquanto o sistema estiver em uso.
12. Solução de problemas
• O sistema não inicia: verifique se o Python está instalado e se o terminal está aberto na pasta principal do projeto.
• Uma biblioteca está ausente: verifique se o arquivo requirements.txt está presente e execute python -m pip install -r requirements.txt.
• Uma imagem não aparece: confira se os arquivos de imagem estão na pasta assets e se os nomes estão corretos.
• Os dados não são salvos: verifique se o programa tem permissão para gravar arquivos na pasta do projeto.
• O relatório não é gerado: confirme se existem pendências cadastradas e se as dependências necessárias foram instaladas corretamente.
13. Tecnologias utilizadas
• Python: linguagem de programação utilizada no desenvolvimento.
• CustomTkinter: criação da interface gráfica.
• Tkinter e ttk: componentes adicionais da interface, incluindo tabelas e caixas de diálogo.
• Pillow: carregamento e tratamento das imagens.
• ReportLab: geração de relatórios em PDF.
• OpenPyXL: criação de planilhas do Excel.
• JSON: armazenamento local dos registros.
14. Organização do projeto
A estrutura principal do projeto é organizada da seguinte forma:
text
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
• main.py: inicia a aplicação.
• modulos/interface.py: reúne as telas e funcionalidades do sistema.
• modulos/persistencia.py: é responsável pelo carregamento e salvamento dos dados.
• assets/: contém as imagens utilizadas na interface.
• requirements.txt: lista as bibliotecas necessárias para executar o sistema.
• README.md: contém a documentação e as instruções de instalação e utilização.
• banco_dados.json: armazena os registros durante o funcionamento do sistema e pode ser criado automaticamente pela aplicação.
O arquivo main.py inicia a aplicação, o módulo interface.py reúne as telas e funcionalidades, e o módulo persistencia.py é responsável pelo carregamento e salvamento dos dados. A pasta assets contém as imagens utilizadas na interface.
15. Considerações finais
O SCPP — InduTech Solutions foi desenvolvido com o propósito de tornar o acompanhamento das pendências de produção mais organizado e acessível.
Ao reunir cadastro, consulta, resolução e exportação de relatórios em uma única aplicação, o sistema contribui para a visualização das informações e o acompanhamento das atividades relacionadas à produção.
