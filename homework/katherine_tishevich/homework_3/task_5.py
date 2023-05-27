# Программа запрашивает у пользователя длину ребра куба. И находит объем куба и площадь его боковой поверхности
cube_edge = float(input('Input value of cube edge length: '))
volume_lateral_surface = cube_edge**3
square_lateral_surface = 6 * volume_lateral_surface**2
print(f"Volume = {volume_lateral_surface}," + ' '
      f"Square = {square_lateral_surface} ")
