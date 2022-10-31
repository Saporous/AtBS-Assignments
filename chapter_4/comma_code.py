spam = ['apples', 'bananas', 'tofu', 'cats']

if len(spam) == 0:
    print("The list is empty")
elif len(spam) == 1:
    print(spam[0])
else:
    for i in range(len(spam)-1):
        print(spam[i], sep=',', end=' ')
    print('and ' + str(spam[len(spam)-1]))