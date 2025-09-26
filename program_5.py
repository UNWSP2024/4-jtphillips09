# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.
#BEGIN
    #DECLARE budget AS FLOAT
    #DECLARE difference AS FLOAT
    #DECLARE spent AS FLOAT
    #DECLARE total AS FLOAT

    #SET spent TO 1.0          # initialize for loop
    #SET total TO 0.0

    # Ask user for budget
    #PROMPT "Enter your budget for the month: $"
    #READ budget

    # Loop to collect expenses
    #WHILE spent != 0 DO
        #PROMPT "Enter an expense (0 to quit): $"
        #READ spent
        #IF spent != 0 THEN
            #ADD spent TO total
        #ENDIF
    #ENDWHILE

    # Calculate difference
    #SET difference = budget - total

    # Display whether under, over, or exactly on budget
    #IF difference > 0 THEN
        #PRINT "You are under budget by $" + difference
    #ELSE IF difference < 0 THEN
        #PRINT "You are over budget by $" + ABS(difference)
    #ELSE
        #PRINT "You are exactly on budget"
    #ENDIF
#END


def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    # WRITE YOUR CODE HERE
    ######################
    budget = float(input("Enter your budget for the month: $"))

    while spent != 0:
        spent = float(input("Enter an expense (0 to quit): $"))
        if spent != 0:
            total += spent

    difference = budget - total

    if difference > 0:
        print(f"You are under budget by ${difference:.2f}.")
    elif difference < 0:
        print(f"You are over budget by ${-difference:.2f}.")
    else:
        print("You are exactly on budget.")

if __name__ == '__main__':
    main()
