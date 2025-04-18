# main.py
import tkinter as tk

def show_message():
    label.config(text="Hello, GitHub Actions!")

# 创建主窗口
root = tk.Tk()
root.title("GitHub Actions 测试软件")
root.geometry("300x200")

# 添加标签
label = tk.Label(root, text="点击按钮查看消息", font=("Arial", 12))
label.pack(pady=20)

# 添加按钮
button = tk.Button(root, text="点击我", command=show_message, font=("Arial", 12))
button.pack(pady=10)

# 添加输入框和提交按钮
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

def submit_text():
    label.config(text=f"你输入了: {entry.get()}")
    
submit_btn = tk.Button(root, text="提交", command=submit_text, font=("Arial", 12))
submit_btn.pack(pady=5)

# 添加复选框
check_var = tk.IntVar()
check = tk.Checkbutton(root, text="启用高级功能", variable=check_var, font=("Arial", 12))
check.pack(pady=5)

# 添加状态栏
status = tk.Label(root, text="就绪", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# 运行主循环
root.mainloop()
