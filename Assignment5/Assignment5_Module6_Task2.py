Number=[1,2,3,4,5,6,7,8,9,10]
#print(type(Number))
print(f'Original list:{Number}')
order=Number[0:5:1]
print(f'Extracted first five elements:{order}')
reversed_number=order[::-1]
print(f'Reversed extracted elements:{reversed_number}')
