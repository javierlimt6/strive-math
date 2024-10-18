from p5 import *

#$$$
#$$$

blue = 70, 130, 180
yellow = 255, 216, 1
greenn = 35, 140, 35

def setup():
  createCanvas(500, 400)
  global a, b
  a = 3 * 20
  b = 4 * 20
  global aSlider, bSlider
  aSlider = createSlider(0.1, 100, 60)
  aSlider.position(75, height - 40)
  aSlider.size(100)
  bSlider = createSlider(0.1, 100, 80)
  bSlider.position(75, height - 90)
  bSlider.size(100)


def draw():
  background('white')
  textSize(30)
  textAlign(CENTER, CENTER)
  referenceTriangle()
  squareOne()
  squareTwo()

  
  
  noStroke()
  fill(blue)
  text('a:', 55, height - 50)
  fill(yellow)
  text('b:', 55, height - 100)

  global a, b
  a = aSlider.value()
  b = bSlider.value()


def referenceTriangle():
  push()
  translate(250, 300)
  fill(200)
  stroke(255)
  triangle(
    0, 0,
    a, 0,
    a, b
  )
  fill('white')
  noStroke()
  fill(blue)
  text('a', a/2, -15)
  fill(yellow)
  text('b', a + 15, b/2 - 10)
  fill(greenn)
  text('c', a/2 - 20, b/2 + 10)
  pop()


def squareOne():
  push()
  # base
  fill(230)
  stroke('black')
  square(0, 0, a + b)

  fill(200)
  # top left
  push()
  translate(0, b)
  triangle(
    0, 0,
    0, a,
    b, a
  )
  triangle(
    0, 0,
    b, 0,
    b, a
  )
  noStroke()
  fill('black')
  text('a+b', (a+b)/2, a + 15)
  text('a+b', (a+b) + 30, -b + (a+b)/2)
  fill(yellow)
  
  text('b²', b/2, -b/2)
  textSize(25)
  text('b', b/2, 10)
  fill(blue)
  text('a', b - 10, a/2)
  pop()

  # bottom right
  push()
  translate(b, 0)
  triangle(
    0, 0,
    a, 0,
    0, b
  )
  triangle(
    a, 0,
    a, b,
    0, b
  )
  fill(blue)
  noStroke()
  text('a²', a/2, b + a/2)
  textSize(25)
  text('a', a/2, b - 10)
  fill(yellow)
  text('b', 10, b/2)
  pop()


def squareTwo():
  push()
  translate(width/2 + 50, 0)
  # base
  fill(230)
  stroke('black')
  square(0, 0, a + b)

  fill(200)
  stroke('black')
  # bottom left
  push()
  triangle(
    0, 0,
    a, 0,
    0, b
  )
  noStroke()
  fill('black')
  text('a+b', -30, (a+b)/2)
  text('a+b', (a+b)/2, a+b+15)
  fill(greenn)
  textSize(25)
  text('c', a/2 - 10, b/2 - 10)
  pop()
  # top left
  push()
  translate(0, b)
  triangle(
    0, 0,
    0, a,
    b, a
  )
  noStroke()
  fill(greenn)
  textSize(25)
  text('c', b/2 - 10, a/2 + 10)
  pop()
  # bottom right
  push()
  translate(a, 0)
  triangle(
    0, 0,
    b, 0,
    b, a
  )
  noStroke()
  fill(greenn)
  textSize(25)
  text('c', b/2 + 10, a/2 - 10)
  pop()
  # top right
  push()
  translate(b, a + b)
  triangle(
    0, 0,
    a, 0,
    a, -b
  )
  noStroke()
  fill(greenn)
  text('c²', (a-b)/2, (-b-a)/2)
  textSize(25)
  text('c', a/2 + 10, -b/2 + 10)
  pop()
  pop()



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
    if number == 0:
      return '?'
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
