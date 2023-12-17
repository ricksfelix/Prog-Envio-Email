# Programa de Teste de Envio de E-mail
## Português
### Descrição
Este é um programa simples desenvolvido para facilitar o envio de e-mails para fins de teste. Ele permite aos usuários configurar parâmetros de e-mail como destinatário, remetente, servidor SMTP, porta e conteúdo da mensagem, tornando-o ideal para testes rápidos de funcionalidades de e-mail em desenvolvimento de software.

### Como usar
Configuração: Edite o arquivo `config.yaml` para configurar as informações do servidor SMTP, como endereço do servidor, porta, e-mail do remetente e senha.
Execução: Execute o programa e siga as instruções na interface para enviar um e-mail.

Para compilar este programa em um executável standalone utilizando o PyInstaller, siga os seguintes passos:

### Instale o PyInstaller: 
Se ainda não tiver o PyInstaller instalado, você pode instalá-lo via pip com o comando `pip install pyinstaller`

### Criação do Executável: 
Na linha de comando ou terminal, navegue até o diretório do projeto e execute o comando pyinstaller `main.spec` Isso irá gerar uma pasta dist que contém o executável do programa.

### Execução do Executável: 
Navegue até a pasta dist e execute o arquivo compilado para iniciar o programa.

### Requisitos
Python `3.x`
Bibliotecas Python: `smtplib, yaml, PySide6, Pyinstaller`

### Contribuições
Contribuições são bem-vindas. Por favor, envie seu pull request para a branch main.


# English
## Description
This is a simple program developed to facilitate email sending for testing purposes. It allows users to set up email parameters such as recipient, sender, SMTP server, port, and message content, making it ideal for quick testing of email functionalities in software development.

### How to Use
Configuration: Edit the `config.yaml` file to set up SMTP server information like server address, port, sender's email, and password.
Execution: Run the program and follow the instructions in the interface to send an email.

To compile this program into a standalone executable using PyInstaller, follow these steps:

### Install PyInstaller: 
If you do not have PyInstaller installed, you can install it via pip with the command `pip install pyinstaller`

### Executable Creation: 
In the command line or terminal, navigate to the project directory and run the command pyinstaller `main.spec` This will generate a dist folder containing the program's executable.

### Executable Execution:
Navigate to the dist folder and run the compiled file to start the program.

### Requirements
Python `3.x`
Python libraries: `smtplib, yaml, PySide6, Pyintaller`

### Contributions
Contributions are welcome. Please submit your pull request to the main branch.


# License  `GNU General Public License v3.0`