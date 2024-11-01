

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbetrs separated by commas (e.g. 5, 67, 32)")

def calc_average(items):
    n = len(items)
    total_sum = sum(items)
    return total_sum/n

def get_user_input():
    print("get_user_input")
    x = input()
    split_x = x.split(",")
    float_x = [float(item) for item in split_x]
    return float_x


def find_min_max(items):
    print("find_min_max")
    return [min(items), max(items)]

def sort_temperature(items):
    print("sort_temperature")
    items.sort()
    return items

def calc_median_temperature(items):
    middle_index = round(len(items)/2) #find the middle index 
    return items[middle_index]
    

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    [min_val, max_val] = find_min_max(num_list)
    num_list.sort() #sort temperature
    index = 9
    while(index != 0):
        print("1 -> Calcualte Average")
        print("2 -> Max")
        print("3 -> Min")
        print("4 -> Median")
        print("0 -> Exit")
        choice = int(input())
        if (choice == 1):
            print("Average value : ", str(calc_average(num_list)))
        elif (choice == 2):
            print("Maximum value : ", max_val)
        elif (choice == 3):
            print("Minimum value : ", min_val)
        elif (choice == 4):
             print("Median value : ", calc_median_temperature(num_list))
        elif (choice == 0):
            index = 0
        else: print ("No such options")

    
    print("Program ended")

if __name__ == "__main__":
    main()