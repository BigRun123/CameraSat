import time
from turtle import*
from TCS34087 import TCS34087

screen = Screen()
screen.setup(700, 600)

Light = TCS34087(0x29)

if Light.TCS34087_init() == 1:
    print("TCS34087 initialization error!!")
    
else:
    print("TCS34087 initialization success!!")

while True:
    Light.Get_RGBData()
    Light.GetRGB888()
    Light.GetRGB565()
    
    screen.bgcolor("#%02x%02x%02x" % (Light.RGB888_R,Light.RGB888_G,Light.RGB888_B))
    
    print("R: %d "%Light.RGB888_R, end = "")
    print("G: %d "%Light.RGB888_G, end = "")
    print("B: %d "%Light.RGB888_B, end = "") 
    print("C: %#x "%Light.C, end = "")
    print("RGB565: %#x "%Light.RG565, end ="")
    print("RGB888: %#x "%Light.RGB888, end = "")   
    print("LUX: %d "%Light.Get_Lux(), end = "") 
    print("CT: %dK "%Light.Get_ColorTemp(), end ="")
    print("INT: %d "%Light.GetLux_Interrupt())