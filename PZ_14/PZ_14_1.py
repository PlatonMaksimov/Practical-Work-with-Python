import tkinter as tk
from tkinter import ttk, messagebox


class ZooAppForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Заявка на работу в зоопарке")
        self.root.geometry("500x620")
        self.root.resizable(False, False)

        #Заголовок
        tk.Label(root, text="Форма заявки на работу в зоопарке",
                 font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Пожалуйста, заполните форму. Обязательные поля помечены *",
                 font=("Arial", 9)).pack(pady=(0, 15))

        #Основной фрейм
        main_frame = tk.Frame(root)
        main_frame.pack(padx=20, fill="both", expand=True)

        #Контактная информация
        tk.Label(main_frame, text="Контактная информация", font=("Arial", 10, "bold")).grid(row=0, column=0,
                                                                                            columnspan=2, sticky="w",
                                                                                            pady=(0, 5))

        tk.Label(main_frame, text="Имя *").grid(row=1, column=0, sticky="w", pady=2)
        self.name_entry = tk.Entry(main_frame, width=30)
        self.name_entry.grid(row=1, column=1, sticky="w", pady=2)

        tk.Label(main_frame, text="Телефон").grid(row=2, column=0, sticky="w", pady=2)
        self.phone_entry = tk.Entry(main_frame, width=30)
        self.phone_entry.grid(row=2, column=1, sticky="w", pady=2)

        tk.Label(main_frame, text="Email *").grid(row=3, column=0, sticky="w", pady=2)
        self.email_entry = tk.Entry(main_frame, width=30)
        self.email_entry.grid(row=3, column=1, sticky="w", pady=2)

        #Персональная информация
        tk.Label(main_frame, text="Персональная информация", font=("Arial", 10, "bold")).grid(row=4, column=0,
                                                                                              columnspan=2, sticky="w",
                                                                                              pady=(10, 5))

        tk.Label(main_frame, text="Возраст *").grid(row=5, column=0, sticky="w", pady=2)
        self.age_spin = tk.Spinbox(main_frame, from_=16, to=100, width=28)
        self.age_spin.grid(row=5, column=1, sticky="w", pady=2)

        tk.Label(main_frame, text="Пол").grid(row=6, column=0, sticky="w", pady=2)
        self.gender_var = tk.StringVar(value="Женщина")
        tk.Radiobutton(main_frame, text="Женщина", variable=self.gender_var, value="Женщина").grid(row=6, column=1,
                                                                                                   sticky="w")
        tk.Radiobutton(main_frame, text="Мужчина", variable=self.gender_var, value="Мужчина").grid(row=7, column=1,
                                                                                                   sticky="w")

        tk.Label(main_frame, text="Личные качества").grid(row=8, column=0, sticky="nw", pady=2)
        self.qualities_text = tk.Text(main_frame, width=30, height=4)
        self.qualities_text.grid(row=8, column=1, pady=2)

        #Любимые животные
        tk.Label(main_frame, text="Выберите ваших любимых животных", font=("Arial", 10, "bold")).grid(row=9, column=0,
                                                                                                      columnspan=2,
                                                                                                      sticky="w",
                                                                                                      pady=(10, 5))

        animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
        self.animal_vars = {}
        animal_frame = tk.Frame(main_frame)
        animal_frame.grid(row=10, column=0, columnspan=2, sticky="w")

        for i, animal in enumerate(animals):
            var = tk.BooleanVar()
            self.animal_vars[animal] = var
            tk.Checkbutton(animal_frame, text=animal, variable=var).grid(row=i // 2, column=i % 2, sticky="w")

        #Кнопка отправки
        tk.Button(main_frame, text="Отправить информацию", command=self.submit, bg="#4CAF50", fg="white", padx=10,
                  pady=5).grid(row=11, column=0, columnspan=2, pady=20)

    def submit(self):
        #Проверка обязательных полей
        if not self.name_entry.get().strip():
            messagebox.showerror("Ошибка", "Поле 'Имя' обязательно для заполнения")
            return
        if not self.email_entry.get().strip():
            messagebox.showerror("Ошибка", "Поле 'Email' обязательно для заполнения")
            return
        if not self.age_spin.get().strip():
            messagebox.showerror("Ошибка", "Поле 'Возраст' обязательно для заполнения")
            return

        #Сбор данных
        animals_selected = [animal for animal, var in self.animal_vars.items() if var.get()]

        info = f"Имя: {self.name_entry.get()}\n"
        info += f"Телефон: {self.phone_entry.get()}\n"
        info += f"Email: {self.email_entry.get()}\n"
        info += f"Возраст: {self.age_spin.get()}\n"
        info += f"Пол: {self.gender_var.get()}\n"
        info += f"Личные качества: {self.qualities_text.get('1.0', tk.END).strip()}\n"
        info += f"Любимые животные: {', '.join(animals_selected) if animals_selected else 'не выбраны'}"

        messagebox.showinfo("Данные заявки", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZooAppForm(root)
    root.mainloop()