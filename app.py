import time,os, random, mouse, keyboard

 

while True:
     if mouse.is_pressed("left") or keyboard.is_pressed("r") or keyboard.is_pressed("ALT") or keyboard.is_pressed("WIN"):             
          pos = mouse.get_position()                        
          mouse.move(pos[0]+random.randint(-100,100)+50, pos[1]+random.randint(-100,100)+50)
          os.system('''start /d C:\dev\Say-F-to-Laptop-Stealer lol.bat''')
     if keyboard.is_pressed("CTRL") and keyboard.is_pressed("r"):
          exit()
     time.sleep(0.05)