import ion
from ion import *
from math import *
from kandinsky import *
from time import *
draw_string("Bienvenue sur Clicker",55,60)
draw_string("by Tom Mathieu",90,120)
draw_string("Chargement...",90,180)
sleep(1)
fill_rect(0,0,1200,1200,'white')
tpy = 0
cc = 0
o =6
tps = 0.5
while o==6:
  cp = str(cc) 
  draw_string("Vous avez",100,0)
  draw_string("euros",250,0)
  draw_string(cp,195,0)
  draw_string("appuyez sur OK pour gagner plus",5,100) 
  draw_string("d'argent par secondes",5,120)
  if ion.keydown(KEY_LEFT):
      print("ots")
      cc = cc + 1
      sleep(tps)
  elif ion.keydown(KEY_OK):
      if cc > 20:
        draw_string("test",0,0)
        #tpy = tps * 0.1
        #tps = tps - tpy
        cc = cc - 20
        sleep(1)
      else:
        draw_string("654",0,0)
  else:
     print("n") 
     return
