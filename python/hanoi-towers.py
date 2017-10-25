class Tower:
  """The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower,[1] and sometimes pluralised) 
  is a mathematical game or puzzle. 
  It consists of three rods, and a number of disks of different sizes which can slide onto any rod. 
  The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest 
  at the top, thus making a conical shape.
  The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another 
       stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
    3. No disk may be placed on top of a smaller disk.
  
  This class will print out the moves that it takes to solve the puzzle"""

  def __init__(self):
        self.counter = 0

  def hanoi(self, n, org, aux, dst):
    """n: Number of disks (above a given level) to be moved
       org: origin rod
       dst: destination rod
       aux: auxiliary rod
       The key point to understand in the recursion is to think about the number of disks above a given level,
       not the amount of disks below a given level"""
    if n == 1: 
       self.counter += 1
       print('{0}->{1}'.format(org, dst))
    else:
       self.hanoi(n-1, org, dst, aux)
       self.hanoi(1, org, aux, dst)
       self.hanoi(n-1, aux, org, dst)

tower = Tower()
tower.hanoi(3, "org", "aux", "dst")
