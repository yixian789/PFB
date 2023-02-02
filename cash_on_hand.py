from pathlib import Path 
import csv

#define the cash on hand function
def cash_on_hand_function():
    """
    - This function woudld read a CSV file and calcualte if there are any cash defetits and cash surplus  
    """
    # create a file to csv file
    fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"
    # read the csv file to append day and cash on hand 
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        # Create a reader to read the csv
        reader = csv.reader(file)
        # skip header 
        next(reader)
        # make output equals to an empty string 
        Output = ""
        # equate previous cash on hand to 0 
        prev_coh = 0
        # set the check value to 0 
        check = 0
        # Assign true to the variable called c
        c = True
        # looping columns in reader 
        for column in reader:
            # equating current cash on hand to column 2 in the excel sheet and changing it to a float 
            curr_coh = float(column[1])
            # if the current cash on hand is less than the previous cash on hand 
            if prev_coh > curr_coh:
                # difference equals previous cash on hand minus current cash on hand
                diff = prev_coh - curr_coh 
                # Increase the check value by 1 
                check += 1
                # Set the previous cash of hand to be equal to the current cash of hand
                prev_coh = curr_coh
                # Set the c variable to False
                c = False
                # make the output show the day and difference for cash on hand 
                Output += (f"[CASH DEFICIT] DAY:{column[0]}, AMOUNT: USD{diff}\n")
            # When the prev coh is less than the current coh 
            elif prev_coh < curr_coh:
                # Set the check value to 0 
                check = 0
                # Equate the previous coh to be equals to the current coh 
                prev_coh = curr_coh 
        # if the variable c is true
        if c == True: 
            # This statement will be printed 
            Output += ('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        # return the output generated 
        return(Output)
        

    


                

