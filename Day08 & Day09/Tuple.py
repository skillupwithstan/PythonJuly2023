'''
sample_tuple = ("Arockia", "Kumar", "Rajesh")
print(sample_tuple)
print(len(sample_tuple))
#sample_tuple[2] = "Raja"
sample_tuple = (1,2,4)
print(sample_tuple)
print(sample_tuple[0])
#sample_tuple[0] = 5
#print(sample_tuple)
'''
sample_tuple = 1,2,4
sample_list = list(sample_tuple) 
print(type(sample_list))
print(sample_list)
print("BEFORE CHANGES:",sample_list[0])
sample_list[0] = 5
print("AFTER CHANGES:",sample_list)
