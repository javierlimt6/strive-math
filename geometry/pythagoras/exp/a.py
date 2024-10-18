from p5 import *

def setup():
  createCanvas(500,400)

def draw():
  background("white")
  #colours
  blue = 70, 130, 180
  yellow = 255, 216, 1
  green = 35, 140, 35
  red = 252, 0, 6
  a_colour = blue
  b_colour = yellow
  c_colour = green
  ##student INPUT
  #$$$
  a_length = $$3$$
  b_length = $$4$$
  #$$$
  angle_ab= 90
  included_angle = angle_ab
  strokeWeight(0)
  #red = (226, 164, 153)
  #blue = (0, 191, 255)
  purple = (208, 184, 230)
  cur_angle = frameCount/2
  if cur_angle > included_angle:
    cur_angle = included_angle
    if included_angle != 90:
      fill(red)

      #text("Try Again!", 250, 275)
      fill('white')
      #text("Hint: Try changing the angle :)", 50, 225)
  
  #r is the ratio in which the triangle is displayed, default set to 32
  r = get_r(a_length, b_length, 75)
  #x1 and y1 represent the coords where the fixed point is
  x1 = width/2-b_length * r/2
  y1 =(height-50)/2-a_length*r/2
  if x1 < 75:
    x1 = 75
  if y1 < 75:
    y1 = 75
  #width = b_length * r
  #height = a_length * r
  #width/2-b_length * r/2
  #height/2-a_length*r/2
  
  #getting coords for the other 2 points
  x_a = a_length * cos(cur_angle) * r + x1
  y_a = a_length * sin(cur_angle) * r + y1
  x_b = x1 + b_length * r
  y_b = y1
  #Text Instructions
  text_size = 0.75 * 32
  textSize(text_size)
  fill("white")
  #cos formula: sqr(a2+b2﹣2abcosγ)
  #Getting coords of labels & length of c
  a_label_coords = ((x_a + x1)/2, (y_a + y1)/2)
  b_label_coords = ((x_b + x1)/2, (y_b + y1)/2)
  c_label_coords = ((x_b + x_a)/2, (y_b + y_a)/2)
  c_length = (a_length ** 2 + b_length ** 2 - 2 * a_length * b_length * cos(cur_angle)) ** 0.5
  c_sq = new_round(c_length ** 2)
  c_length = new_round(c_length)
  a_sq_b_sq = a_length ** 2  + b_length ** 2
  #Labelling each side of the triangle
  fill(a_colour)
  textAlign(RIGHT, CENTER)
  text(f"a = {a_length}", a_label_coords[0] - 20, a_label_coords[1])
  fill(b_colour)
  textAlign(CENTER, CENTER);
  text(f"b = {b_length}", b_label_coords[0], b_label_coords[1] - 50)
  fill(c_colour)
  textAlign(LEFT, CENTER);
  text(f"c = {c_length}", c_label_coords[0] + 50, c_label_coords[1])
  fill('white')
  
  #Implement triangle
  stroke("black")
  strokeWeight(4)
  fill(200)
  triangle(x1, y1, x_a, y_a, x_b, y_b)
  strokeWeight(0)

  #Drawing and labelling the angle displayed
  #if green actions
  if cur_angle == 90 and included_angle == 90:
    #success()
    #celebrate()
    fill(green)
    textAlign(RIGHT, CENTER)
    #text(a_sq_b_sq, 395, 325)
    textAlign(LEFT, CENTER)
    #text(c_sq, 420, 325)
    #text("Good job!", 250, 225)
    textSize(text_size)
    text(str(cur_angle) + "°", x1 + text_size, y1 + text_size)
    #text('=', 400, 325)
    rect(x1, y1, 20, 20)
    pass
  else:
    fill(purple)
    textAlign(RIGHT, CENTER)
    #text(a_sq_b_sq, 395, 325)
    fill('yellow')
    textAlign(LEFT, CENTER)
    #text(c_sq, 420, 325)
    fill('white')
    strokeWeight(2)
    arc(x1, y1, 30, 30, 0, cur_angle)
    strokeWeight(1)
    fill(red)
    #text('=', 400, 325) # turns green when solved
    #text('X', 399, 325)
    fill('black')
    text(str(cur_angle) + "°", x1 + text_size, y1 + text_size)
  strokeWeight(0)
  text(LEFT, CENTER)
  stroke("black")
  
  textAlign(RIGHT, CENTER)
  #display angle text
  stroke(red)
  fill(255,255,255)
  
  
  #Writing out the text (a^2 + b^2 = ...), c^2 = ..
  stroke("black")
  #text('How do I prove that', 0, 400)
  textSize(1.2 * r)
  textAlign(LEFT, CENTER);
  fill(a_colour)
  #text('a²', 25, 350)
  #text('a^2 +', 300, 375)
  
  fill(b_colour)
  #text(' b^2 ', 105, 375)
  #text('b²', 180, 350)
  #fill('black')
  #text(f'={a_length ** 2}', 90, 350)
  #text(f'={b_length ** 2}', 243, 350)
  #text(c_sq, 415, 350)
  #text(f'=', 390, 350)
  #fill(c_colour)
  #text('c²', 330, 350)
  fill(225, 232, 245)
  stroke(173, 191, 226)
  
  rect(0,height-100,width,100,0)
  draw_text("a²",a_length ** 2,blue,40,350,1.5 * text_size)
  draw_text("b²",b_length ** 2,yellow,180,350,1.5 * text_size)
  draw_text("c²",c_sq,green,340,350,1.5 * text_size)
  #draw_text("c²",c_sq,green,340,350,1.5 * text_size)


def draw_text(t,value,colour,x,y,size):
  push()
  stroke("black")
  textAlign(CENTER, CENTER)
  textSize(size)
  textStyle(BOLD)
  fill(colour)
  text(t, x, y)

  textStyle(NORMAL)
  textAlign(LEFT, CENTER)
  fill("black")
  text("= " + str(value),x+size-10,y)
  
  pop()

def draw_text_question(t,value,colour,x,y,size):
  push()
  stroke("black")
  textAlign(CENTER, CENTER)
  textSize(size)
  textStyle(BOLD)
  fill(colour)
  text(t, x, y)

  textStyle(NORMAL)
  textAlign(LEFT, CENTER)
  fill("black")
  text("= ?",x+size-10,y)
  
  pop()

def get_r(a, b, border):
  #gets ratio of line depending on length of legs
  max_width = 500 - 2 * border
  max_height = 400 - 2 * border - 100
  r_width = max_width/b
  r_height = max_height/a
  return min(r_width, r_height)
def new_round(num):
    # Multiply the number by 10 to shift the decimal point
    shifted_num = num * 10

    # Get the integer part of the shifted number
    integer_part = int(shifted_num)

    # Get the fractional part of the shifted number
    fractional_part = shifted_num - integer_part

    # Round the fractional part to the nearest integer
    if fractional_part >= 0.5:
        integer_part += 1

    # Shift the decimal point back and convert to string
    rounded_string = str(integer_part / 10)

    return rounded_string
