import matplotlib.pyplot as plt
import seaborn as sns
titanic = sns.load_dataset("titanic")

sns.countplot(x = "class",data=titanic)

plt.show()

number = input()


type(number)

dictionary = {"REG": "Regression",
               "LOG": "Logistic Regression",
               "CART": "Classification and Reg"}
dictionary["LOG"]


def calc(wage, hour):
  print(wage * hour)
calc(10, 40)-200



students = ["Denise", "Arsen", "Tony", "Audrey"]
low = lambda x: x[0].lower()
print(list(map(low, students)))


import random
def toss_coin():
  T = random. randrange(0,2)
  H = random. randrange(0,2)
  return T, H


toss_coin()




def sqr_root(x):
    sqr_r = x ** (1 / 2)

sqr_root(16)

import numpy as np
from functools import reduce
num_list = np.arange(10)
filter_list = list(filter( lambda x: x % 3 == 0,num_list))
final_list = reduce( lambda x,y: x * y,filter_list)

final_list

import numpy as np
serie = np.arange(1, 10 )
x = [3, 4, 5]
serie[x]


import seaborn as sns
df =sns. load_dataset( "titanic")
df [["sex", "survived"]].groupby("sex")