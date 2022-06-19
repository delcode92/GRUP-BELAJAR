from tkinter import Canvas, Tk, PhotoImage, NW
import time

WIDTH = 600
HEIGHT = 600
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

i = 1
while True:
    
    if i==1:
        for j in range(10):
            j+=1
            
            photo_image = PhotoImage(file=f'game/freedinosprite/png/Walk ({j}).png')
            my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)
            
            window.update()
            time.sleep(0.03)
    

    photo_image = PhotoImage(file=f'game/freedinosprite/png/Run ({i}).png')
    my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)


    
    i+=1

    if i== 9:
        i=1

    window.update()
    time.sleep(0.03)

window.mainloop()