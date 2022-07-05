p

from random import randint
class Banking_system:
    def __init__ (self):
        self.card_number = []
        self.pin_number = []
        self.inn = 0
    def main_welcome_screen(self):
        print("create account\n"
               "login account\n"
                "exit")
        main_menu_selection = str(input())
        if main_menu_selection == "1":
            self.create_account()
        if main_menu_selection == "2":
            self.account_login()
        if main_menu_selection == "3":
            exit()
    def create_account(self):
        print("enter your name")
        name = str(input())
        print("enter your card number")
        card_number = str(input())
        print("enter your pin)")
        pin_number = str(input())
        self.card_number.append(card_number)
        self.pin_number.append(pin_number)
        print("your account has been created")
        print("your card number is{}".format(card_number))
        print("your pin number is{}".format(pin_number))
        print("your balance is{}".format(self.inn))
        self.main_welcome_screen()
    def account_login(self):
        print("enter your card number")
        card_number = str(input())
        print("enter your pin")
        pin_number = str(input())
        if card_number in self.card_number:
            if pin_number in self.pin_number:
                print("you have succesfully logged in")
                self.account_balance()
            else:
                print("incorrect pim")
        else:
             print("incorrect card number")


                   
        self.main_welcome_screen()
    def account_balance(self):
        print("your balance is {}".format(self.inn))
        self.account_menu()
    def account_menu(self):
        print("1.withdraw\n")
        print("2.deposit\n")
        print("3.transfer\n")
        print("4.logout\n")
        print("5.delete account\n")
        print("6.exit\n")
        account_selection  = str(input())
        if account_selection == "1":
            self.withdraw()
        if account_selection == "2":
            self.deposit()
        if account_selection == "3":
            self.transfer()
        if account_selection == "4":
            self.logout()
        if account_selection == "5":
            self.delete()
        if account_selection == "6":
            exit()
            self.main_welcome_screen()

            

    def withdraw(self):
        print("enter the ammount you want to withdraw")
        withdraw = int(input())
        if withdraw > self.inn:
            print("insufficient funds")
        else:
            self.inn = self.inn - withdraw
            print("your balance is{}".format(self.inn))
        self.account_menu()
    def deposit(self):
        print("enter the amount you want to deposit")
        deposit = int(input())
        self.inn = self.inn + deposit
        print("your balance is{}".format(self.inn))
        self.account_menu()
    def transfer(self):
        print("entr the amount you want to transfer")
        transfer = int(input())
        if transfer > self.inn:
            print("insufficient funds")
        else:
            self.inn = self.inn - transfer
            print("your balance is{}".format(self.inn))
            self.account_menu()
    def logout(self):
        print("you have succesfully logged out")
        self.main_welcome_screen()
    def delete(self):
        print("enter your card number")
        card_number = str(input())
        
        if card_number in self.card_number:
            print("enter your pin")
            pin_number = str(input())
            if pin_number in self.pin_number:
                self.card_number.remove(card_number)
                self.pin_number.remove(pin_number)
                print("your account has been deleted")
            else:
                print("incorrect pin")

        else:
            print("incorrect card number")
            self.main_welcome_screen()
    def exit(self):
        exit()
        self.main_welcome_screen()
print(Banking_system().main_welcome_screen())


   











            









            


    