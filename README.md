### Hi, I'm Michael D.🤙

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-douglas-640a11180/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/michael.douglaspdl/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/MikeeD.Cloud9/)


# Sistema de Reserva de Quartos de Hotel

Este é um sistema simples de reserva de quartos de hotel desenvolvido em Python usando a biblioteca PySide6 para a interface gráfica e o SQLite como banco de dados para armazenar informações sobre os quartos e sua disponibilidade.

## Estrutura do Projeto

O projeto é composto por um único arquivo Python e um arquivo de banco de dados SQLite.

- `sistema_de_reserva_de_quarto_de_hotel.py`: Este é o arquivo principal do projeto, que contém todo o código do sistema, incluindo a definição da classe principal `SistemaReservaHotel` e a lógica de funcionamento.

- `hotel.db`: Este é o arquivo do banco de dados SQLite que armazena informações sobre os quartos do hotel, incluindo o número do quarto e sua disponibilidade.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. Exibição de Quartos Disponíveis: O sistema exibe uma lista de quartos disponíveis para reserva.

2. Exibição de Quartos Ocupados: O sistema exibe uma lista de quartos ocupados.

3. Reserva de Quartos: Os usuários podem inserir o número do quarto desejado em um campo de entrada e clicar no botão "Reservar Quarto" para fazer uma reserva. Se o quarto estiver disponível, a reserva será efetuada e o quarto será marcado como ocupado.

4. Checkout de Quartos: Os usuários podem selecionar um quarto ocupado na lista de quartos ocupados e clicar no botão "Checkout" para liberar o quarto, marcando-o como disponível novamente.

5. Mensagens de Alerta: O sistema exibe mensagens de alerta em caixas de diálogo para informar os usuários sobre o status das operações, como sucesso na reserva, erro de reserva, sucesso no checkout e erro no checkout.

## Comentários no Código

O código-fonte do sistema está bem comentado para explicar cada parte do programa. Aqui estão algumas seções comentadas:

-- Configuração da Interface Gráfica: As configurações iniciais da janela principal, como título e tamanho, são definidas aqui.

-- Conexão com o Banco de Dados: O sistema se conecta a um banco de dados SQLite chamado `hotel.db`. Se a tabela de quartos não existir, ela será criada.

-- Inserção de Quartos de Teste: Para fins de teste, o sistema insere quartos de hotel na tabela se ela estiver vazia.

-- Configuração da Interface Gráfica: Aqui, os widgets da interface gráfica, como listas de quartos disponíveis e ocupados, campos de entrada e botões, são criados e organizados em um layout.

-- Atualização das Listas de Quartos: Este método atualiza as listas de quartos disponíveis e ocupados com base nas informações do banco de dados.

-- Reserva de Quartos: Este método é chamado quando o usuário clica no botão "Reservar Quarto" e lida com a lógica de reserva de quartos.

-- Checkout de Quartos: Este método é chamado quando o usuário clica no botão "Checkout" e lida com a lógica de checkout de quartos.

-- Exibição de Mensagens de Alerta: Este método exibe mensagens de alerta em caixas de diálogo para informar os usuários sobre o resultado das operações.

-- Método para inserir quartos de teste no banco de dados
- `def inserir_quartos_teste(self)`: Inserir quartos de teste no banco de dados.

## Executando o Sistema

Para executar o sistema, é necessário ter Python instalado no seu ambiente. Você também precisa instalar a biblioteca PySide6. Após instalar as dependências, basta executar o arquivo `sistema_de_reserva_de_quarto_de_hotel.py`. O sistema exibirá uma janela com a interface gráfica, onde você pode realizar reservas e checkouts de quartos.

Este é um projeto simples que pode ser expandido com mais recursos e funcionalidades, como a inclusão de informações sobre os hóspedes e a persistência de reservas entre sessões.

Lembre-se de que este projeto é apenas uma demonstração básica de como criar um sistema de reserva de quartos de hotel em Python e pode ser aprimorado para atender às necessidades específicas do seu negócio ou aplicação.
