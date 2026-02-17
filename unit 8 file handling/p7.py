# a append(add) new transaction and create new file if not available
def log_transaction(transaction_data):
    file=open("transaction_log4.txt", 'a')  # Open file in append mode
    file.write(transaction_data)

# Example usage
transaction_data = "Transaction details: [Account: e250, Amount: $266]"
log_transaction(transaction_data)
