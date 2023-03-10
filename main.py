import cash_on_hand, overheads, profit_loss

# create a main function 
def main():
    """
    - Main function will modularise our program by running all the functions and creating a summary report 
    """
    # let cash on hand value be equal to cash on hand function 
    cash_on_hand_value = cash_on_hand.cash_on_hand_function()
    # let overhead value be equal to overhead function 
    overhead_value = overheads.overhead_function()
    # let profit loss value be equal to profit loss function 
    profit_loss_value = profit_loss.profitloss_function()
    
    # create a txt file called summary report 
    with open('summary_report.txt', 'w') as file:
        # write inside the summary report y running the functions previously created 
        file.write(f"{overhead_value}{cash_on_hand_value}{profit_loss_value}")
#call the function         
main()
