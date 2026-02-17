# a append(add) new transaction and create new file if not available
def log_transaction(transaction_data):
    file=open("transaction_log4.txt", 'w')  # Open file in append mode
    file.write(transaction_data)

# Example usage
transaction_data = "Transaction details: [Account: e1120, Amount: $266]"

log_transaction(transaction_data)


def read_log_transaction():
    file=open("transaction_log4.txt", 'r')
    f=file.read()
    print(f)
    
read_log_transaction()

