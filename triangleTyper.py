def triangleChecker(one, two, three):
        if sorted([one, two, three])[0] + sorted([one, two, three])[1] < sorted([one, two, three])[2]:
            print ('Hey smarty pants, no triangle can be made from those side-lenghts!')
        elif one == two == three:
            print('That there is an Equalateral!')
        elif one == two or two == three or one == three:
            print('And she\'s an Isosceles!')
        else:
            print('Ah, another ugly duckling.  Just a Scalene!')


while True:
    one = input('Side one: ')
    two = input('Side two: ')
    three = input('Side three: ')
    triangleChecker(one, two, three)
