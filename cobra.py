import keyboard
from tkinter import Tk, Canvas

class WindowSnakeGame(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("snake game")
        self.geometry("600x500")
        self.resizable(False,False)
        self.configure(background="black")
        
        # "r" faz com que o python não aceite comando na linha como "/n"
        self.icon = r"C:\Users\Pedro\Downloads\snake.ico"
        self.iconbitmap(self.icon)
        
        self.pixel_x = 20
        self.pixel_y = 20
        self.pixel_size = 20
        
        self.canvas = Canvas(self, width=600, height=500, bg="black")
        self.canvas.pack()
        
        self.snake = self.canvas.create_rectangle(self.pixel_x, self.pixel_y, 
                                             self.pixel_x + self.pixel_size, 
                                             self.pixel_y + self.pixel_size, 
                                             fill = "green")
        
        self.bind("<Key>", self.move_snake)
        
    def move_snake(self, e):
        if keyboard.is_pressed("Right"):
            self.pixel_x += 10
            self.change_snake_position()
        elif keyboard.is_pressed("up"):
            self.pixel_y -= 10
            self.change_snake_position()
        elif keyboard.is_pressed("left"):
            self.pixel_x -= 10
            self.change_snake_position()
        elif keyboard.is_pressed("down"):
            self.pixel_y += 10
            self.change_snake_position()
            
            
    def change_snake_position(self):
        self.canvas.coords(self.snake, self.pixel_x, self.pixel_y, self.pixel_x + self.pixel_size, self.pixel_y + self.pixel_size)
                           
app = WindowSnakeGame()
app.mainloop()