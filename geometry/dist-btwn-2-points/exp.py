from p5 import *

orange = '#ffe7c2'
red = '#ff1a40'
blue = '#0000ff'
purple = '#f5e1ff'
green = '#00ff00'
lgreen = '#e0f0ea'
dot_spacing = 5  # Spacing between dots
is_pressed = False
grid_size = 25
zero_pt = (25,25) # both x, y coords must be in multiples of the grid_size, zero_pt cannot be (0,0)
#uncomment to produce graph in a fixed window
windowWidth = 500
windowHeight = 400
def setup():
  createCanvas(windowWidth,windowHeight)

  
def draw():
  global is_pressed
  ###STUDENT INPUTS
  #$$$
  start_coords = ($$1$$, $$2$$)
  end_coords = ($$7$$,$$6$$)
  #$$$
  ###
  background(255)
  #colouring the rectangles
  xyaxis()
  grid()
  
  if is_pressed:
    solidify(start_coords, end_coords)
  graph_line(start_coords, end_coords)
  drawMousePos(start_coords, end_coords)

  if mouseIsPressed:
    is_pressed = True
    noLoop()

    
  

  # Draw dotted lines

def xyaxis():
  push()
  strokeWeight(4)
  #x-axis
  line(0,zero_pt[1] ,windowWidth, zero_pt[1])
  #y-axis
  line(zero_pt[0],0,zero_pt[0],windowHeight)
  pop()


