immutable_var = 1, 5, 'apple', False
print(immutable_var)
#immutable_var[3] = 'peach'
#print(immutable_var) #кортеж не поддерживает назначение элементов
mutable_list = (['water', 45, 'tea'], 10)
print(mutable_list)
mutable_list[0][1] = 37
print(mutable_list)
