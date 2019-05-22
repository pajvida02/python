import random ,sys

for i in range(5):
    print(random.randint(0,12))
response = input()
if response == 'exit':
    sys.exit()
print('you response'  + response + ',')
