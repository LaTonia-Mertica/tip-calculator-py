# THROUGHOUT MY CODE BELOW ARE COMMENTS (NOT SUDO CODE)
# VISIT README FOR SUDO CODE OUTLINING STEP-BY-STEP

# import all functions from tip calculator fns script
# from tip_calculator_fns import *

# brief intro and app purpose

while (True):
    print('\n##############################################\n')
    print('TIP CALCULATOR: EASILY DETERMINE WHO PAYS WHAT')
    print('~ let\'s calculate how to split the bill ~')
    print('\n##############################################\n')

    # assigns food cost value to user input
    food_cost = float(input('Cost Minus Tip & Tax: $'))

    # print food_cost()to test
    print(f'Food Cost: ${food_cost}')

    # inform user 10% considered standard tip
    print('\nSTANDARD TIP IS 10 PERCENT')

    standard_tip = .10
    # code below possibly contributes to compounded rounding issue that throws off outputs
    standard_tip_to_apply = round((food_cost * standard_tip), 2)
    cost_plus_stanTip = round((food_cost + standard_tip_to_apply), 2)
    # tested code below to try to get same results as use cases provided in canvas
    # standard_tip_to_apply = food_cost * standard_tip
    # cost_plus_stanTip = food_cost + standard_tip_to_apply

    # printed three below to test
    # print(standard_tip)
    # print(standard_tip_to_apply)
    # print(cost_plus_stanTip)

    # calculate tip per user input and ensure y/n input
    apply_standard_tip = (input('Apply 10% Tip? y/n '))
    if apply_standard_tip == 'y':
        print(f'Applying {standard_tip}% Tip')
        print(f'Tip Amount to Apply: ${standard_tip_to_apply}')
        print(f'Cost Plus Tip: ${cost_plus_stanTip}')

        num_peo_split_cost = int(input(f'People Splitting Cost: '))
        print(f'COST PER PERSON: ${round((cost_plus_stanTip / num_peo_split_cost), 2)}')

        print(f'\n10% TAX ADDED FOR TOTAL COST')
        total_cost = float(cost_plus_stanTip * .10) + cost_plus_stanTip
        print(f'TOTAL COST: ${round(total_cost, 2)}')

    # accept and calculate specified tip
    elif apply_standard_tip == 'n':
        print(f'\nEnter 0 or 2-DIGIT Tip Percent')
        print('\'ex. enter 3 percent as 03\'\n')

        specified_tip = int(input('Tip Percent: .'))
        # code below possibly contributes to compounded rounding issue that throws off outputs 
        specified_tip_to_apply = round((food_cost * specified_tip)/100, 2)
        cost_plus_specTip = round((food_cost + specified_tip_to_apply), 2)
        # tested code below to try to get same results as use cases provided in canvas
        # specified_tip_to_apply = food_cost * specified_tip
        # cost_plus_specTip = food_cost + specified_tip_to_apply

    # printed three below to test
    # print(specified_tip)
    # print(specified_tip_to_apply)
    # print(cost_plus_specTip)
        
        # print(float(input('Tip Percent: .')))
        print(f'Applying {specified_tip}% Tip')
        print(f'Tip Amount to Apply: ${specified_tip_to_apply}')
        print(f'Cost Plus Tip: {round(cost_plus_specTip, 2)}')

        # num_peo_split_cost = int(input('Tip Percent: .'))
        num_peo_split_cost = int(input(f'People Splitting Cost: '))
        print(f'COST PER PERSON: ${round((cost_plus_stanTip / num_peo_split_cost), 2)}')
        
        print(f'\n10% TAX ADDED FOR TOTAL COST')
        total_cost = float(cost_plus_specTip * .10) + cost_plus_specTip
        print(f'TOTAL COST: ${round(total_cost, 2)}')

    elif apply_standard_tip != 'y' or 'n':
        print(input('enter letter y or n only: \n'))
        print(apply_standard_tip)

        if apply_standard_tip != 'y' and 'n' == True:
            print(input('enter letter y or n only: \n'))

        else:
            print(input('you must enter the letter y or n: \n'))