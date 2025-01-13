from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QPushButton, 
    QCheckBox, QLabel, QWidget, QFileDialog, QStatusBar
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Безопасное шифрование файлов")
        self.setFixedSize(500, 250)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: 'Segoe UI', Arial;
            }
            QPushButton {
                background-color: #0d6efd;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                min-width: 150px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #0b5ed7;
            }
            QCheckBox {
                padding: 10px;
                font-size: 14px;
            }
        """)

        # Main layout with margins
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Title
        title = QLabel("Шифрование файлов")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Buttons layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.encrypt_button = QPushButton("🔒 Зашифровать")
        self.encrypt_folder_button = QPushButton("📁 Зашифровать папку")
        self.decrypt_button = QPushButton("🔓 Дешифровать")
        
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.encrypt_folder_button)
        button_layout.addWidget(self.decrypt_button)

        main_layout.addLayout(button_layout)

        # Checkbox with modern style
        self.delete_original_checkbox = QCheckBox("🗑️ Удалять оригинал")
        self.delete_original_checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
        """)
        main_layout.addWidget(self.delete_original_checkbox)

        # Status bar
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("color: #666;")
        self.status_bar.showMessage("Готов к работе")
        main_layout.addWidget(self.status_bar)

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
