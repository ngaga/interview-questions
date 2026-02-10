def compute_station_index(gas, cost):
    def is_starting_index_valid(gas, cost, start_index):
        tank = gas[start_index]
        print(f"tank {tank}")
        if tank <= 0:
            return False
        tank -= cost[start_index]
        i = (start_index + 1) % (len(gas) - 1)
        while i != start_index:
            print('nextI', i)
            tank += gas[i]
            print(f"tank {tank}")
            if tank <= 0:
                return False
            tank -= cost[i]
            i += 1
            i %= (len(gas) - 1)
        return True

    for i in range(len(gas)):
        print('i ', i)
        if is_starting_index_valid(gas, cost, i):
            return i
    return -1

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]

print("RESULT", compute_station_index(gas, cost))
