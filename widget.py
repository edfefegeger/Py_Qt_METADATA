import os
import subprocess
from pathlib import Path
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide2.QtCore import QFile, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtUiTools import QUiLoader
import sys
from PySide2.QtWidgets import QFileDialog
class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        self.setup_ui()
        self.setup_background()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

    def setup_ui(self):
        # Добавляем обработчик сигнала кнопки
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def setup_background(self):
        # Создаем QLabel для отображения изображения
        self.background_label = QLabel(self)

        # Загружаем изображение из файла
        image_path = os.path.join(os.path.dirname(__file__), "IMG_8222.JPG")
        pixmap = QPixmap(image_path)

        # Устанавливаем изображение в QLabel
        self.background_label.setPixmap(pixmap)

        # Добавляем QLabel в качестве виджета-потомка
        self.background_label.lower()

    def resizeEvent(self, event):
        # Обновляем геометрию background_label при изменении размера виджета
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        event.accept()

    def embed_text_in_video(self, video_path, text_to_embed):
        try:
            video_filename, video_extension = os.path.splitext(os.path.basename(video_path))

            # Формируем путь к выходному видео с префиксом "COMPLETED"
            output_path = f"{video_filename}_COMPLETED{video_extension}"

            # Используем ffmpeg для внедрения текста в метаданные видео
            subprocess.run([
                "ffmpeg",
                "-i", video_path,
                "-c", "copy",
                "-metadata", f"description={text_to_embed}",
                output_path
            ], check=True)

            print("Текст успешно внедрен в метаданные видео.")
        except subprocess.CalledProcessError as e:
            print(f"Произошла ошибка: {e}")
    def on_button_clicked(self):
        # Открываем диалог выбора файла для видео
        video_dialog = QFileDialog()
        video_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mkv);;All Files (*)")
        video_dialog.setFileMode(QFileDialog.ExistingFile)

        if video_dialog.exec_():
            # Получаем путь к выбранному видеофайлу
            selected_video_files = video_dialog.selectedFiles()
            video_path = selected_video_files[0]

            # Открываем диалог выбора файла для текста
            text_dialog = QFileDialog()
            text_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")
            text_dialog.setFileMode(QFileDialog.ExistingFile)

            if text_dialog.exec_():
                # Получаем путь к выбранному текстовому файлу
                selected_text_files = text_dialog.selectedFiles()
                text_file_path = selected_text_files[0]

                # Обновляем текстовые поля с путями к видео и текстовому файлу
                self.ui.textEdit_2.setPlainText(video_path)
                self.ui.textEdit.setPlainText(text_file_path)

                # Вызываем метод для внедрения текста в видео
                with open(text_file_path, 'r') as text_file:
                    text_to_embed = text_file.read()
                    self.embed_text_in_video(video_path, text_to_embed)



if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # Устанавливаем атрибут перед созданием QApplication
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())


