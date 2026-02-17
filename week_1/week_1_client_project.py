# Week-1 : Introduction to Python Programming
# Client Project : Calculation of Average Temperature

def calc_avg_temp():

    # store the temperature values in this variable
    temp_vals = []

    # collect number of readings to set the loop range
    n = int(input("Enter number of temperature readings:"))

    for i in range(n):
        # input manually
        temp = float(input(f"Enter temperature reading {i+1}: "))

        # insert in the declared variable
        temp_vals.append(temp)

    total = 0

    for t in temp_vals:
        total += t
    
    avg_temp = total / len(temp_vals)

    print("Temperature readings given : ", temp_vals)
    print("Average Temperature : ", avg_temp)


if __name__ == "__main__":
    calc_avg_temp()