import sys
import string
import secrets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QCheckBox, QPushButton
from PySide6.QtCore import Qt
import qdarktheme

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 350, 300)

        # UI Setup
        panel = QWidget()
        self.setCentralWidget(panel)
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Widgets
        self.output = QLineEdit(self)
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Generated password...")
        self.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.output)

        self.caps = QCheckBox("Include Capital Letters (A-Z)", self)
        self.caps.setChecked(True)
        layout.addWidget(self.caps)

        self.nums = QCheckBox("Include Numbers (0-9)", self)
        self.nums.setChecked(True)
        layout.addWidget(self.nums)

        self.syms = QCheckBox("Include Symbols (!@#$...)", self)
        self.syms.setChecked(True)
        layout.addWidget(self.syms)

        self.btn = QPushButton("Generate", self)
        self.btn.setMinimumHeight(40)
        self.btn.clicked.connect(self.create_password)
        layout.addWidget(self.btn)

    def create_password(self):
        pool = string.ascii_lowercase
        
        if self.caps.isChecked():  pool += string.ascii_uppercase
        if self.nums.isChecked():  pool += string.digits
        if self.syms.isChecked():  pool += string.punctuation

        res = "".join(secrets.choice(pool) for _ in range(16))
        self.output.setText(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark")
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())