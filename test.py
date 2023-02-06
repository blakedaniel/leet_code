
list_one = ["black"] * 4  # reference
list_two = ["black" for c in range(4)]  # copy


for item1 in list_one:
    print('list_one:', id(item1))

print('-----------')

for item2 in list_two:
    print('list_two:', id(item2))
