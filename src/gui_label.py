import tkinter as tk
from tkinter import messagebox
import pandas as pd
from src.utils import save_to_csv

class QueryLabeler:
    def __init__(self, master):
        self.master = master
        self.master.title("Query Labeler")
        
        self.data = pd.read_csv("data/devtest.csv")
        self.current_index = 0
        
        self.query_label = tk.Label(master, text="", wraplength=400)
        self.query_label.pack(pady=10)
        
        self.rewriting_label = tk.Label(master, text="", wraplength=400)
        self.rewriting_label.pack(pady=10)
        
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)
        
        for n in range(1, 5):
            button = tk.Button(self.button_frame, text=str(n), command=lambda x=n: self.label_query(x))
            button.pack(side="left", padx=5)
        
        self.status_var = tk.StringVar(value="未标注")
        tk.Label(master, textvariable=self.status_var).pack(side="bottom", fill="x", padx=10, pady=6)
        
        self.load_query()

    def load_query(self):
        if self.current_index < len(self.data):
            self.query_label.config(text=self.data.iloc[self.current_index]['query'])
            self.rewriting_label.config(text=self.data.iloc[self.current_index]['query_rewriting'])
        else:
            messagebox.showinfo("完成", "所有查询已标注！")
            self.master.quit()

    def label_query(self, number):
        self.data.at[self.current_index, 'label'] = number
        self.status_var.set(f"已标注: {number}")
        self.current_index += 1
        self.load_query()
        save_to_csv(self.data, "data/devtest.csv")

def main():
    root = tk.Tk()
    app = QueryLabeler(root)
    root.mainloop()

if __name__ == "__main__":
    main()