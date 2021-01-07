import sys
import random

string = str(sys.argv[1])
substr = string.split("@",1)
for x in range (100):
        lst = ['.']
        print(''.join("{}{}".format(x, random.choice(lst) if random.randint(0,1) else '') for x in substr[0])+ "@" + substr[1])
