
    
class Account:  
    def __init__(self, account_holder_name, amount_bal):
        self.pockets = {}
        self.account_holder_name = account_holder_name
        self.amount_bal = int(amount_bal)

    class Pocket:
        def __init__(self,pocket_name,pocket_amount, pin,parent,lock = False):
            """
            Args:
            pocket_name, pocket_amount, pin(4 digit), lock(bool)
            """
            self.pocket_name = pocket_name
            self.pocket_amount = int(pocket_amount)
            self.pin= int(pin)
            self.parent = parent
            self.lock = False
            if self.pocket_amount > self.parent.amount_bal:
                raise ValueError("The Value of Pocket is exceding the Amount Balance")
            else:
                self.parent.pockets[pocket_name] = pocket_amount
                self.parent.amount_bal -= self.pocket_amount

       # Helper Functions
        
        def verify_pin(self, entered_pin):
            if self.pin == entered_pin:
                return True
            return False
        
        # getter functions
        def get_balance(self):
            return self.parent.amount_bal
        
        def get_pockets(self):
            pockets_avaiable = [(key,value) for key,value in self.parent.pockets.items() if value!= 0]
            if len(pockets_avaiable) == 0:
                return "There are no pockets present at this time"
            else:
                return pockets_avaiable

        def get_account_details(self):
            return (self.parent.account_holder_name)

        #setter 
        def lock_pocket(self):
            if self.lock == False:
                self.lock = True
        
        def unlock_pocket(self):
            if self.lock:
                self.lock = False

        #Functions on Pockets

        def add_money_via_card_to_pocket(self):
            self.unlock_pocket()
            print("Please Enter your Card Number:")
            CardNumber = input()
            print("Please enter the pocket which you want to add money")
            pocket_to_add_money = input()
            print("Enter the amount you need to add")
            amount_to_add_money = int(input())
            self.add_money_to_pocket(pocket_to_add_money, amount_to_add_money, False, True)
        
        
        def add_money_to_pocket(self,pocket_name,amount,from_account_balance = True, from_card = False):
            if from_account_balance:
                if self.pocket_amount > self.parent.amount_bal:
                    raise ValueError("The Value of Pocket is exceding the Amount Balance")
                else:
                    self.parent.pockets[pocket_name] += int(amount)
                    self.parent.amount_bal -= int(amount)
            elif from_card:
                self.parent.pockets[pocket_name] += int(amount)
            else:
                self.add_money_via_card_to_pocket()
            self.lock_pocket()

        def withdraw_pocket(self,pocket_name):
            if self.lock:
                counter = 3
                while(counter):
                    print("Enter Pin to unlock the pocket")
                    entered_pin = int(input())
                    if self.verify_pin(entered_pin):
                        self.parent.pockets[pocket_name] = 0
                        print("The Pocket '{}' has been withdrawn".format(pocket_name))
                        del self.parent.pockets[pocket_name]
                        break
                    else:
                        print("The Pin is wrong! Try again. You have {} tries left".format(counter-1))
                        counter-=1
                if counter==0:
                    print("The Pocket is Locked for 24 Hours. You may try after 24 Hours")
            else:
                print("The pocket is not locked yet!")
            
            
            
                
        
        
    

    
account_one = Account("Shubham Uttarwar",1000)
pocket = account_one.Pocket("Credit Card",500,5732,account_one)
print(pocket.get_balance())
print(pocket.get_pockets())
print(pocket.get_account_details())
pocket.lock_pocket()
print(pocket.withdraw_pocket("Credit Card"))


