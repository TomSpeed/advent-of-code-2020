from functools import reduce

def parse_slope_line(line):
  return [ch == '#' for ch in line]

def read_slope():
  with open('input.txt', 'r') as f:
    lines = [parse_slope_line(line.strip()) for line in f]
  return lines

def get_path_coords(slope_len, x_multiplier, y_multiplier):
  path_coords = map(lambda z: (z * x_multiplier, z * y_multiplier), range(0, slope_len))
  return list(filter(lambda coord: coord[1] <= slope_len, path_coords))

def get_slope_x_coord(x, line_len):
  if x < line_len:
    return x
  return x % line_len

def is_tree(slope, coord):
  y = coord[1]
  line = slope[y]
  x = get_slope_x_coord(coord[0], len(line))
  return line[x]

def get_tree_cords(slope, x_multiplier, y_multiplier):
  slope_len = len(slope)
  path_coords = get_path_coords(slope_len, x_multiplier, y_multiplier)
  return list(filter(lambda coord: is_tree(slope, coord), path_coords))

def count_trees(slope, x_multiplier, y_multiplier):
  return len(get_tree_cords(slope, x_multiplier, y_multiplier))

def part_two(slope, part_one_answer):
  tree_counts = [
    count_trees(slope, 1, 1),
    part_one_answer,
    count_trees(slope, 5, 1),
    count_trees(slope, 7, 1),
    count_trees(slope, 1, 2)
  ]
  return reduce(lambda x, y: x * y, tree_counts)

def main():
  slope = read_slope()
  part_one_answer = count_trees(slope, 3, 1)
  print('Part one:', part_one_answer)
  print('Part two:', part_two(slope, part_one_answer))

main()