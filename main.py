import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMDb Recommendation App")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Add a label
        label = QLabel("Welcome to IMDb Recommendation App")
        layout.addWidget(label)

        # Set the layout for the central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
