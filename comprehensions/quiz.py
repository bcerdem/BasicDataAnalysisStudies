names = ["denise", "jean", "fleur"]
ages = [20,32,45]
cities = ["lyon","lille","nantes"]

list(zip(names,ages,cities))
############################################################
wages = [1000,2000,3000,4000,5000]
new_wages = lambda x : x*0.20 + x
list(map(new_wages,wages))
############################################################
students = ["Denise","Arsen","Tony","Audrey"]
low = lambda  x : x[0].lower()
print(list(map(low,students)))
############################################################
dictn = {"Denise": 10, "Arsen": 12, "Tony": 15, "Audrey":17}
new_dict = {k: v * 2 + 3 for (k,v) in dictn.items()}
new_dict
############################################################
numbers = range(1,10)
{n: n **2 for n in numbers if n % 2 != 0}