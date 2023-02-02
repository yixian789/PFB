from pathlib import Path 
import csv

#define the profit loss function
def profitloss_function():
    """
    - This function woudld read a CSV file and calcualte if there are any cash defetits and cash surplus  
    """
    # create a file to csv file
    fp = Path.cwd()/"project_group"/"csv_reports"/"profit_loss.csv"
    #[ read the csv file to append day and net profit 
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        # Create a reader to read the csv
        reader = csv.reader(file)
        # skip header
        next(reader)
        # make output equals to an empty string
        Output = ""
        # Equate the previous net profit to 0 
        prev_net_profit = 0
        # set the check value to 0
        check = 0
        # Assign true to the variable called c
        c = True  
        # looping columns in reader 
        for column in reader:
            # equating current net profit to column 4 in the excel sheet and changing it to a float 
            curr_net_profit = float(column[4])
            # if the current net profit is less than previous net profit
            if prev_net_profit > curr_net_profit :
                # diffrence equals to previous net profit minus current net profit 
                diff = prev_net_profit - curr_net_profit
                # Increase the check value by 1 
                check += 1
                # Set the previous net profit to be equals to the current net profit 
                prev_net_profit = curr_net_profit
                # Set the c variable to False 
                c = False
                # make the output show the day and difference for net profit 
                Output += (f"[PROFIT DEFICIT] DAY:{column[0]}, AMOUNT: USD{diff}\n")
            # when the previous net profit is less than the current net profit 
            elif prev_net_profit < curr_net_profit:
                # Set the check value to 0
                check = 0
                # Equate the previous net profit to be equals to the current net profit  
                prev_net_profit = curr_net_profit
        # if variable c is true
        if c == True:
            # This statement will be printed 
            Output += ("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
        # return the output generated 
        return(Output)
