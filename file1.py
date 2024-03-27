
def addition(*args):
  return sum(args)


def subtraction(*args):
  result = args[0]
  for num in args[1:]:
    result -= num
  return result


