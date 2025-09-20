# Drawing Patterns with Nested Loops
# This program draws a pattern using nested loops.
pattern =int(input("Enter the size of the pattern: "))
for x in range(pattern):
    for y in range(pattern):
        print("*", end=" ")
    print()   

        