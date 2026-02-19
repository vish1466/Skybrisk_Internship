# Week 2 : Client Project

# Remove duplicates, filtering

def rem_duplic(a):
    return list(set(a))

# To filter a certain list of numbers, we need to set a threshold, which is going to be user specific

def filter_data(data, threshold):
    return [x for x in data if x >= threshold]



def main():
    thresh = float(input("Set a threshold value to filter the data : "))
    nums = list(map(int, input("Enter the numbers (separated with comma only) : ").split(",")))

    print("Given data : ", nums)
    print("Given threshold : ", thresh)

    # Remove the duplicates first
    print("Data without any duplicates : ",rem_duplic(nums))

    # Filter based on the threshold
    print("Filtered data : ", filter_data(nums, thresh))


if __name__ == "__main__":
    main()