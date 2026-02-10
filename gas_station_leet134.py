def compute_station_index(gas, cost):
    def is_starting_index_valid(gas, cost, start_index):
        start = True
        i =  start_index
        tank = gas[start_index]
        print(f"tank starting at {tank} at index {i}")
        while i != start_index or start:
            tank -= cost[i]
            print(f"moving to next station, consuming to {tank}")
            if tank < 0:
                print(f"not enough gas: {tank}")
                return False
            i += 1
            i %= (len(gas))
            tank += gas[i]
            print(f"moving, filling tank to {tank} at index {i}")
            start = False
        return True

    for rr in range(len(gas)):
        print('i ', rr)
        if is_starting_index_valid(gas, cost, rr):
            return rr
    return -1

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]

print("RESULT", compute_station_index(gas, cost))
