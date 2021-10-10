# DECIDED NOT TO USE SEPARATE FNS FILE FOR MORE STREAMLINED CODING EXPERIENCE
# STILL, I WILL AMP MY PYTHON SKILLS AND COMPETENTLY NAVIGATE MULTI-FILE ORGANIZATION

# THIS SCRIPT CONTAINS ASSIGNMENTS & FUNCTIONS (w/COMMENTS)
# VISIT README FOR SUDO CODE OUTLINING STEP-BY-STEP

# assigns food cost value to user input
food_cost = float(input('Cost Minus Tip & Tax: $'))

# inform user 10% considered standard tip
# y/n option to calculate w/10% tip or other
standard_tip = .10
standard_tip_to_apply = (food_cost * standard_tip)/100

# specified_tip = input('Enter Tip to Apply: .')
specified_tip = float(int())
specified_tip_to_apply = (food_cost * specified_tip)/100

# calculate tip per user input and ensure y/n input
def apply_standard_tip():
    if apply_standard_tip == 'y\n':
        print(f'Tip Amount to Apply: ${standard_tip_to_apply}')
        print(f'Cost Plus Tip: {round(float(food_cost + standard_tip), 2)}')
        print(apply_standard_tip)
        
    elif apply_standard_tip == 'n':
        apply_standard_tip == specified_tip
        print(float(input('Enter 0 or 2-DIGIT Tax Percent: .')))
        print('\'ex. Enter 3 Percent as 03\'\n')
        print(f'Tip Amount to Apply: ${specified_tip * food_cost}')
        print(f'Cost Plus Tip: {round(float(food_cost + specified_tip), 2)}')
        print(specified_tip_to_apply)

    elif apply_standard_tip != 'y' or 'n':
        print(input('enter letter y or n only: \n'))
        print(apply_standard_tip)

    else:
        print('Run Error - Please Re-Try')
    


    # elif apply_standard_tip == 'n\n':
    #     print(f'Tip Amount to Apply: ${specified_tip_to_apply}')
        


# def standard_tip_applied():
#     if apply_standard_tip == 'y\n':
#         print(f'Tip to Apply: {round((food_cost * standard_tip), 2)}')
#         print(f'Cost Plus Tip: {round(float(food_cost + standard_tip), 2)}')
    

# tip_to_apply = round((food_cost * standard_tip), 2)
# cost_plus_tip = round(float(food_cost + tip_to_apply), 2)

   


    # while True:
        
    #     try:
    #         val = int(specified_tip)
    #         if val >= 0:
    #             break
    #         else:
    #             print('Percent Must Be Zero or More')
    #     except ValueError:
    #         print('Percent Must Be Numeric')

    # print(specified_tip_to_apply = round((food_cost * specified_tip), 2))

    # print(cost_plus_specified_tip = round(float(food_cost + specified_tip_to_apply), 2))


# def apply_specified_tip():
#     specified_tip = input(('Enter 0 or 2-DIGIT PERCENT: .'))
#     print('\'ex. Enter 3 Percent as 03\'')
#     specified_tip_to_apply = round((food_cost * specified_tip), 2)
#     cost_plus_specified_tip = round(float(food_cost + specified_tip_to_apply), 2)


# def percent_value():
#     while True:
#         percent = input('Enter Percent: ')
#         try:
#             val = int(percent)
#             if val >= 0:
#                 break
#             else:
#                 print('Percent Must Be Zero or More')
#         except ValueError:
#             print('Percent Must Be Numeric')
#     return val



