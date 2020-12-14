def check_even_list(num_list):
 for num in num_list:
  if num % 2 == 0:
   return True
 return False


def test(*args,**kwargs):
 print(args)
 print(kwargs)
 print('test')

test(name=1,'test',l=2,'t','fff',1.0, m=(1,2,3,4))

print(check_even_list([1,3,7,5]))
