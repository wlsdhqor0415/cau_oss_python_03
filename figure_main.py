# %%

# 모듈 figure를 불러와 정사각형, 정삼각형, 원의 넓이를 계산하는 프로그램입니다.

import figure

myline = figure.line(10)

square = figure.area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)