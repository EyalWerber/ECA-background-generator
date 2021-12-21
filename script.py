from PIL import Image, ImageDraw
import math
import ECA_font_5_random_pillow


pingy = ECA_font_5_random_pillow.main(90)
im= Image.new("RGB" ,(len(pingy[0]),len(pingy)),(0,0,0))
draw=ImageDraw.Draw(im)

def rules(ECA_matrix):
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
    # print((j/len(pingy[0])*100),'%')

if __name__ == '__main__':

  rules(pingy)
  im.save("output.png",format="PNG")
  with open('rules.txt','r') as f: 
    prompt = f.read()
  markdown = f"![photo](./output.png) \n {prompt}"
  open("./README.md", "w", encoding="utf-8").write(markdown)
  