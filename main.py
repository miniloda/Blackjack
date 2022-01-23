import random
from logo import logo
def sum_cards(lst1):
    sum = 0
    for i in lst1:
        sum += i
    return sum

#blackjack game
print(logo)
lst = [11,2,3,4,5,6,7,8,9,10,10,10,10]
game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )

while game == 'y':
    cards = []
    computer = []
    for i in range(0,2):
        temp = random.choice(lst)
        if temp == 11:
            yes = int(input("You have an Ace, do you want to treat it 11 or 1?: "))
            if yes == 11:
                cards.append(temp)
            else:
                cards.append(1)
        else:
            cards.append(temp)
    print("Your cards: "+ str(cards))
    temp=random.choice(lst)
    computer.append(temp)
    print("Computer's card: "+ str(computer))
    pass_card = input("Type 'y' to get another card, type 'n' to pass : ")
    if pass_card == 'y':
        temp=random.choice(lst)
        if temp == 11:
            yes = int(input("You have an Ace, do you want to treat it 11 or 1?: "))
            if yes == 11:
                cards.append(temp)
            else:
                cards.append(1)
        else:
            cards.append(temp)
    temp=random.choice(lst)
    computer.append(temp)
    your_sum = sum_cards(cards)
    computer_sum = sum_cards(computer)
    if computer_sum < 17:
        temp=random.choice(lst)
        if temp == 11:
            if temp+computer_sum<=21:
                computer.append(temp)
            else:
                computer.append(1)
    computer_sum = sum_cards(computer)
    print("Your card: " + str(cards))
    print("Computer's card: "+ str(computer))
    print("The sum of your cards is "+ str(your_sum) + " and the sum of the computer's card is "+ str(computer_sum) + ".")
    if your_sum > 21:
        print("You lose.")
    elif your_sum > computer_sum:
        print("You win.")
    elif your_sum < computer_sum:
        print("You lose.")
    elif your_sum == computer_sum:
        print("Draw.")
    game = input("Do you want to play again? Type 'y' or 'n': " )
