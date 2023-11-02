import sqlite3
import tkinter as tk

# класс главного окна
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
    
    # хранение и инициализация объектов GUI
    def init_main(self):
        self.generate_img = tk.PhotoImage(file='.\\img\\refresh.png')
        btn_generate = tk.Button(self, image=self.generate_img, command=self.generate)
        btn_generate.pack()
        self.text_joke = tk.Text(self, border=1, wrap='word')
        self.text_joke.pack()
    
    def generate(self):
        self.db.c.execute("SELECT joke FROM Jokes ORDER BY RANDOM() LIMIT 1;")
        self.text_joke.delete(0.0, tk.END)
        self.text_joke.insert(0.0, self.db.c.fetchone()[0])

# класс БД
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.c = self.conn.cursor()

if __name__ == '__main__':
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Joke')
    root.geometry('400x400')
    root.resizable(False, False)
    root.mainloop()


