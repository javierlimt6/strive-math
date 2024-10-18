from p5 import *

windowHeight = 400
windowWidth = 600
orange = '#ffddc9'
red = '#FFCCCC'
combined = '#f0f4ff'
purple = '#d6c2ff'
col = 4
row = 6
col_r = windowWidth/col
row_r = windowHeight/row
def setup():
  createCanvas(windowWidth,windowHeight)
  
def draw():
  background(255)
  #colouring the rectangles
  # push()
  # noStroke()
  # fill(red)
  # rect(150 ,300, 300, 100)
  # rect(150, 0, 300, 100)
  # fill(orange)
  # rect(0, 100, 150, 200)
  # rect(450, 100, 150, 200)
  # fill(purple)
  # rect(0,0, 150, 100)
  # rect(450, 300, 150, 100)
  # rect(450, 0, 150, 100)
  # fill(combined)
  # rect(150, 100, 300, 200)
  # pop()
  push()
  noStroke()
  fill('pink')
  rect(0, windowHeight * (row-3)/row, windowWidth, windowHeight)
  fill(220)
  rect(0, 0, windowWidth/col, windowHeight * ((row-3)/row))
  rect(col_r,windowHeight * ((row-3)/row), windowWidth, row_r)

  pop()
  textAlign(CENTER, CENTER)
  textSize(150/row)
  push()
  ###STUDENT INPUTS
  #$$$
  like_apple_orange = $$13$$
  hate_apple_orange = $$4$$
  like_apple_hate_orange = $$2$$
  hate_apple_like_orange = $$1$$
  size = $$20$$
  #$$$
  ###TEACHER INPUTS
  
  item1 = 'apple'
  item2 = 'orange'
  like = '✅'
  hate = '❌'
  title = 'Play around with the values to see the changes!'
  ###
  #place text
  text(like+item1, col_r * 1.5, row_r * (row - 2.5))
  text(hate+item1, col_r * 2.5, row_r * (row - 2.5))
  text(like+item2, col_r * 0.5, row_r * 2.5)
  text(hate+item2, col_r * 0.5, row_r * 1.5)
  #text(item1 + '/' + item2, 75, windowHeight * (row - 1.5)/row)
  textStyle(BOLD)
  push()
  textAlign(LEFT, BASELINE)
  textSize(30)
  text_boxed(title, string_width=windowWidth-10, x=10, y=row_r * (row -0.5) - 20, box_clr="pink", text_clr="black")
  #text(title, windowWidth/2, row_r * (row - 0.5))
  pop()
  text('Total', col_r * 0.5, windowHeight * 0.5/row)
  text('Total', col_r * (col - 0.5), windowHeight * (row - 2.5)/row)
  pop()
  grid()
  #text_boxed("Speech Goes Here!", string_width=100, x=50, y=350, box_clr="white", text_clr="black")
  item1_hate_item2_like = hate_apple_like_orange
  item1_like_item2_hate = like_apple_hate_orange
  item12_like = like_apple_orange
  item12_hate = hate_apple_orange
  item1_like = item12_like + item1_like_item2_hate
  item2_like = item12_like + item1_hate_item2_like
  item1_hate = item1_hate_item2_like + item12_hate
  item2_hate = item12_hate + item1_like_item2_hate
  
  
  
  push()
  textStyle(BOLD)
  
  def text_checksize(size, x, y):
    push()
    if item1_like + item1_hate != size or item2_like + item2_hate != size:
      fill('#b31240')
    else:
      fill('green')
    text_num(size, x, y)
    pop()

  
  text_checksize(size, col_r * (col - 0.5), row_r * 0.5)
  text_num(item1_like, col_r * 1.5, row_r * 0.5)
  text_num(item1_hate, col_r * 2.5, row_r * 0.5)
  text_num(item2_like, col_r * (col - 0.5), row_r * 2.5)
  text_num(item2_hate, col_r * (col - 0.5), row_r * 1.5)
  pop()
  text_num(item12_like, col_r * 1.5, row_r * 2.5)
  text_num(item12_hate, col_r * 2.5, row_r * 1.5)
  text_num(item1_hate_item2_like, col_r * 2.5, row_r * 2.5)
  text_num(item1_like_item2_hate, col_r * 1.5, row_r * 1.5)
  

  

def text_num(el, x, y):
  push()
  if el < 0:
    fill('#b31240')
  text(el, x, y)
  pop()
def grid():
  push()
  strokeWeight(2.5)
  r = windowWidth/col
  j = r
  for i in range(row - 1):
    if i == row - 2:
      i *= (windowHeight/row)
      line(r,i,windowWidth, i)
    else:
      i *= (windowHeight/row)
      line(0,i,windowWidth, i)

  while j <= windowWidth:
    line(j,0,j,windowHeight * ((row-2)/row))
    j += r
  pop()


def string_wrapped(string, string_width):
  x=0
  new_string = ""
  for part in string.split(" "):
    part_width = textWidth(part+" ")
    if x+part_width >= string_width:
      new_string += char(10) +part+" "
      x = part_width
    else:
      new_string += part+" "
      x += part_width
  return new_string



def text_boxed(string, string_width, x, y, box_clr, text_clr):
  w, h = string_width*1.1, None
  string = string_wrapped(string, string_width)
  num_lines = 2 + string.count(char(10))
  h = num_lines*textLeading() - 10
  push()
  noStroke()
  fill(box_clr)
  rect(x-0.05*string_width, y+textLeading(), w, -h)
  fill(text_clr)
  text(string, x, y)
  pop()
