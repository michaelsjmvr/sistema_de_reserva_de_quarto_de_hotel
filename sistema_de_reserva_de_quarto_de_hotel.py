import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox

# Definindo a classe principal da aplicação
class SistemaReservaHotel(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Sistema de Reserva de Quartos de Hotel")
        self.setGeometry(100, 100, 800, 600)

        # Conexão com o banco de dados SQLite
        self.conexao = sqlite3.connect("hotel.db")
        self.cursor = self.conexao.cursor()

        # Criação da tabela de quartos se não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS quartos (
            numero INTEGER PRIMARY KEY,
            disponivel INTEGER
        )''')
        self.conexao.commit()

        # Inserção de quartos de teste se a tabela estiver vazia
        self.cursor.execute("SELECT COUNT(*) FROM quartos")
        if self.cursor.fetchone()[0] == 0:
            self.inserir_quartos_teste()

        # Configuração da interface gráfica da janela
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Widget para exibir quartos disponíveis
        self.quartos_disponiveis_list = QListWidget(self)

        # Widget para exibir quartos ocupados
        self.quartos_ocupados_list = QListWidget(self)

        # Widget para reservas
        self.reserva_input = QLineEdit(self)
        self.reserva_input.setPlaceholderText("Digite o número do quarto para reservar")
        self.reserva_button = QPushButton("Reservar Quarto", self)
        self.reserva_button.clicked.connect(self.realizar_reserva)

        # Botão para fazer checkout
        self.checkout_button = QPushButton("Checkout", self)
        self.checkout_button.clicked.connect(self.realizar_checkout)

        # Adicionando elementos à interface gráfica
        layout.addWidget(QLabel("Quartos Disponíveis:"))
        layout.addWidget(self.quartos_disponiveis_list)
        layout.addWidget(QLabel("Quartos Ocupados:"))
        layout.addWidget(self.quartos_ocupados_list)
        layout.addWidget(QLabel("Realizar Reserva:"))
        layout.addWidget(self.reserva_input)
        layout.addWidget(self.reserva_button)
        layout.addWidget(self.checkout_button)

        # Inicialização das listas de quartos disponíveis e ocupados
        self.atualizar_listas_quartos()

    # Método para atualizar as listas de quartos disponíveis e ocupados
    def atualizar_listas_quartos(self):
        self.quartos_disponiveis_list.clear()
        self.quartos_ocupados_list.clear()
        
        self.cursor.execute("SELECT numero, disponivel FROM quartos")
        quartos = self.cursor.fetchall()
        
        for numero, disponivel in quartos:
            if disponivel == 1:
                self.quartos_disponiveis_list.addItem(str(numero))
            else:
                self.quartos_ocupados_list.addItem(str(numero))

    # Método para realizar uma reserva
    def realizar_reserva(self):
        numero_quarto = self.reserva_input.text()
        self.cursor.execute("SELECT disponivel FROM quartos WHERE numero = ?", (numero_quarto,))
        resultado = self.cursor.fetchone()

        if resultado and resultado[0] == 1:
            # O quarto está disponível
            self.cursor.execute("UPDATE quartos SET disponivel = 0 WHERE numero = ?", (numero_quarto,))
            self.conexao.commit()
            self.atualizar_listas_quartos()
            self.mostrar_mensagem("Reserva Efetuada", f"Quarto {numero_quarto} reservado com sucesso!")
        else:
            self.mostrar_mensagem("Erro", f"O quarto {numero_quarto} não está disponível.")

    # Método para realizar o checkout de um quarto ocupado
    def realizar_checkout(self):
        current_item = self.quartos_ocupados_list.currentItem()
        
        if current_item:
            numero_quarto = current_item.text()
            self.cursor.execute("UPDATE quartos SET disponivel = 1 WHERE numero = ?", (numero_quarto,))
            self.conexao.commit()
            self.atualizar_listas_quartos()
            self.mostrar_mensagem("Checkout Efetuado", f"Checkout do quarto {numero_quarto} realizado com sucesso!")
        else:
            self.mostrar_mensagem("Erro", "Selecione um quarto ocupado para fazer o checkout.")

    # Método para exibir uma mensagem de alerta
    def mostrar_mensagem(self, titulo, mensagem):
        mensagem_box = QMessageBox(self)
        mensagem_box.setWindowTitle(titulo)
        mensagem_box.setText(mensagem)
        mensagem_box.setStandardButtons(QMessageBox.Ok)
        mensagem_box.exec()

    # Método para inserir quartos de teste no banco de dados
    def inserir_quartos_teste(self):
        # Inserir quartos de teste
        for numero_quarto in range(1, 11):
            self.cursor.execute("INSERT INTO quartos (numero, disponivel) VALUES (?, 1)", (numero_quarto,))
        self.conexao.commit()

# Ponto de entrada da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sistema_reserva_hotel = SistemaReservaHotel()
    sistema_reserva_hotel.show()
    sys.exit(app.exec())
