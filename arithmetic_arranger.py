# arithmetic_arranger.py - 2023.10.02
# (c) Kingsley Ezenwaka (kezenwaka@gmail.com)

def arithmetic_arranger(problems_string, check=None):
  if type(problems_string) == type([]):
    math_problems = splitter(problems_string)
  else:
    return None

  if len(math_problems) > 5:
    return "Error: Too many problems."

  for problem in math_problems:
    try:
      int(problem[0])
      int(problem[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    if not (problem[1] == '+' or problem[1] == '-'):
      return "Error: Operator must be '+' or '-'."

    problem = solutions(problem)
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

  for v in math_problems:
    v[0] = align(v[0], v[3])
    v[2] = align(v[2], v[3])
    v[4] = align(v[4], v[3])

  first_prob = math_problems.pop(0)
  line = []
  line.append('  ' + first_prob[0])
  line.append(first_prob[1] + ' ' + first_prob[2])
  line.append('-' * (2 + first_prob[3]))
  if len(first_prob[4]) > first_prob[3]:
    line.append(' ' + first_prob[4])
  else:
    line.append('  ' + first_prob[4])
  
  if math_problems:
    for prob in math_problems:
      lstx = spacer(prob)
      for i in range(4):
        line[i] = line[i] + lstx[i]

  if check == True:
    arranged_problems = line[0] + '\n' + line[1] + '\n' + line[2] + '\n' + line[3]
  else:
    arranged_problems = line[0] + '\n' + line[1] + '\n' + line[2]

  return arranged_problems

def splitter(x):
  probs = []
  for item in x:
    probs.append(item.split())
  return probs

def solutions(x):
  x.append(max([len(a) for a in x]))
  if x[1] == '+':
    x.append(str(int(x[0]) + int(x[2])))  
  elif x[1] == '-':
    x.append(str(int(x[0]) - int(x[2])))
  return x

def align(string, length):
  space = ' '
  add = ''
  if length > len(string):
    diff = length - len(string)
    for i in range(diff):
      add += space
    string = add + string
  return string

def spacer(m):
  a = '      ' + m[0]
  b = '    ' + m[1] + ' ' + m[2]
  c = '    ' + ('-' * (2 + m[3]))
  if len(m[4]) > m[3]:
    d = '     ' + m[4]
  else:
    d = '      ' + m[4]
  return [a, b, c, d]

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
