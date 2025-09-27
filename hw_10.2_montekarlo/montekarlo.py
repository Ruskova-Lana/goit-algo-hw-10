import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# ---------------------------
# 1. Метод Монте-Карло
# ---------------------------
N = 100000  # кількість випадкових точок
x_rand = np.random.uniform(a, b, N)  # випадкові точки
y_rand = f(x_rand)

# оцінка інтеграла: середнє значення функції * довжина інтервалу
monte_carlo_result = (b - a) * np.mean(y_rand)

# ---------------------------
# 2. Аналітичне обчислення
# ---------------------------
# Інтеграл від x^2 = x^3/3
analytic_result = (b**3)/3 - (a**3)/3

# ---------------------------
# 3. Перевірка через quad
# ---------------------------
quad_result, error = quad(f, a, b)

# ---------------------------
# Вивід результатів
# ---------------------------
print(f"Метод Монте-Карло: {monte_carlo_result:.5f}")
print(f"Аналітичний результат: {analytic_result:.5f}")
print(f"Результат функції quad: {quad_result:.5f}, похибка: {error:.2e}")

# ---------------------------
# Візуалізація
# ---------------------------
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки для наочності (невелика підмножина)
sample_x = np.random.uniform(a, b, 500)
sample_y = np.random.uniform(0, max(y), 500)
ax.scatter(sample_x, sample_y, s=5, color='blue', alpha=0.4)

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f"Інтеграл f(x) = x^2 від {a} до {b}")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.grid()
plt.show()
