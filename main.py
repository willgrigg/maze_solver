from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, background="white", width=width, height=height)
        self.canvas.pack(fill=BOTH)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False
        
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    window = Window(800, 600)
    window.wait_for_close()

main()
