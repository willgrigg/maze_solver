from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, background="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
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

    def draw_line(self, fill_color, line) -> None:
        line.draw(fill_color, self.canvas)
        
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1 : Point, point2 : Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, fill_color, canvas : Canvas) -> None:
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y, 
            fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


def main():
    window = Window(800, 600)
    point1 = Point(1, 1)
    point2 = Point(100, 800)
    line1 = Line(point1, point2)
    window.draw_line("red", line1)
    window.wait_for_close()

main()
