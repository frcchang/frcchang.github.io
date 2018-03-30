import sys

class Visitor():

   total = 0

   def __init__(self, name = None):
      Visitor.total += 1
      if name:
         self.name = name
      else:
         self.name = 'Visitor {}'.format(Visitor.total)
      self.n = 0

   def setName(self, name):
      self.name = name

   def __call__(self):
      self.n += 1
      return '{} called the {}th time.'.format(self.name, self.n)

#v1 = Visitor('John')
#print v1()
#v2 = Visitor()
#print v2()
#print v1()
#v2.setName('Marina')
#print v2()
#v3 = Visitor()
#print v3()

###

def main():
   f = open(sys.argv[3], 'w')
   test = sys.argv[2]
   v1 = Visitor()
   ans = v1()
   if test == '1':
      print 'v1 = Visitor()'
      print 'Test case 1: v1()'
      f.write(ans)
   v1.setName('John')
   ans = v1()
   if test == '2':
      print "v1.setName('John')"
      print 'Test case 2: v1()'
      f.write(ans)
   v2 = Visitor('Marina')
   ans = v2()
   if test == '3':
      print 'v2 = Visitor("Marina")'
      print 'Test case 3: v2()'
      f.write(ans)
   v3 = Visitor()
   ans = v3()
   if test == '4':
      print 'v3 = Visitor()'
      print 'Test case 4: v3()'
      f.write(ans)
   ans = v2()
   if test == '5':
      print 'Test case 5: v2()'
      f.write(ans)
   ans = v3()
   if test == '6':
      print 'Test case 6: v3()'
      f.write(ans)
   ans = v1()
   if test == '7':
      print 'Test case 7: v1()'
      f.write(ans)
   f.close()

main()
