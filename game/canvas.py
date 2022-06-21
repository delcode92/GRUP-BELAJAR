<<<<<<< HEAD
from tkinter import Canvas, Tk, PhotoImage, NW
import time

WIDTH = 1600
HEIGHT = 1200
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
path = "game/freedinosprite/png/"
bg_path = "game/craftpix-516661-free-cartoon-forest-game-backgrounds/PNG/Cartoon_Forest_BG_03/"

background_photo = PhotoImage(file=f'{bg_path}Cartoon_Forest_BG_03.png')
canvas.create_image(0,-70,image=background_photo,anchor=NW)

b = 0
def animate(style:str, img_count:int, reverse:bool=False):
    
    for i in range(img_count):
        
        if reverse:
            i = img_count-i
        elif reverse == False:     
            i+=1

        # global b
        # b-=2
        # canvas.create_image(0,-70,image=background_photo,anchor=NW)

        photo_image = PhotoImage(file=f'{path}{style} ({i}).png')
        canvas.create_image(100,580,image=photo_image,anchor=NW)

        window.update()
        time.sleep(0.03)

while True:
    

    animate("Idle", 10)    
    animate("Walk", 10)    
    animate("Run", 8)    
    animate("Jump", 12)    

    animate("Run", 8)
    animate("Walk", 10)
    animate("Idle", 10)
    animate("Dead", 8)
    animate("Dead", 8, True)

    time.sleep(1)

    
window.mainloop()
=======
from tkinter import Canvas, Tk, PhotoImage, NW
import time

WIDTH = 1600
HEIGHT = 1200
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
path = "game/freedinosprite/png/"
bg_path = "game/craftpix-516661-free-cartoon-forest-game-backgrounds/PNG/Cartoon_Forest_BG_03/"

background_photo = PhotoImage(file=f'{bg_path}Cartoon_Forest_BG_03.png')

b = 0
def animate(style:str, img_count:int, reverse:bool=False):
    
    for i in range(img_count):
        
        if reverse:
            i = img_count-i
        elif reverse == False:     
            i+=1

        # global b
        # b-=2
        canvas.create_image(0,-70,image=background_photo,anchor=NW)

        photo_image = PhotoImage(file=f'{path}{style} ({i}).png')
        canvas.create_image(100,580,image=photo_image,anchor=NW)

        window.update()
        time.sleep(0.03)

while True:
    

    animate("Idle", 10)    
    animate("Walk", 10)    
    animate("Run", 8)    
    animate("Jump", 12)    

    animate("Run", 8)
    animate("Walk", 10)
    animate("Idle", 10)
    animate("Dead", 8)
    animate("Dead", 8, True)

    time.sleep(1)

    
window.mainloop()
>>>>>>> 86adebd20f95887626af2a6198b994837931656b
