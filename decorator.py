import time

def calculate_time(sum1):
   def wrap(funct1):
      begin = time.time()
      sum1(funct1)
      finish = time.time()
      print(f"It took {finish - begin} sec.")
      return sum1(funct1)
   return wrap
@calculate_time
def sum1(n):
   result = 0
   for i in range(1, n + 1):
      result += i
   return result
if __name__ == '__main__':
    n = 1000000
    s = sum1(1000000)
    print(f'The sum of numbers from 1 to {n} is {s}.')