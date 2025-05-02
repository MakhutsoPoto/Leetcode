class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        store = []
        for n in range(1,n+1):
            if n %5 == n %3==0:
                store.append("FizzBuzz")
            elif n % 3 == 0:
                store.append('Fizz')
            elif n % 5 == 0 :
                store.append('Buzz')
            else:
                store.append(str(n))
        return store