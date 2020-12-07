def read_report():
  with open('input.txt', 'r') as f:
    entries = [line.strip() for line in f]
  int_entries = map(int, entries)
  return list(int_entries)

def part_one(report):
  matches_map = map(lambda x : 2020 - x, report)
  matching_etries_filter = filter(lambda x : x in report, matches_map)
  matching_etries = tuple(matching_etries_filter)

  return matching_etries[0] * matching_etries[1]

def part_two(report):
  for x in report:
    for y in report:
      for z in report:
        if x + y + z == 2020:
          return x * y * z

def main():
  report = read_report()
  print('Part one:', part_one(report))
  print('Part two:', part_two(report))

main()
