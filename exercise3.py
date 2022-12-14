
from library import Renderer, color, V2, V3
from shaders import fragmentShader, flat, glow, textureShader, flatNtex
from texture import Texture
import random

width = 500
height = 500

rend = Renderer(width, height)

rend.active_shader = flatNtex
rend.active_texture = Texture("./models/watermelon.bmp")


rend.glLoadModel("./models/watermelon.obj", 
                 translate= V3(width/2, height/5, 0), 
                 rotate = V3(0, 0, 0),
                 scale= V3(700, 700, 700))

rend.glFinish("outputs/output.bmp")

