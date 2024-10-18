from p5 import *

blue = 70, 130, 180
yellow = 255, 216, 1
greenn = 35, 140, 35

def setup():
  createCanvas(500,400)
  background('white')
  fill(14, 99, 151)
  rect(0, 300, width, 100)
  textStyle(BOLD)
  prompt = Text('b =', (180, 335))
  prompt.fill = yellow
  prompt.size = 50
  prompt2 = Text(' ?', (255, 335))
  prompt2.fill = 255, 255, 255
  prompt2.size = 50
  prompt.draw()
  prompt2.draw()
  textStyle(NORMAL)

def draw():
  default()
  ## TEACHER INPUTS
  a = 60 #must be less than c (leg)
  c = 109 #must be greater than a (hypotenuse)
  ## 
  #$$$
  b = $$0$$
  #Remember the Pythagoras Theorem!
  #$$$
  b, c = c, b 

  green = 135, 199, 101
  c_correct = (b ** 2 - a ** 2) ** 0.5
  start_RA = (100, 75)
  frame_r = frameCount/100
  end_frame = False
  if frame_r > 1:
    frame_r = 1
    noLoop()
    end_frame = True
  r = get_r(a,c_correct, 100)
  triangle_fill = RightTriangle(a, c_correct)
  triangle_fill.draw(start_RA[0], start_RA[1])
  a_end = (start_RA[0], start_RA[1] + a * r)
  a_line = Line(start_RA,a_end)
  a_line.draw()
  
  c_end = (start_RA[0] + c * r * frame_r, start_RA[1])
  c_line = Line(start_RA, c_end)
  if end_frame:
    c_line.strokeWeight = 10
    if c == c_correct:
      c_line.strokecolour = 'green'
      c_line.strokeweight = 6
      success()
      res_text = Text('You did it!', (300,250))
      res_text.fill = '#01BC39'
      res_text.size = 35
      res_text.draw()
    elif c != 0:
      c_line.strokeweight = 6
      c_line.strokecolour = 'red'
      #res_text = Text('Try Again!', (200,300))
      #res_text.fill = 'red'
      #res_text.size = 35
      #res_text.draw()
    
  c_line.draw()

  b_start = a_end
  b_end = (start_RA[0] + c_correct * r, start_RA[1])
  b_line = Line(b_start, b_end)
  b_line.draw()
  #init_triangle = RightTriangle(a, b)
  #init_triangle.draw(100,100)
  #fill
  a_mid = ((start_RA[0] + a_end[0])/2 - 70,(start_RA[1] + a_end[1])/2)
  b_mid = ((b_start[0] + b_end[0])/2 + 30,(b_start[1] + b_end[1])/2)
  c_coords = (150, 50)
  #print(a_mid, b_mid)
  a_text = Text(f'a = {new_round(a)}', a_mid)
  b_text = Text(f'c = {new_round(b)}', b_mid)
  if c == 0:
    q = '?'
  else:
    q = new_round(c)
  c_text = Text(f'b = {q}', c_coords)
  a_text.fill = blue
  b_text.fill = greenn
  c_text.fill = yellow
  
  #a_text.strokecolour = 'light'
  a_text.draw()
  b_text.draw()

  c_text.draw()
  c_text.draw()
  rect(start_RA[0], start_RA[1], 4 * r, 4 * r)


def get_r(a, b, border):
  #gets ratio of line depending on length of legs
  max_width = 500 - 2 * border
  max_height = 400 - 2 * border
  r_width = max_width/b
  r_height = max_height/a
  return min(r_width, r_height)
  


def hypo(a,b):
  return (a ** 2 + b ** 2) ** 0.5
  
def win():
  success()
  celebrate()
  
def default():
  #resets all relevant fonts, colours, etc to a default value
  def_strokecolour = 'black'
  def_strokeweight = 1
  def_fill = 'white'
  stroke(def_strokecolour)
  strokeWeight(def_strokeweight)
  fill('white')
  
class Line:
  def __init__(self, start, end):
    self.start = start #starting coords (x,y)
    self.end = end #ending coords(x,y)
    self.strokecolour = 'black' #strokecolour
    self.strokeweight = 4

  def settings(self):
    stroke(self.strokecolour)
    strokeWeight(self.strokeweight) 
    
  def draw(self):
    self.settings()
    line(self.start[0], self.start[1], self.end[0], self.end[1])
    default()

class Text:
  def __init__(self, text, coords):
    self.text = text
    self.strokecolour = 'black' #strokecolour
    self.strokeweight = 0
    self.size = 20
    self.coords = coords
    self.fill = 'white'
    
  def draw(self):
    fill(self.fill)
    stroke(self.strokecolour)
    strokeWeight(self.strokeweight)
    textSize(self.size)
    text(self.text, self.coords[0], self.coords[1])
    default()

class RightTriangle:
  def __init__(self, a, b):
    self.a = a 
    self.b = b
    self.c = hypo(a,b)  # Calculate hypotenuse using Pythagoras' Theorem

  def draw(self, x, y):
    #
    fill(200)
    strokeWeight(0)
    r = get_r(self.a,self.b, 100)
    triangle(x, y, x, y + self.a * r, x + self.b * r, y)  # Draw right-angled triangle


#triangle1 = RightTriangle(3, 4)
#treasure_map = TreasureMap((100, 200))


def new_round(number):
    # Convert the number to a string
    number_str = str(number)

    # Find the index of the dot (decimal point)
    dot_index = number_str.find('.')

    # If the dot is found and there is at least one digit after the dot
    if dot_index != -1 and len(number_str) > dot_index + 1:
        # Extract the first digit after the dot
        first_digit_after_dot = int(number_str[dot_index + 1])

        # If the next digit is 5 or greater, round up
        if first_digit_after_dot >= 5:
            rounded_number_str = str(int(number_str[:dot_index]) + 1)
        else:
            rounded_number_str = number_str[:dot_index + 2]
    else:
        # No dot found or no digit after the dot, return the original number
        return number

    # Convert the rounded string back to a float

    return rounded_number_str

    
