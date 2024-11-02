pip install pillow pygame

from tkinter import Tk, Label
from PIL import Image, ImageTk
import pygame
import time

# Инициализация окна
window = Tk()
window.title("Гачи-картинка и звук")
window.geometry("600x400")  # Установите размер окна

# Загрузка изображения
image_path = "gachi_image.jpg"  # Укажите путь к изображению
image = Image.open(image_path)
image = image.resize((600, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Отображение изображения в окне
label = Label(window, image=photo)
label.pack()

# Инициализация pygame для воспроизведения звука
pygame.mixer.init()
sound_path = "aaa_sound.mp3"  # Укажите путь к звуковому файлу "ааааа"
pygame.mixer.music.load(sound_path)

# Функция для воспроизведения звука
def play_sound():
    pygame.mixer.music.play()
    time.sleep(5)  # Дайте звуку немного времени для воспроизведения

# Воспроизведение звука при запуске окна
window.after(1000, play_sound)  # Запуск через секунду после открытия окна

# Запуск основного цикла окна
window.mainloop()
