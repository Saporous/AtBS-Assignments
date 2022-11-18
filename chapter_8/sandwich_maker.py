import pyinputplus as pyip

prices = {
    'wheat': .99,
    'white': .50,
    'sourdough': .99,
    'chicken': .99,
    'turkey': 1.25,
    'ham': 1.25,
    'tofu': .99,
    'cheddar': .50,
    'swiss': .50,
    'mozzarella': .50,
    'nocheese': 0
}

bread = pyip.inputMenu(['wheat','white','sourdough'],prompt='What type of bread?: ')
protein = pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt='What kind of protein?: ')
if pyip.inputYesNo(prompt='Cheese? (Yes/No): ') == 'yes':
    cheeseChoice = pyip.inputMenu(['cheddar','swiss','mozzarella'],prompt='Type of cheese?: ')
else: cheeseChoice = 'nocheese'
mayo = pyip.inputYesNo(prompt='Mayo? (Yes/No): ')
mustard = pyip.inputYesNo(prompt='Mustard? (Yes/No): ')
lettuce = pyip.inputYesNo(prompt='Lettuce? (Yes/No): ')
tomato = pyip.inputYesNo(prompt='Tomato? (Yes/No): ')
numSandwich = pyip.inputInt(prompt='How many sandwiches?: ')

totalCost = numSandwich * (prices[bread]+prices[protein]+prices[cheeseChoice])
print('Your total cost is: %s' %totalCost)