# Write your code here
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.money = 550
        self.cups = 9
        self.coffee_list = ('espresso', 'latte', 'cappuccino')
        self.coffee_price = (4, 7, 6)
        self.coffee_ingredients = ([250, 0, 16], [350, 75, 20], [200, 100, 12])
        self.state = 'stop'

    def machine_start(self):
        if self.state == 'stop':
            self.state = 'start'
            while self.state != 'stop':
                print('Write action (buy, fill, take, remaining, exit):')
                u_input = self.get_user_input('start', input())
                if u_input == 'buy':
                    self.state = 'buy'
                    self.buy()
                elif u_input == 'fill':
                    self.state = 'fill'
                    self.fill()
                elif u_input == 'take':
                    self.state = 'take'
                    self.take()
                elif u_input == 'remaining':
                    self.state = 'remaining'
                    self.remaining()
                elif u_input == 'exit':
                    self.state = 'stop'

    def get_user_input(self, state, str_):
        if state == self.state and self.state != 'stop':
            return str_

    def buy(self):
        if self.state == 'buy':
            str_ = '\nWhat do you want to buy?'
            n = 0
            for ls in self.coffee_list:
                n += 1
                str_ += ' {} - {},'.format(n, ls)
            str_ += ' back - to main menu:'
            print(str_)
            u_input = self.get_user_input('buy', input())
            if u_input != 'back':
                coffee = int(u_input) - 1
                if self.verify(coffee):
                    self.water -= self.coffee_ingredients[coffee][0]
                    self.milk -= self.coffee_ingredients[coffee][1]
                    self.coffee_beans -= self.coffee_ingredients[coffee][2]
                    self.cups -= 1
                    self.money += self.coffee_price[coffee]
                    self.state = 'start'
            else:
                print()
                self.state = 'start'

    def verify(self, coffee):
        if self.state == 'buy':
            verified = True
            if self.water < self.coffee_ingredients[coffee][0]:
                print('Sorry, not enough water!\n')
                verified = False
            if self.milk < self.coffee_ingredients[coffee][1]:
                print('Sorry, not enough milk!\n')
                verified = False
            if self.coffee_beans < self.coffee_ingredients[coffee][2]:
                print('Sorry, not enough coffee beans!\n')
                verified = False
            if not verified:
                self.state = 'start'
                return False
            print('I have enough resources, making you a coffee!\n')
            self.state = 'start'
            return True

    def fill(self):
        if self.state == 'fill':
            print('\nWrite how many ml of water do you want to add:')
            self.water += int(self.get_user_input('fill', input()))
            print('Write how many ml of milk do you want to add:')
            self.milk += int(self.get_user_input('fill', input()))
            print('Write how many grams of coffee beans do you want to add:')
            self.coffee_beans += int(self.get_user_input('fill', input()))
            print('Write how many disposable cups of coffee do you want to add:')
            self.cups += int(self.get_user_input('fill', input()))
            print()
            self.state = 'start'

    def take(self):
        if self.state == 'take':
            print('\nI gave you ${}\n'.format(self.money))
            self.money -= self.money
            self.state = 'start'

    def remaining(self):
        if self.state == 'remaining':
            print('\nThe coffee machine has:')
            print('{} of water'.format(self.water))
            print('{} of milk'.format(self.milk))
            print('{} of coffee beans'.format(self.coffee_beans))
            print('{} of disposable cups'.format(self.cups))
            print('${} of money\n'.format(self.money))
            self.state = 'start'


machine = CoffeeMachine()
machine.machine_start()
