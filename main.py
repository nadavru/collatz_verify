from tqdm import tqdm

def collatz(x):
    # The origin collatz function
    return x//2 if x%2==0 else 3*x+1

def modified_collatz(x):
    # Modified collatz function
    return x//2 if x%2==0 else 5*x+1

def verify_function(f, until=1000):
    # Check that eventually all numbers until the parameter gets to one, in O(n) complexity

    dict_check = {}
    dict_check[1] = [f(1),0]

    for i in tqdm(range(2,until+1)):
        curr = i
        memory = []
        while curr not in dict_check:
            memory.append(curr)
            after = f(curr)
            dict_check[curr] = [after,-1]
            curr = after
        if dict_check[curr][1] == -1:
            # circle, abort
            print(f"Found a circle: {curr} --> {curr}")
            ind = memory.index(curr)
            circle = memory[ind:] + [curr]
            print(f"Circle is: {circle}")
            return;
        else:
            last_num = dict_check[curr][1]
            for j in reversed(memory):
                last_num += 1
                dict_check[j][1] = last_num
    print("Success!")
    return dict_check


if __name__ == "__main__":

    # should be success
    verify_function(collatz, until=100000)

    # fails
    verify_function(modified_collatz, until=100000)