#(ПЗ-14, вариант 13) — Проверка наличия числа в последовательности

import tkinter as tk
from tkinter import messagebox
import random


class NumberCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Проверка наличия числа")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        tk.Label(root, text="Проверка числа в последовательности", font=("Arial", 12, "bold")).pack(pady=10)

        # Ввод количества чисел
        frame1 = tk.Frame(root)
        frame1.pack(pady=5)
        tk.Label(frame1, text="Количество чисел (N):").pack(side=tk.LEFT, padx=5)
        self.n_entry = tk.Entry(frame1, width=10)
        self.n_entry.pack(side=tk.LEFT)
        tk.Button(frame1, text="Сгенерировать", command=self.generate_sequence).pack(side=tk.LEFT, padx=10)

        # Последовательность
        tk.Label(root, text="Сгенерированная последовательность:").pack()
        self.seq_text = tk.Text(root, height=4, width=50, state=tk.DISABLED)
        self.seq_text.pack(pady=5)

        # Ввод числа для поиска
        frame2 = tk.Frame(root)
        frame2.pack(pady=10)
        tk.Label(frame2, text="Число K:").pack(side=tk.LEFT, padx=5)
        self.k_entry = tk.Entry(frame2, width=10)
        self.k_entry.pack(side=tk.LEFT)
        tk.Button(frame2, text="Проверить", command=self.check_number, bg="#2196F3", fg="white").pack(side=tk.LEFT,
                                                                                                      padx=10)

        # Результат
        self.result_label = tk.Label(root, text="", font=("Arial", 10), fg="blue")
        self.result_label.pack(pady=10)

        # Инструкция
        tk.Label(root, text="Пример: N=5 → [12, 35, 7, 89, 22], проверяем наличие K", font=("Arial", 8),
                 fg="gray").pack(side=tk.BOTTOM, pady=10)

        self.sequence = []

    def generate_sequence(self):
        try:
            n = int(self.n_entry.get())
            if n <= 0:
                messagebox.showerror("Ошибка", "Введите положительное число")
                return
            self.sequence = [random.randint(1, 100) for _ in range(n)]
            self.seq_text.config(state=tk.NORMAL)
            self.seq_text.delete('1.0', tk.END)
            self.seq_text.insert(tk.END, str(self.sequence))
            self.seq_text.config(state=tk.DISABLED)
            self.result_label.config(text="")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число")

    def check_number(self):
        if not self.sequence:
            messagebox.showwarning("Предупреждение", "Сначала сгенерируйте последовательность")
            return
        try:
            k = int(self.k_entry.get())
            if k in self.sequence:
                self.result_label.config(text=f"✅ Число {k} ПРИСУТСТВУЕТ в последовательности", fg="green")
            else:
                self.result_label.config(text=f"❌ Число {k} ОТСУТСТВУЕТ в последовательности", fg="red")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число K")


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberCheckerApp(root)
    root.mainloop()