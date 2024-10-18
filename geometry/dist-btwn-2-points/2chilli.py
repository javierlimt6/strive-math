from p5 import *

orange = '#ffe7c2'
red = '#ff1a40'
blue = '#0000ff'
purple = '#f5e1ff'
green = '#99ff99'
lgreen = '#e0f0ea'
a_blue = 70, 130, 180
b_yellow = 255, 216, 1
c_green = 35, 140, 35
dot_spacing = 5  # Spacing between dots
is_pressed = False
grid_size = 25
zero_pt = (250,175) # both x, y coords must be in multiples of the grid_size, zero_pt cannot be (0,0)
#uncomment to produce graph in a fixed window
windowWidth = 500
windowHeight = 400
def setup():
  createCanvas(windowWidth,windowHeight)

  
def draw():
  global is_pressed
  ###STUDENT INPUTS
  #$$$
  a = $$0$$
  b = $$0$$
  c = $$0$$
  #$$$
  ###TEACHER INPUTS
  start_coords = (1, -1)
  end_coords = (5,-4)
  background(255)
  #colouring the rectangles
  xyaxis()
  grid()
  qn_prompt(c, start_coords, end_coords)
  if is_pressed:
    solidify(start_coords, end_coords, a, b, c)
  graph_line(start_coords, end_coords)
  drawMousePos(start_coords, end_coords)

  if mouseIsPressed:
    is_pressed = True
    noLoop()

    
  

  # Draw dotted lines

def xyaxis():
  push()
  strokeWeight(3)
  #x-axis
  line(0,zero_pt[1] ,windowWidth, zero_pt[1])
  #y-axis
  line(zero_pt[0],0,zero_pt[0],windowHeight)
  pop()


def solidify(start_coords, end_coords, a, b, c):
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
  strokeWeight(grid_size // 5 - 2)
  triangle(actual_start[0], actual_start[1], snapped[0], snapped[1], actual_end[0], actual_end[1])
  if snapped in accepted:
    pos = draw_RA(snapped, actual_start, actual_end)
    correct_resp(start_coords, end_coords, a, b, c)
    draw_text(pos, actual_start, actual_end, snapped)
  
  pop()

def draw_text(pos, start, end, snapped):
  push()
  x = start[0] if end[0] == snapped[0] else end[0]
  y = start[1] if end[1] == snapped[1] else end[1]
  textSize(20)
  textAlign(CENTER, CENTER)
  fill(a_blue)
  text('a', (x + snapped[0])/2, snapped[1] - 1.5 * pos[0])
  fill(b_yellow)
  text('b', snapped[0] - 1.5 * pos[1], (y + snapped[1])/2)
  fill(c_green)
  text('c', (x + snapped[0])/2 + pos[1], (y + snapped[1])/2 + pos[0])
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
  left = grid_size / 2
  bot = grid_size / 2
  if snapped[0] > min(actual_start[0], actual_end[0]):
    x -= grid_size / 2
    left = -left
  if snapped[1] > min(actual_start[1], actual_end[1]):
    y -= grid_size / 2
    bot = -bot
  square(x, y, grid_size / 2)
  pop()
  return (bot, left)

def get_correct(start, end):
  x_sq = (start[0] - end[0]) ** 2
  y_sq = (start[1] - end[1]) ** 2
  return (x_sq + y_sq) ** 0.5

def qn_prompt(ans, start, end):
  push()
  noStroke()
  fill(149, 173, 190, 230)
  rect(0, 350, windowWidth, 80)
  textAlign(CENTER, CENTER)
  fill_col = 'white'
  if ans == 0:
    ans = '?'
  else: 
    ans = float(new_round(ans))
    if ans == float(new_round(get_correct(start, end))):
      success()
      celebrate()
      fill_col = green
      fill(green)
      textSize(30)
      text('Correct!', 360, 370)
    else:
      fill(red)
      textSize(30)
      text('Wrong!', 360, 370)
      fill_col = red
  textSize(40)
  colorful_text(f"c = {str(ans)}", windowWidth/4, 370, 'white', {"c": c_green, str(ans) : fill_col}, "")
  pop()


def correct_resp(start, end, a, b, c):
  push()
  textSize(25)
  noStroke()
  fill(lgreen)
  for el in [a,b,c]:
    if el == 0:
      el = '?'
  def check(x):
    if x == 0:
      return '?'
    return new_round(x)
  c_corr = get_correct(start, end)
  x_dist = abs(start[0] - end[0])
  y_dist = abs(start[1] - end[1])
  corr = [new_round(x_dist), new_round(y_dist), new_round(c_corr)]
  a, b, c = (check(x) for x in (a,b,c))
  vars = [a,b,c]

  rect(320, 295, textWidth(f'dist = √({x_dist}²+{y_dist}²) = {new_round(dist)}') + 15, 130, 10)
  for i in range(3):
    if vars[i] != '?' and vars[i] != corr[i]:
      push()
      textSize(30)
      fill(red)
      text('Wrong!', 395, 370 - i * 30)
      pop()
  colorful_text(f'a = {a}', 325, 370, "black", {"a": a_blue, str(a): "red"}, "")
  colorful_text(f'b = {b}', 325, 340, "black", {"b": b_yellow, str(b):"blue"}, "")
  colorful_text(f'c = {c}', 325, 310, "black", {'c': c_green}, "")
  pop()
def mouseClicked():
  redraw()

def brkt(x):
  if int(x) < 0:
    return '(' + str(x) + ')'
  return x

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
  
