#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)I think it's O(n) because if n == 5, it takes 5 operations until the while loop breaks. If n == 10, it
would take 10 operations.

b)I think the for loop will go through and touch every element in the list and and double the value of j until it's bigger than n and then reset it, so it will touch every element no matter what (O(n)) then with the while loop running as many times as it needs until j > n makes it O(N x M)

c)The length of bunnies will decrement until it hits 0. Every time it decrements, it also returns a 2 which I believe is constant. So the runtime should be O(c n) because the function invokes itself for every value in the list and has a constant return right before each invocation.

## Exercise II

My initial thought was to drop from the first, then second, then third floor and so on, which may be logical in real life because you won't ever be able to drop an egg from higher than the first floor. But if the egg could survive a longer fall and n floors is arbitrary, I would use binary search and start at the middle and see if it breaks. If it didn't then I know the floor that will break it is located in the top half of the structure and 1 egg still didnt break. If it did then I'd go to half the height and try again, continuously cutting the floors involved in half. The runtime of this is O(log n).
