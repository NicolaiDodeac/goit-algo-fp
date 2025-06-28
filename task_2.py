import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, length, angle, depth, max_depth):
    if depth > max_depth:
        return

    # Реалізація логіки візуалізації фракталу
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    plt.plot([x, x_end], [y, y_end], color='brown')

    new_length = length * 0.7
    angle_left = angle + np.pi / 4
    angle_right = angle - np.pi / 4

    draw_branch(x_end, y_end, new_length, angle_left, depth + 1, max_depth)
    draw_branch(x_end, y_end, new_length, angle_right, depth + 1, max_depth)

if __name__ == '__main__':
    try:
        user_depth = int(input("Вкажіть рівень рекурсії (4 - 15): "))
        if user_depth > 15:
            print("Занадто велике значення! Встановлюємо максимальний рівень = 15.")
            user_depth = 15
        elif user_depth < 4:
            print("Занадто малий рівень! Встановлюємо мінімальний рівень = 4.")
            user_depth = 4
    except ValueError:
        print("Некоректне значення! Встановлюємо рівень за замовчуванням = 8.")
        user_depth = 8

# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')

start_x, start_y = 0, 0
initial_length = 100
initial_angle = np.pi / 2

draw_branch(start_x, start_y, initial_length, initial_angle, 1, user_depth)

plt.show()