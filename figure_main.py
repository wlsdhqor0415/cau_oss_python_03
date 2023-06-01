# %%

# 모듈 figure를 불러와 직사각형, 직각삼각형, 타원의 넓이를 계산하는 프로그램입니다.

import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive number for width and height")

myline.set_length(10, 30)
width, height = myline.get_length()
try:
    right_triangle = figure.area_right_triangle(width, height)
    print(right_triangle)
except ValueError:
    print("please input positive number for width and height")

myline.set_length(20, 10)
width, height = myline.get_length()
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please input positive number for width and height")