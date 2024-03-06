import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def random_0to1():
    return random.uniform(0, 1)

def get_c1():
    rand_prob = random_0to1()
    ranges = [0, 0.1, 0.3, 0.7, 0.9]
    values = [43, 44, 45, 46, 47]
    c1 = np.interp(rand_prob, ranges, values)
    return c1

def get_c2():
    return np.random.normal(90, 5)

# Generate a random value for x from a normal distribution with mean 15000 and standard deviation 4500
def get_x():
    return np.random.normal(15000, 4500)

def simulate_profits(count, selling_price):
    direct_costs = [get_c1() for _ in range(count)]
    parts_costs = [get_c2() for _ in range(count)]
    demands = [get_x() for _ in range(count)]

    losses = 0
    profit_list = []
    for i in range(count):
        profit = ((selling_price - direct_costs[i] - parts_costs[i]) * demands[i]) - 1000000
        if profit < 0:
            losses += 1
        else:
            profit_list.append(profit)

    return direct_costs, parts_costs, demands, profit_list, losses

def print_statistics(profit_list, losses, count):
    max_profit = np.max(profit_list)
    min_profit = np.min(profit_list)
    average_profit = np.mean(profit_list)
    probability_of_loss = losses / count
    probability_of_profit = 1 - probability_of_loss

    print("Maximum Profit =", max_profit)
    print("Minimum Profit =", min_profit)
    print("Average Profit =", average_profit)
    print("Probability of Loss =", probability_of_loss)
    print("Probability of Profit =", probability_of_profit)

def save_to_excel(dataframes, file_path):
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        for name, df in dataframes.items():
            df.to_excel(writer, sheet_name=name, index=False)

def plot_histogram(data, xlabel, ylabel, title):
    plt.hist(data, density=True, bins=30)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def main():
    count = 10**6
    selling_price = 249
    direct_costs, parts_costs, demands, profit_list, losses = simulate_profits(count, selling_price)

    print_statistics(profit_list, losses, count)

    dataframes = {
        'c1': pd.DataFrame({'c1': direct_costs}),
        'c2': pd.DataFrame({'c2': parts_costs}),
        'x': pd.DataFrame({'x': demands}),
        'profit': pd.DataFrame({'profit': profit_list}),
    }

    save_to_excel(dataframes, 'Simulation_results.xlsx')

    plot_histogram(direct_costs, 'Values of c1', 'probability of c1', 'Histogram of c1')
    plot_histogram(parts_costs, 'Values of c2', 'probability of c2', 'Histogram of c2')
    plot_histogram(demands, 'Values of x', 'probability of x', 'Histogram of x')
    plot_histogram(profit_list, 'Values of the Profit', 'probability of profit', 'Histogram of Profit')

if __name__ == "__main__":
    main()



# import random
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Deterministic inputs
# Selling_Price = 249
# Administrative_Cost = 400000
# Advertising_Cost  = 600000
# totalFixedCost = Advertising_Cost + Administrative_Cost
#
# # Inputs
# count = 10**6
# mu, Sigma = 15000, 4500
#
# # List of randomly generated numbers
# directCost = list()
# partsCost = list()
# Demand = list()
# ProfitList = list()
#
# # Calculating C1,C2,X values with functions in terms of probability of each range
# def random_0to1():
#     return random.uniform(0, 1)
#
# def get_c1():
#   rand_prob=random_0to1()
#   if rand_prob>=0 and rand_prob<0.1:
#        c1=43
#   elif rand_prob>=0.1 and rand_prob<0.3:
#        c1=44
#   elif rand_prob>=0.3 and rand_prob<0.7:
#        c1=45
#   elif rand_prob>=0.7 and rand_prob<0.9:
#        c1=46
#   else :
#        c1=47
#   return c1
#
# def get_c2():
#     c2 = np.random.normal(90,5)
#     return c2
#
# def get_x():
#     x = np.random.normal(15000,4500)
#     return x
#
# # Array to get Lists with range of num of probabilities
# loss = 0
# Max = 0
# Min = 0
#
# for i in range(count):
#     # Counting number of trials to get average
#     c1 = get_c1()
#     directCost.append(c1)
#     c2 = get_c2()
#     partsCost.append(c2)
#     x = get_x()
#     Demand.append(x)
#     profit = ((249 - c1 - c2)*x) - 1000000
#     if profit < 0:
#         loss = loss + 1
#     else:
#         ProfitList.append(profit)
#     Max = max(profit, Max)
#     Min = min(profit, Min)
#
# # Outputs
# print("Maximum Profit = ", Max, "\n")
# print("Minimum Profit = ", Min, "\n")
# print("Average Profit = ", (sum(ProfitList)-loss)/len(ProfitList),"\n")
# print("Probability of Loss = ", loss/count, "\n")
# print("Probability of profit = ",1-(loss/count),"\n")
#
# # Create DataFrames from lists
# directCost_df = pd.DataFrame({'c1': directCost})
# partsCost_df = pd.DataFrame({'c2': partsCost})
# demand_df = pd.DataFrame({'x': Demand})
# profit_df = pd.DataFrame({'profit': ProfitList})
#
# # Save DataFrames to an Excel file
# with pd.ExcelWriter(r'C:\Users\nourh\Videos\result\Simulation_results.xlsx', engine="openpyxl") as writer:
#     directCost_df.to_excel(writer, sheet_name="c1", index=False)
#     partsCost_df.to_excel(writer, sheet_name="c2", index=False)
#     demand_df.to_excel(writer, sheet_name="x", index=False)
#     profit_df.to_excel(writer, sheet_name="profit", index=False)
#
#
#
# # Histograms
# plt.hist(directCost, density = True , bins = 30)
# plt.ylabel('probability of c1')
# plt.xlabel('Values of c1')
# plt.show()
#
# plt.hist(partsCost, density = True, bins = 30)
# plt.ylabel('probability of c2')
# plt.xlabel('Values of c2')
# plt.show()
#
# plt.hist(Demand, density = True, bins = 30)
# plt.ylabel('probability of x')
# plt.xlabel('Values of x')
# plt.show()
#
# plt.hist(ProfitList , density = True , bins = 30)
# plt.ylabel('probability of profit')
# plt.xlabel('Values of the Profit')
# plt.show()
#
