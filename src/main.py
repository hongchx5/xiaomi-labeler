# ...existing code...
import os
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from data_loader import load_data, save_data

# 指定数据文件路径（相对于 src 上一级的 data 目录）
DATA_CSV = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "data", "devtest.csv"))

class DevTestLabeler:
    def __init__(self, master):
        self.master = master
        self.master.title("DevTest Labeler")
        
        # 加载数据（并确保有 label 列）
        self.data = load_data(DATA_CSV)
        if 'label' not in self.data.columns:
            # 在最后添加 label 列（空字符串）
            self.data['label'] = ''
        self.current_index = 0

        # 要显示的字段顺序（按需调整）
        self.fields = [
            "request_id",
            "session_id",
            "domain",
            "query",
            "to_speak",
            "copilot_code",
            "large_model_info",
        ]

        # 创建显示区域
        self.display_frame = tk.Frame(master)
        self.display_frame.pack(padx=10, pady=10, anchor="w")

        try:
            self.master.geometry("1200x700")
        except Exception:
            pass

        # 创建可滚动的显示区域（Canvas + Frame）
        self.display_container = tk.Frame(master)
        self.display_container.pack(padx=10, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.display_container)
        vsb = tk.Scrollbar(self.display_container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # 更新滚动区域
        def _on_frame_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.inner_frame.bind("<Configure>", _on_frame_configure)

        # 鼠标滚轮支持（Windows/Mac/Linux）
        def _on_mousewheel(event):
            if getattr(event, "delta", 0):
                # Windows / Mac
                self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            else:
                # Linux (Button-4/5)
                if event.num == 4:
                    self.canvas.yview_scroll(-1, "units")
                elif event.num == 5:
                    self.canvas.yview_scroll(1, "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        self.canvas.bind_all("<Button-4>", _on_mousewheel)
        self.canvas.bind_all("<Button-5>", _on_mousewheel)

        # 字段标签（可调 wraplength）
        self.field_labels = {}
        wrap_len = 1000
        for f in self.fields:
            tk.Label(self.inner_frame, text=f + ":", font=("Arial", 9, "bold")).pack(anchor="w")
            lbl = tk.Label(self.inner_frame, text="", wraplength=wrap_len, justify="left")
            lbl.pack(anchor="w", padx=10, pady=2)
            self.field_labels[f] = lbl

        # 状态行（显示当前进度）
        self.status_var = tk.StringVar(value="未开始")
        tk.Label(master, textvariable=self.status_var).pack(fill="x", padx=10, pady=(0,5))

        # 按钮区
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)
        
        for n in range(1, 5):
            button = tk.Button(self.button_frame, text=str(n), width=6, command=lambda x=n: self.label_data(x))
            button.pack(side="left", padx=5)
        
        self.update_display()
    
    def update_display(self):
        total = len(self.data)
        if self.current_index < total:
            row = self.data.iloc[self.current_index]
            for f in self.fields:
                val = row.get(f, "")
                # 显示 None/NaN 为空字符串
                if pd.isna(val):
                    val = ""
                self.field_labels[f].config(text=str(val))
            self.status_var.set(f"Index: {self.current_index+1}/{total}    file: {DATA_CSV}")
        else:
            messagebox.showinfo("完成", "所有数据已标注！")
            # 最后也保存一次以防遗漏
            save_data(self.data, DATA_CSV)
            self.master.quit()
    
    def label_data(self, label):
        if self.current_index < len(self.data):
            # 写入 label 到最后一列（列名 'label'）
            self.data.at[self.current_index, 'label'] = label
            # 立即保存
            save_data(self.data, DATA_CSV)
            self.current_index += 1
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = DevTestLabeler(root)
    root.mainloop()
# ...existing code...