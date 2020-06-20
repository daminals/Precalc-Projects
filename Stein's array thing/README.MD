1. Between the numbers 1-100, there is a simple way to add up all the numbers in between. This is because, between these numbers, we are able to pair the numbers with their ‘opposites’ and multiply by pair numbers. For instance, 100 is paired with 1, adding up to 101. Then, 2 would be paired with 99, once again totalling 101. The pattern continues for 100/2, or 50. Therefore, we are able to attain the sum of these numbers through the equation(written in python) Solution = (n[0] + n[len(n)-1]) * (len(n)/2), where n is the array for all numbers. In this case, after plugging in the numbers, the solution is 5050.

    <img src=''>

2. In the previous question I explained it algorithmically using python-based abstraction. We can still evaluate the array through this method. In the array [n-3,n-2,n-1,n], we can still pair the first and last items, n-3 and n, and we get 2n-3. Following the pattern, adding n-2 with n-1, we STILL get 2n-3. Through the method, we get the answer 4n-6. Verifying the solution manually, n-3 + n-2 + n-1 + n = 4n-6. So to test our previous equation, (((n-3)+(n))*4/2)=4n-6. Perfect!

3. Our method theoretically should still work with arrays with an odd number of items. Testing it manually, 1+2+3 equals 6. Our method continues to evaluate correctly. 
    <img src=''>

    of course, one example is inconclusive evidence, so to test it twice more we must. 
    
    1+2+3+4+5 = 15
    <img src=''>
    
    But why stop at manual testing? Our updated algorithm now tests both methods, and evaluates them. Once again our method works marvelously. However a mere three examples are far from evidence. We can test this automatically
    
    <img src=''>
    <img src=''>
    
    Gif of automated tests, we are correct.
