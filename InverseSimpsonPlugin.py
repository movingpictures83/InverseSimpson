import sys
import numpy

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


class InverseSimpsonPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      for line in filestuff:
         self.ADJ.append([])
         contents = line.split(',')
         for j in range(len(contents)-1):
            value = float(contents[j+1])
            self.ADJ[len(self.ADJ)-1].append(value)

   def output(self, filename):
      totalzeros = 0.0
      totalentries = 0
      for i in range(len(self.ADJ)):
         sum = 0
         for j in range(len(self.ADJ[i])):
            if (self.ADJ[i][j] == 0):
               totalzeros += 1
            sum += self.ADJ[i][j]*self.ADJ[i][j] 
            totalentries += 1 
         if (sum != 0):
            print ("Inverse Simpson For Row  "+str(i)+" :  "+str(1.0/sum))
         else:
            print ("Zero Sum for Row  "+str(i))
      print (str(totalzeros/totalentries*100)+" % ZEROES")
