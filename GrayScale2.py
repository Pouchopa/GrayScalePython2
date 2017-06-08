#!/usr/bin/env python
import sys
from PIL import Image

param_1= sys.argv[1] 
param_2= sys.argv[2] 
img = Image.open(param_1).convert('LA')
img2 = Image.open(param_2).convert('LA')
img.save('grayscale.png')
img2.save('grayscale2.png')