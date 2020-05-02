from functools import wraps

def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
  """Print the sum of the two numbers """   
  print(a + b)
  
print_sum(15, 20)

print(print_sum.__name__)
print(print_sum.__doc__)

