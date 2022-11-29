import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.geometry('1305x780')
root.title("Dashboard")
root.configure(bg='#fcffe8')

top_bg = tk.Canvas(root, width=1305, height=60, bg='#232421', highlightthickness=0).place(x=0, y=0)
tk.Label(top_bg, text='Dashboard', font='Montserrat 25', bg='#1b2838', fg='white').place(x=15, y=3)


class Rack(tk.Canvas):
    def __init__(self, child, x, y, transform = False, color='blue'):
        tk.Canvas.__init__(self, child)
        self.width = 96
        self.height = 288
        self.config(width=self.width, height=self.height)
        if transform:
            temp = self.width
            self.width = self.height
            self.height = temp
            self.config(width=self.width, height=self.height)
        self.x = x
        self.y = y
        self.place(x=x, y=y)
        if color == 'blue':
            self.config(bg="#b4caed")
        else:
            self.config(bg='#ffff8e')
        
            
class Idea(Rack):
   pass
Rack(top_bg, 85, 85)
Rack(top_bg, 181, 85, transform=True, color='black')
root.mainloop()