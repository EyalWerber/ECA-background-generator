from PIL import Image, ImageDraw
import math
import ECA_font_5_random_pillow


pingy = ECA_font_5_random_pillow.main(90)
im= Image.new("RGB" ,(len(pingy[0]),len(pingy)),(0,0,0))
draw=ImageDraw.Draw(im)

def gradient_color(ECA_matrix):
  sin_prox= 0
  cos_prox = 0
  gradient = 0
  invert = ' '

  for j in range(len(pingy[0])):
    for i in range(len(pingy)):
      if pingy[i][j] == invert: #'▓' or ' '

        draw.point((j,i), fill=(int(255*math.e(sin_prox)),int(120*math.cos(cos_prox)),255*gradient))
        if j<(len(pingy[0])/2):
          gradient+=0.01
        else:
          invert = '▓'

          gradient-=0.003
        cos_prox += 0.0001

      sin_prox += 0.1
    print((j/len(pingy[0])*100),'%')


def rules(ECA_matrix):
  error_blue_meter =0
  error_green_meter =0
  invert = '▓'

  for j in range(len(pingy[0])):
    for i in range(len(pingy)):
      
      if pingy[i][j] == invert: #'▓' or ' '
        try:  
          if pingy[j][i+2] == ' ' or pingy[i-2] == ' ':

            draw.point((j,i), fill=(255,0,0))
          else:
            draw.point((j,i), fill=(255,120,0))
        except IndexError as e:
          draw.point((j,i), fill=(255,0,0))
    print((j/len(pingy[0])*100),'%')


rules(pingy)

im.show()

im.save("trial.png",format="PNG")