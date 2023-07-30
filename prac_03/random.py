import random
dir(random)

"""
What did you see on line 1?
#The number between 5 and 20.
What was the smallest number you could have seen, what was the largest?
#The smallest number is 5 and the largest is 20.

What did you see on line 2?
#The number between 3 and 10.
What was the smallest number you could have seen, what was the largest?
#The smallest number is 3 and the largest is 9. 
Could line 2 have produced a 4?
#No, because the range is 3 to 10 and the step is 2.

What did you see on line 3?
#The number between 2.5 and 5.5.
What was the smallest number you could have seen, what was the largest?
#The smallest number is 2.5 and the largest is 5.5.

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random
print(random.randint(1, 100))