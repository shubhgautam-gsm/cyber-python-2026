# Define a custom exception for insufficient funds
class InsufficientFundsError(Exception):
    """Exception raised when a user attempts to withdraw more than the available balance."""
    
    def __init__(self, balance, amount):
        """
        Initialize the exception with the user's balance and attempted withdrawal amount.
        
        Args:
        balance (float): Current balance in the user's account.
        amount (float): The amount the user is trying to withdraw.
        """
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} failed. Current balance is {self.balance}."
        super().__init__(self.message)

    def __str__(self):
        """Return a string representation of the error."""
        return self.message


# Simulate a bank account
class BankAccount:
    def __init__(self, balance):
        """Initialize a bank account with a given balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Attempt to withdraw money from the account."""
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance is {self.balance}.")


# Example of using the BankAccount class and handling the exception
def main():
    # Create a BankAccount with an initial balance
    account = BankAccount(1000.00)

    try:
        user=float(input('give amount which u want to withdraw:'))
        # Attempt to withdraw more money than is available
        account.withdraw(user)
        
    except InsufficientFundsError as e:
        # Handle the exception if funds are insufficient
        print(f"Error: {e}")

    try:
        user=float(input('give amount which u want to withdraw:'))

        # Attempt to withdraw a valid amount
        account.withdraw(user)
    except InsufficientFundsError as e:
        # Handle any exceptions if they occur
        print(f"Error: {e}")


if __name__ == "__main__":
    main()



# 55000 (1)- chor (2) - tamara lagan(3)


