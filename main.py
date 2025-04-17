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

# 运行主循环
root.mainloop()