def solidify(start_coords, end_coords):
  snapped_x = round(mouseX / grid_size) * grid_size
  snapped_y = round(mouseY / grid_size) * grid_size
  actual_start = actual_pos_x(start_coords[0]), actual_pos_y(start_coords[1])
  actual_end = actual_pos_x(end_coords[0]), actual_pos_y(end_coords[1])
  accepted = [(actual_start[0], actual_end[1]), (actual_end[0], actual_start[1])]
  push()
  snapped = (snapped_x, snapped_y)
  if snapped in accepted:
    fill(green)
    
    
  else:
    fill(red)
  strokeWeight(grid_size // 5)
  triangle(actual_start[0], actual_start[1], snapped[0], snapped[1], actual_end[0], actual_end[1])
  if snapped in accepted:
    draw_RA(snapped, actual_start, actual_end)
    correct_resp(start_coords, end_coords)
  pop()

def draw_RA(snapped, actual_start, actual_end):
  push()
  strokeWeight(grid_size / 10)
  #snapped x > min(start, end x) right
  #else left
  #snapped y > min(start, end y) top
  #else bot
  fill('white')
  x, y = snapped
  if snapped[0] > min(actual_start[0], actual_end[0]):
    x -= grid_size
  if snapped[1] > min(actual_start[1], actual_end[1]):
    y -= grid_size
  square(x, y, grid_size)
  pop()

def correct_resp(start, end):
  push()
  textSize(25)
  noStroke()
  fill(lgreen)
  
  x_dist = abs(start[0] - end[0])
  y_dist = abs(start[1] - end[1])
  dist = (x_dist ** 2 + y_dist ** 2) ** 0.5  
  rect(240, 260, textWidth(f'dist = √({x_dist}²+{y_dist}²) = {new_round(dist)}') + 15, 130, 10)
  colorful_text('Correct!', 250, 360, "black", {"x":"red", "y":"blue"}, "")
  colorful_text(f'x dist = {max(start[0], end[0])}-{min(start[0], end[0])} = {x_dist}', 250, 330, "black", {"x":"red", str(x_dist):"red", "y":"blue"}, "")
  colorful_text(f'y dist = {max(start[1], end[1])}-{min(start[1], end[1])} = {y_dist}', 250, 300, "black", {"x":"red", str(y_dist):"blue","y":"blue"}, "")
  colorful_text(f'dist = √({x_dist}²+{y_dist}²) = {new_round(dist)}', 250, 270, "black", {str(x_dist):"red", str(y_dist):"blue"}, "")
  pop()
def mouseClicked():
  redraw()
  
def grid():
  push()
  strokeWeight(0.5)
  textSize(grid_size / 2)
  textAlign(CENTER, CENTER)
  #vert lines
  for x in range(0, windowWidth + 1, grid_size):
    line(x, 0, x, windowHeight)
    value = (x - zero_pt[0])//grid_size
    if value != 0:
      text(value, x, zero_pt[1] - grid_size // 2)
  #horizontal lines
  for y in range(0, windowHeight + 1, grid_size):
    line(0, y, windowWidth, y)
    value = (y - zero_pt[1])//grid_size
    if value != 0:
      text(value, zero_pt[0] - grid_size // 2, y)
    
  text(0, zero_pt[0] - grid_size // 2, zero_pt[1] - grid_size // 2)
  
  pop()

def actual_pos_x(x):
  return grid_size * x + zero_pt[0]

def actual_pos_y(y):
  return grid_size * y + zero_pt[1]

def drawMousePos(start_coords, end_coords):
  if mouseX == 0 and mouseY == 0:
    return
  snapped_x = round(mouseX / grid_size) * grid_size
  snapped_y = round(mouseY / grid_size) * grid_size
  actual_start = actual_pos_x(start_coords[0]), actual_pos_y(start_coords[1])
  actual_end = actual_pos_x(end_coords[0]), actual_pos_y(end_coords[1])
  dotted(actual_start, (snapped_x, snapped_y))
  dotted(actual_end, (snapped_x, snapped_y))
  ellipse(snapped_x, snapped_y, grid_size // 2, grid_size // 2)
  
  
  text_coords(((snapped_x - zero_pt[0])//grid_size, (snapped_y - zero_pt[1])//grid_size), 'pointer')
    
  #print(mouseX, mouseY)

def dotted(start, end):
  push()
  d = int(dist(start[0], start[1], end[0], end[1]))
  for i in range(0, d, dot_spacing * 2):
      x1 = lerp(start[0], end[0], i / d)
      y1 = lerp(start[1], end[1], i / d)
      x2 = lerp(start[0], end[0], (i + dot_spacing) / d)
      y2 = lerp(start[1], end[1], (i + dot_spacing) / d)
      line(x1, y1, x2, y2)
  pop()

def graph_line(start_coords, end_coords):
  axis_line(start_coords, end_coords)
  text_coords(start_coords, 'start')
  text_coords(end_coords, 'end')


def axis_line(start_coords, end_coords):
  actual_start = actual_pos_x(start_coords[0]), actual_pos_y(start_coords[1])
  actual_end = actual_pos_x(end_coords[0]), actual_pos_y(end_coords[1])
  push()
  strokeWeight(grid_size // 7)
  line(actual_start[0], actual_start[1], actual_end[0], actual_end[1])
  noStroke()
  fill(150)
  ellipse(actual_start[0], actual_start[1], grid_size // 2, grid_size // 2)
  ellipse(actual_end[0], actual_end[1], grid_size // 2, grid_size // 2)
  stroke(0)
 
  pop()

def text_coords(coords, pos):
  x = coords[0]
  y = coords[1]
  actual = actual_pos_x(x), actual_pos_y(y)
  push()
  noStroke()
  textSize(grid_size // 2)
  textAlign(CENTER, CENTER)
  textStyle(BOLD)
  rectMode(CENTER)
  text = f"x: {x}, y: {y}"
  w = textWidth(text) + 0.2 * grid_size
  h = grid_size // 2
  if pos == 'start':
    fill(orange)
  elif pos == 'pointer':
    fill('#c2ffc2')
  else:
    fill(purple)
  rect(actual[0]+grid_size, actual[1] - grid_size // 2, w, h, 10)
  colorful_text(text, actual[0] - w//2 + 1.2 * grid_size, actual[1] - grid_size // 2, "black", {"x":"red", "y":"blue"}, "")
  pop()

def colorful_text(tex_major, x, y, default_clr, dictionary, sep=" "):
  #colorful_text("Hello 3+4 = 7", 250-textWidth("Hello 3+4 = 7")/2, 200, 255, {"+":"red", "-":"red", "=":"blue"}, "")
  push()
  tex = tex_major
  if sep!="":
    parts = tex.split(sep)
  else:
    parts = list(tex)
  
  dx = 0
  for part in parts:
    similar_parts = [part]
    if "," in part and (list(part).index(",")==0 or list(part).index(",")==len(part)-1):
      part_list = list(part)
      part_list.pop(part.index(","))
      similar_parts.append("".join(part_list))
    if "." in part and (list(part).index(".")==0 or list(part).index(".")==len(part)-1):
      part_list = list(part)
      part_list.pop(part.index("."))
      similar_parts.append("".join(part_list))
    if "!" in part and (list(part).index("!")==0 or list(part).index("!")==len(part)-1):
      part_list = list(part)
      part_list.pop(part.index("!"))
      similar_parts.append("".join(part_list))
    if "?" in part and (list(part).index("?")==0 or list(part).index("?")==len(part)-1):
      part_list = list(part)
      part_list.pop(part.index("?"))
      similar_parts.append("".join(part_list))
    result = 0
    winning_sp = None
    for sp in similar_parts:
      if sp in dictionary:
        result+=1
        winning_sp=sp
    if result>0:
      clr = dictionary[winning_sp]
      fill(clr)
    else:
      fill(default_clr) # default color (black)
    text(part + sep, x+dx, y) # display the part
    dx += textWidth(part + sep) # increment x position by part width
  pop()

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
  
