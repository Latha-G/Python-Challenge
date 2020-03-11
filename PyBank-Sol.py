import os
import csv

total_months = 0
total_amount = 0

net_change = 0
net_change_total = 0

prev_net = 0

greatest_inc = 0
greatest_dec = 0

# Path to collect data from the Resources folder
file_to_read = os.path.join('Resources', 'Budget_Data.csv')

# Path to upload output
file_to_upload = os.path.join('Analysis' , 'PyBank_Results.txt')

# Read in the CSV file
with open(file_to_read, 'r') as csvfilehandle:

    # Split the data on commas
    csvfile = csv.reader(csvfilehandle, delimiter = ',')

    header = next(csvfile)

    # Loop through the data
    for row in csvfile:

        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        
        net_change = int(row[1]) - prev_net
        net_change_total = net_change_total + net_change
        
        #print(f' {row} - net_change = {net_change} \n )
        
        prev_net =  int(row[1])
        
        if net_change > greatest_inc:
            
            greatest_inc = net_change
            greatest_inc_month = row[0]
            
        if net_change < greatest_dec:
                       
            greatest_dec = net_change
            greatest_dec_month = row[0]
                       
    net_change_total = net_change_total - 867884
    average_change = round((net_change_total / (total_months - 1)),2)
        
    output = (
    f'\nFinancial Analysis    \n\n'
    f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n'
    f'Total months: {total_months} \n\n'
    f'Total Amount: {total_amount} \n\n'
    f'Average Change: {average_change} \n\n'
    f'Greatest Increase: {greatest_inc_month} (${greatest_inc})\n\n'
    f'Greatest Decrease: {greatest_dec_month} (${greatest_dec})\n\n'
    f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n'
    )
   
    print(output)
    
with open(file_to_upload, 'w') as txtfile:
    txtfile.write(output)
    


'''
Financial Analysis

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Total months: 86

Total Amount: 38382578

Average Change: -2315.12

Greatest Increase: Feb-2012 ($1926159)

Greatest Decrease: Sep-2013 ($-2196167)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''

