# http://adventofcode.com/2017/day/21


def rotate2(input):
  output = ""
  output += input[1]
  output += input[4]
  output += "/"
  output += input[0]
  output += input[3]

  return output


def rotate3(input):
  output = ""
  output += input[2]
  output += input[6]
  output += input[10]
  output += "/"
  output += input[1]
  output += input[5]
  output += input[9]
  output += "/"
  output += input[0]
  output += input[4]
  output += input[8]

  return output


def mirror3(input):
  output = ""
  output += input[2]
  output += input[1]
  output += input[0]
  output += "/"
  output += input[6]
  output += input[5]
  output += input[4]
  output += "/"
  output += input[10]
  output += input[9]
  output += input[8]

  return output

def get_rules():
  rule_lines = open("day21-input.txt", 'r').read().splitlines()
  rules = {}

  for rule_line in rule_lines:
    rule = rule_line.split(" => ")
    if len(rule[0]) == 5:
      rules[rule[0]] = rule[1]
      tmp = rotate2(rule[0])
      rules[tmp] = rule[1]
      tmp = rotate2(tmp)
      rules[tmp] = rule[1]
      tmp = rotate2(tmp)
      rules[tmp] = rule[1]
    else:
      rules[rule[0]] = rule[1]
      tmp = rotate3(rule[0])
      rules[tmp] = rule[1]
      tmp = rotate3(tmp)
      rules[tmp] = rule[1]
      tmp = rotate3(tmp)
      rules[tmp] = rule[1]
      tmp = mirror3(tmp)
      rules[tmp] = rule[1]
      tmp = rotate3(tmp)
      rules[tmp] = rule[1]
      tmp = rotate3(tmp)
      rules[tmp] = rule[1]
      tmp = rotate3(tmp)
      rules[tmp] = rule[1]

  return rules


def iter(iter_count=1):
  
  rules = get_rules()

  grid = """.#.
  ..#
  ###""".splitlines()


  for i in range(iter_count):
    for i in range(5):
      if (len(grid) % 2) == 0:
        tmp_grid = []
        for offset in range(int(len(grid)/2)):
          line1 = line2 = line3 = ""
          for j in range(int(len(grid)/2)):
            sub_grid = grid[offset*2][j*2:(j+1)*2] + "/" + grid[offset*2+1][j*2:(j+1)*2]
            result = rules[sub_grid].split("/")
            line1 += result[0]
            line2 += result[1]
            line3 += result[2]
          tmp_grid.append(line1)
          tmp_grid.append(line2)
          tmp_grid.append(line3)
        grid = tmp_grid
      else:
        tmp_grid = []
        for offset in range(int(len(grid)/3)):
          line1 = line2 = line3 = line4 = ""
          for j in range(int(len(grid)/3)):
            sub_grid = grid[offset*3][j*3:(j+1)*3] + "/" + grid[offset*3+1][j*3:(j+1)*3] + "/" + grid[offset*3+2][j*3:(j+1)*3]
            result = rules[sub_grid].split("/")
            line1 += result[0]
            line2 += result[1]
            line3 += result[2]
            line4 += result[3]
          tmp_grid.append(line1)
          tmp_grid.append(line2)
          tmp_grid.append(line3)
          tmp_grid.append(line4)
        grid = tmp_grid


  count = 0
  for i in range(len(grid)):
    for offset in range(len(grid)):
      if grid[i][offset] == "#":
        count += 1

  print(count)


iter(1)
iter(18)
