from src.common.database import Database


class Main(object):

    @classmethod
    def start_service(cls):
        card_number = input("Enter card Number: ")

        check_card_number = Database.find_one(query={"card_number": card_number})
        if check_card_number is not None:
            pin = input("Enter Pin: ")
            data = Database.find_one(query={"card_number": card_number, "pin": pin})
            if data is not None:
                print('___________________________________')
                print("Welcome {} ".format(data['name']).upper())
                print('___________________________________')

                Main.present_options(card_number, pin)
            else:
                print("invalid pin")
        else:
            print("Invalid card number")

    @staticmethod
    def present_options(card_number, pin):
        print("1. Deposite cash\n2. Withdraw cash\n3. Account enquiries\n4. Change pin")
        print('___________________________________\n')
        number = int(input(" Enter Option number: "))
        if number == 1:
            amount = int(input("Enter the amount to Deposit: "))
            data = Database.find_one(query={"card_number": card_number, "pin": pin})
            print("You are Depositing GHS {} into your account( {} )".format(amount, data['acc_number']))
            print("Do you wish to continue?\n1. YES\n2. NO")
            confirm_option = int(input(""))
            if confirm_option == 1:
                initial = Database.find_one(query={"card_number": card_number})
                Database.update_balance(card_number=card_number,
                                        pin=pin,
                                        amount=amount)
                updated = Database.find_one(query={"card_number": card_number})
                print("You have succesfully Deposited GHS {} into your account {}\nInitial balance: GHS {}\nNew Balance GHS {}\nLast Transaction date: {}".format(amount,
                                                                                                                                       updated['acc_number'],
                                                                                                                                       initial['balance'],
                                                                                                                                       updated['balance'],
                                                                                                                                       updated['last_transaction_date']))


            elif confirm_option == 2:
                print("Transaction cancelled")
                return None
            else:
                print("You have entered invalid response")
                return None

        elif number == 2:
            withdrawal_amount = int(input("Enter the amount to withdraw: "))
            data = Database.find_one(query={"card_number": card_number})
            print("You are withdrawing GHS {} from your account( {} )".format(withdrawal_amount, data['acc_number']))
            print("Do you wish to continue?\n1. YES\n2. NO")
            confirm_option = int(input(""))
            if confirm_option == 1:
                initial = Database.find_one(query={"card_number": card_number})
                if initial['balance']-5 >= withdrawal_amount:
                    Database.update_balance(card_number=card_number,
                                            pin=pin,
                                            amount=-withdrawal_amount)
                    updated = Database.find_one(query={"card_number": card_number})
                    print("You have succesfully withdrawn GHS {} from your account {}\nInitial balance: GHS {}\nNew Balance GHS {}\nLast Transaction date: {}".format(withdrawal_amount,
                                                                                                                                           updated['acc_number'],
                                                                                                                                           initial['balance'],
                                                                                                                                           updated['balance'],
                                                                                                                                           updated['last_transaction_date']))
                else:
                    print("Transaction failed! Your balance is insufficient")

            elif confirm_option == 2:
                print("Transaction cancelled")
                return None
            else:
                "You have entered invalid response"
                return None

        elif number == 3:
            data = Database.find_one(query={"card_number": card_number, "pin": pin})
            print("_____________________________")
            print('Name: {}\nAccount Number: {}\nCurrent Balance: {}\nLast transaction Date: {}'.format(data['name'], data['acc_number'], data['balance'], data['last_transaction_date']))
        elif number == 4:
            new_pin = input("Enter new pin: ")
            comfirm_new_pin = input("Enter new pin again: ")
            if new_pin == comfirm_new_pin:
                Database.update_pin(card_number=card_number, new_pin=new_pin)
                print("Pin changed successfully\nExiting app...\nRun app again")
                return None
            else:
                print('Pin does not match\nExiting app...')
        else:
            print("Invalid input")