# File: addressbook.py
# Author: Alex Bae, Galen Forbes-Roberts, Josue Bautista
# Date: 2/26/21
# Description: Code for a program that displays a clock

import math
import datetime
import tkinter as tk


class Display_Clock:
    def __init__(self):
        self.window = tk.Tk()  # Create a window
        self.window.title("Current Time")  # Set a title

        # declared necessary variables
        self.canvas_size = 200
        self.centerx = self.canvas_size//2
        self.centery = self.canvas_size//2
        self.clock_radius = 0.8*0.5*self.canvas_size
        self.sec_hand_length = 0.8*self.clock_radius
        self.min_hand_length = 0.65*self.clock_radius
        self.hour_hand_length = 0.5*self.clock_radius
        self.sleep_time = 1000

        # create and pack canvas
        self.canvas = tk.Canvas(
            self.window, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()
        # create the circle for clock
        self.canvas.create_oval(
            20, 20, 2*self.clock_radius + 20, 2*self.clock_radius + 20)
        # create the texts for numbers and position them
        self.canvas.create_text(100, 27, text='12', font='Times 10')
        self.canvas.create_text(177, 100, text='3', font='Times 10')
        self.canvas.create_text(100, 173, text='6', font='Times 10')
        self.canvas.create_text(26, 100, text='9', font='Times 10')

        frame = tk.Frame(self.window)
        frame.pack()
        self.text = tk.StringVar()
        self.text.set('Stop')
        self.start_stop_button = tk.Button(
            frame, text=self.text.get(), command=self.Stop)
        self.start_stop_button.grid(row=1, column=1)
        quit_button = tk.Button(frame, text='Quit', command=self.Quit)
        quit_button.grid(row=1, column=2)

        self.isStopped = False
        self.animate()

        self.window.mainloop()

    def Stop(self):
        self.isStopped = True
        self.start_stop_button['text'] = 'Start'
        self.start_stop_button['command'] = self.Start
        self.get_time()
        self.draw_lines()
        self.canvas.after_cancel(self.timer)

    def get_time(self):
        self.current_time = datetime.datetime.now()
        self.hour = self.current_time.hour
        self.minute = self.current_time.minute
        self.second = self.current_time.second    
        self.endx_h = self.centerx + self.hour_hand_length * \
            math.sin((self.hour/12)*(2*math.pi))
        self.endy_h = self.centery - self.hour_hand_length * \
            math.cos((self.hour/12)*(2*math.pi))
        self.endx_m = self.centerx + self.min_hand_length * \
            math.sin((self.minute/60)*(2*math.pi))
        self.endy_m = self.centery - self.min_hand_length * \
            math.cos((self.minute/60)*(2*math.pi))
        self.endx_s = self.centerx + self.sec_hand_length * \
            math.sin((self.second/60)*(2*math.pi))
        self.endy_s = self.centery - self.sec_hand_length * \
            math.cos((self.second/60)*(2*math.pi))
        if int(self.hour) > 12:
            self.hour -= 12
        self.time = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
        self.canvas.create_text(self.centerx, self.centery + self.clock_radius + 10, text = self.time, tags = 'hands') 

    def Start(self):
        self.isStopped = False
        self.start_stop_button['text'] = 'Stop'
        self.start_stop_button['command'] = self.Stop
        self.animate()

    def animate(self):
        self.canvas.delete('hands')
        self.get_time()
        self.draw_lines()
        self.timer = self.canvas.after(self.sleep_time, self.animate)

    def draw_lines(self):
        self.canvas.create_line(
            self.centerx, self.centery, self.endx_h, self.endy_h, fill="green", tags="hands")
        self.canvas.create_line(
            self.centerx, self.centery, self.endx_m, self.endy_m, fill="blue", tags="hands")
        self.canvas.create_line(
            self.centerx, self.centery, self.endx_s, self.endy_s, fill="red", tags="hands")

    def Quit(self):
        self.window.destroy()


if __name__ == "__main__":
    Display_Clock()
