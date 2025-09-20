# Drawing Patterns with Nested Loops
# This program draws a pattern using nested loops.
pattern =int(input("Enter the size of the pattern: "))
x = 0
while x < pattern:
    y = 0
    while y < pattern:
        print("*", end=" ")
        y += 1
    print()
    x += 1
    
#for x in range(pattern):
   # for y in range(pattern):
        #print("*", end=" ")
    #print()
      

        