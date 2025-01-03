import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QUrl, Qt, QPropertyAnimation, QSize
from gui.main_window import MainWindow
from gui.splash_screen import SplashScreen

def main():
    # Initialize application
    app = QApplication(sys.argv)
    
    # Create and show splash screen
    splash = SplashScreen()
    splash.show()
    
    # Create main window (but don't show it yet)
    window = MainWindow()
    
    def finish_splash():
        splash.finish(window)
        window.show()
        window.fade_in()  # Start fade-in animation
    
    # Single timer for the whole sequence
    QTimer.singleShot(1500, finish_splash)
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
