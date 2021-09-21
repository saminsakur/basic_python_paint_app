from tkinter import (
    Tk,
    Button,
    Frame,
    Canvas,
    W,
    E,
    X,
    filedialog,
    messagebox,
    colorchooser,
)
import PIL.Image
from PIL import ImageDraw

HEIGHT, WIDTH = 500, 500
CENTER = WIDTH // 2
WHITE = (255, 255, 255)


class AppGUI:
    def __init__(self):

        self.window = Tk()
        self.window.title("Simple Paint App")

        self.brush_width = 15
        self.curcolor = "#000000"

        self.cnv = Canvas(self.window, width=WIDTH - 10, height=HEIGHT - 10, bg="white")
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)

        self.btn_frame = Frame(self.window)
        self.btn_frame.pack(fill=X)

        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        self.clear_btn = Button(self.btn_frame, text="Clear", command=self.clear)
        self.clear_btn.grid(row=0, column=1, sticky=W + E)

        self.save_btn = Button(self.btn_frame, text="Save", command=self.save)
        self.save_btn.grid(row=0, column=2, sticky=W + E)

        self.brush_plus_btn = Button(self.btn_frame, text="B+", command=self.brush_plus)
        self.brush_plus_btn.grid(row=0, column=0, sticky=W + E)

        self.brush_minus_btn = Button(
            self.btn_frame, text="B-", command=self.brush_minus
        )
        self.brush_minus_btn.grid(row=1, column=0, sticky=W + E)

        self.color_btn = Button(
            self.btn_frame, text="Change Color", command=self.pick_color
        )
        self.color_btn.grid(row=1, column=1, sticky=W + E)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def paint(self, e):
        x0, y0 = (e.x - 1), (e.y - 1)
        x1, y1 = (e.x + 1), (e.y + 1)

        self.cnv.create_rectangle(
            x0,
            y0,
            x1,
            y1,
            outline=self.curcolor,
            fill=self.curcolor,
            width=self.brush_width,
        )
        self.draw.ellipse(
            [x0, y0, x1 + self.brush_width, y1 + self.brush_width],
            outline=self.curcolor,
            fill=self.curcolor,
            width=self.brush_width,
        )

    def clear(self):
        self.cnv.delete("all")
        self.draw.rectangle([0, 0, 100, 100], fill="white")

    def save(self):
        filename = filedialog.asksaveasfilename(
            initialfile="untitled.png",
            defaultextension="png",
            filetypes=[("PNG", "JPG"), ("*.png", "*.jpg")],
        )
        if filename != "":
            self.image.save(filename)

    def brush_plus(self):
        self.brush_width += 1

    def brush_minus(self):
        if self.brush_width > 1:
            self.brush_width -= 1

    def pick_color(self):
        _, self.curcolor = colorchooser.askcolor(title="Choose A Color")

    def on_close(self):
        answer = messagebox.askyesnocancel(
            "Quit", "Do you want to save this file as any format?", parent=self.window
        )
        if answer is not None:
            if answer:
                self.save()
            self.window.destroy()
            exit(0)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = AppGUI()
    app.run()
