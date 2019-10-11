#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

Answer - The above program will run O(n) times because the while loop will run n^3/n^2 times which is equal to n times.
For every time the while loop runs, a increases by approximately n^2 times.

```python
b)  sum = 0 # O(c)
    for i in range(n): # O(n)
      j = 1 # O(c)
      while j < n: # O(n/2)
        j *= 2 # O(c)
        sum += 1 # O(c)
```

Answer - The above program will run:
    n * n/2 times (ignoring all constant time)
    => O(n^2)

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

Answer - The runtime of the above recursive function is linear O(n)
    This is because there is only one function call ber recursion.

## Exercise II

Lets take the building to be a list of stories of length `n`,
And since the stories are obviously ordered,
1 - We find out the middle of the list of stories `(n/2)`
2 - We drop an egg at the middle floor,
3 - if the egg breaks,
4 -    if the difference between top floor and the middle is <= 1,
5 -       return middle + 1
6 -    else we find the middle of the lower floors and repeat from step 2,
7 - else (if the egg does not break),
8 -    if the difference between the middle and the ground floor is <=1,
9 -       return middle - 1
10 -   else we find the middle of the upper floors and repeat from step 2
