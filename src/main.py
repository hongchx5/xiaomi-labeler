import tkinter as tk
from tkinter import messagebox
import pandas as pd
from data_loader import load_data, save_data

class DevTestLabeler:
    def __init__(self, master):
        self.master = master
        self.master.title("DevTest Labeler")
        
        self.data = load_data('D:\Dataset\devtest-labeler\data\devtest.csv')
        self.current_index = 0
        
        self.query_label = tk.Label(master, text="")
        self.query_label.pack(pady=10)
        
        self.rewriting_label = tk.Label(master, text="")
        self.rewriting_label.pack(pady=10)
        
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)
        
        for n in range(1, 5):
            button = tk.Button(self.button_frame, text=str(n), command=lambda x=n: self.label_data(x))
            button.pack(side="left", padx=5)
        
        self.update_display()
    
    def update_display(self):
        if self.current_index < len(self.data):
            self.query_label.config(text=f"Query: {self.data.iloc[self.current_index]['query']}")
            self.rewriting_label.config(text=f"Query Rewriting: {self.data.iloc[self.current_index]['query_rewriting']}")
        else:
            messagebox.showinfo("完成", "所有数据已标注！")
            self.master.quit()
    
    def label_data(self, label):
        if self.current_index < len(self.data):
            self.data.at[self.current_index, 'label'] = label
            self.current_index += 1
            save_data(self.data,'D:\Dataset\devtest-labeler\data\devtest.csv')
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = DevTestLabeler(root)
    root.mainloop()