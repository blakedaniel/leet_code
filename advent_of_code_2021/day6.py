from collections import Counter

fish = [3,3,5,1,1,3,4,2,3,4,3,1,1,3,3,1,5,4,4,1,4,1,1,1,3,3,2,3,3,4,2,5,1,4,1,2,2,4,2,5,1,2,2,1,1,1,1,4,5,4,3,1,4,4,4,5,1,1,4,3,4,2,1,1,1,1,5,2,1,4,2,4,2,5,5,5,3,3,5,4,5,1,1,5,5,5,2,1,3,1,1,2,2,2,2,1,1,2,1,5,1,2,1,2,5,5,2,1,1,4,2,1,4,2,1,1,1,4,2,5,1,5,1,1,3,1,4,3,1,3,2,1,3,1,4,1,2,1,5,1,2,1,4,4,1,3,1,1,1,1,1,5,2,1,5,5,5,3,3,1,2,4,3,2,2,2,2,2,4,3,4,4,4,1,2,2,3,1,1,4,1,1,1,2,1,4,2,1,2,1,1,2,1,5,1,1,3,1,4,3,2,1,1,1,5,4,1,2,5,2,2,1,1,1,1,2,3,3,2,5,1,2,1,2,3,4,3,2,1,1,2,4,3,3,1,1,2,5,1,3,3,4,2,3,1,2,1,4,3,2,2,1,1,2,1,4,2,4,1,4,1,4,4,1,4,4,5,4,1,1,1,3,1,1,1,4,3,5,1,1,1,3,4,1,1,4,3,1,4,1,1,5,1,2,2,5,5,2,1,5]

def fish_growth_slow(fish:list[int], days:int) -> int:
    for day in range(days):
        new_fish = []
        for idx in range(len(fish)):
            if fish[idx] == 0:
                new_fish.append(8)
                fish[idx] = 6
            else:
                fish[idx] -= 1
        fish.extend(new_fish)
    return len(fish)

def fish_growth(fish:list[int], days:int) -> int:
    fish = Counter(fish)
    fish[7] = 0
    fish[8] = 0
    
    for day in range(days):
        temp = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5] 
        fish[5] = fish[6]
        fish[6] = fish[7] + temp
        fish[7] = fish[8]
        fish[8] = temp
    return sum(fish.values())

print(fish_growth(fish, 256))