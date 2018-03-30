import sys 

def init():

   retval = []
   for i in range(3):
      retval.append(['_']*3)
   return retval

def movex(b, x, y):
   move('x', b, x, y)

def moveo(b, x, y):
   move('o', b, x, y)

def move(c, b, x, y):
   if b[x-1][y-1] != '_':
      raise Exception('Cannot take the move.')
   b[x-1][y-1] = c

def countmoves(b):
   retval = 0
   for i in range(3):
      for j in range(3):
         if b[i][j] != '_':
            retval += 1
   return retval

def getmoves(b):
   retval = {'x':[], 'o':[]}
   for i in range(3):
      for j in range(3):
         if b[i][j] != '_':
            retval[b[i][j]].append((i+1, j+1))
   return retval
def winsx(b):
   return wins('x', b)

def winso(b):
   return wins('o', b)

def wins(c, b):
   f=lambda x: x == c
   for i in range(3):
      if reduce(lambda x, y: x and y, map(f, b[i])):
         return True
      if reduce(lambda x, y: x and y, map(f, [b[j][i] for j in range(3)])):
         return True
   if reduce(lambda x, y: x and y, map(f, [b[i][i] for i in range(3)])):
      return True
   if reduce(lambda x, y: x and y, map(f, [b[i][2-i] for i in range(3)])):
      return True
   return False

def show(b):
   return '\n'.join([''.join(l) for l in b]) + '\n'

###

def main():
   f = open(sys.argv[3], 'w')
   test = sys.argv[2]
   b = init()
   if test == '1':
      print 'Test 1: b = init()'
      ans = str(b)
   if test == '2':
      print 'Test 2: show(b)'
      ans = show(b)
   movex(b, 1, 1)
   if test == '3':
      print 'Test 3: movex(b, 1, 1)'
      ans = str(b)
   moveo(b, 1, 3)
   if test == '4':
      print 'Test 4: moveo(b, 1, 3)'
      ans = str(b)
   if test == '5':
      print 'Test 5: show(b)'
      ans = show(b)
   if test == '6':
      print 'Test 6: countmoves(b)'
      ans = str(countmoves(b))
   if test == '7':
      print 'Test 7: getmoves(b)'
      ans = str(getmoves(b))
   if test == '8':
      print 'Test 8: winsx(b)'
      ans = str(winsx(b))
      #print winsx(b)
   movex(b, 2, 1)
   moveo(b, 2, 3)
   if test == '9':
      print 'movex(b, 2, 1)'
      print 'moveo(b, 2, 3)'
      print 'Test 9: getmoves(b)'
      ans = str(getmoves(b))
   movex(b, 3, 2)
   moveo(b, 3, 3)
   if test == '10':
      print 'movex(b, 3, 2)'
      print 'moveo(b, 3, 3)'
      print 'Test 10: winso(b)'
      ans = str(winso(b))
   if test == '11':
      print 'Test 11: countmoves(b)'
      ans = str(countmoves(b))
   if test == '12':
      print 'Test 12: getmoves(b)'
      ans = str(getmoves(b))
   if test == '13':
      print 'Test 13: winsx(b)'
      ans = str(winsx(b))
   f.write(ans)
   f.close()

main()
