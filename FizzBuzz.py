for count in range(1, 101):
   if count % 5 == 0 and count % 3 == 0:
       print "FizzBuzz"
   elif count % 5 == 0:
       print "Buzz"
   elif count % 3 == 0:
       print "Fizz"
   else:
       print count