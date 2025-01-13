from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QLabel, QWidget, QFileDialog
)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифрование")
        self.setFixedSize(400, 200)

        # Main layout
        main_layout = QVBoxLayout()

        # Buttons for encryption and decryption
        button_layout = QHBoxLayout()
        self.encrypt_button = QPushButton("ЗАШИФРОВАТЬ")
        self.encrypt_folder_button = QPushButton("ЗАШИФРОВАТЬ папку")
        self.decrypt_button = QPushButton("ДЕШИФРОВАТЬ")

        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.encrypt_folder_button)
        button_layout.addWidget(self.decrypt_button)

        main_layout.addLayout(button_layout)

        # Checkboxes
        self.delete_original_checkbox = QCheckBox("Удалять оригинал")
        self.create_vault_checkbox = QCheckBox("Создать VAULT")

        main_layout.addWidget(self.delete_original_checkbox)
        main_layout.addWidget(self.create_vault_checkbox)

        # Save folder label
        self.save_folder_label = QLabel("ПАПКА ДЛЯ СОХРАНЕНИЯ")
        main_layout.addWidget(self.save_folder_label)

        # Add functionality for selecting save folder
        self.save_folder_button = QPushButton("Выбрать папку")
        self.save_folder_button.clicked.connect(self.select_save_folder)
        main_layout.addWidget(self.save_folder_button)

        self.setLayout(main_layout)

    def select_save_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        if folder:
            self.save_folder_label.setText(f"ПАПКА ДЛЯ СОХРАНЕНИЯ: {folder}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
