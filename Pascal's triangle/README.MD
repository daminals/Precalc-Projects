<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/the%20assignment.png">


<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/1.png">

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/2.png">

Ok, this isn’t exactly what I wanted, but it’s actually really good because these are the numbers we have to add by in order to get the correct number

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/3.png">

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/4.png">

Hm, it’s getting closer but still not exactly what I want.

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/5.png">

Success!

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/6.png">

Added comments to explain the code. Well, now that it works, I suppose it should be translated into math as well 😢

Recursive: 

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/7.png">

This is meant in the sense that there are two formulas for the solution, where a(x) is the number we add by in order to get our solution, found by n(x)

Explicit

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/8.png">

I was going to try this but I realized that this is just the recursive formula with extra steps

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/9.png">

I remembered that an explicit function already exists for the sum of all integers that come before it, which we already derived in this class. The solution clearly was not as simple as just this formula since 2 is not in the sequence, but it is a start.

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/10.png">


Ok, so I configured the function to check the terms so I could see what the list was looking like, as well as added a comparison mechanism for me to check. The function currently is providing a list of all the terms we need to add in order to get the solution. It is a good starting point now that we have identified what exactly is going on.


<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/11.png">


Welp that didn’t work ://


Ok, I figured out how it works. Basically, I need to add all the previous terms in the sequence in order to get the correct answer. 

<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/12.png">


<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/13.png">


And this is my simplified recursive formula after the discovery made searching for the explicit formula:


<img src="https://github.com/daminals/Precalc-Projects/blob/master/Pascal's%20triangle/images/14.png">
