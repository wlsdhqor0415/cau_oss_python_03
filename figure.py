## 오픈소스와 파이썬 Homework#5
"""
figure 모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈입니다.
line class를 이용하여 선의 길이를 설정하고 참조하는 것을 수행하며
area_rectangle, area_ellipse, area_right_triangle 함수로
각각 직사각형, 타원, 직각삼각형의 넓이를 반환합니다.
"""
class line:
    """"
    line 클래스는 가로와 세로의 길이에 대해 저장하고 있는 클래스입니다.
    변수로는 외부에서 접근 불가능한 __width와 __height가 있으며,
    해당 변수를 수정하고 접근하기 위한 메소드로는 
    set_length와 get_length가 있습니다.
    """
    __width = 0
    __height = 0

    def __init__(self, initial_width, initial_height):
        """
        생성자 초기 width 값과 height 값을 받습니다.
        Args:
            initial_width (int or float): 초기 가로의 길이 값입니다.
            initial_height (int or float): 초기 세로의 길이 값입니다.
        """
        self.__width = initial_width
        self.__height = initial_height

    def set_length(self, width, height):
        self.__width = width
        self.__height = height
        """
        가로와 세로의 길이를 수정합니다.
        Args:
            width (int or float): 수정하고자 하는 가로의 길이 값입니다.
            height (int or float): 수정하고자 하는 세로의 길이 값입니다.
        """
    def get_length(self):
        """
        객체가 저장하고 있는 가로와 세로의 길이를 반환합니다.
        Returns:
            int or float: 저장하고 있는 가로와 세로의 길이 값입니다.
        """
        return self.__width, self.__height

import math

def area_rectangle(width, height):
    """
    area_rectangle 함수는 밑변과 높이의 길이를 입력받아 직사각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 밑변의 길이입니다.
        height (int or float): 높이의 길이입니다.
    Returns:
        int or float: 직사각형의 넓이를 반환합니다.
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height
def area_ellipse(width, height):
    """
    area_ellipse 함수는 짧은쪽과 긴쪽 반지름의 길이를 입력받아 타원의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 짧은쪽 반지름의 길이입니다.
        height (int or float): 긴쪽 반지름의 길이입니다.
    Returns:
        int or float: 타원의 넓이를 반환합니다.
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi
def area_right_triangle(width, height):
    """"
    area_right_triangle 함수는 밑변과 세로의 길이를 입력받아 직각삼각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 밑변의 길이입니다.
        height (int or float): 높이의 길이입니다.
    Returns:
        int or float: 직각삼각형의 넓이를 반환합니다.
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2