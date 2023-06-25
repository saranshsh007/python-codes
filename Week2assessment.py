# # Q1
# import numpy as np

# def top_students(arr, k):
#     total_scores = np.sum(arr, axis=1)
    
#     sorted_indices = np.argsort(total_scores)[::-1]
    
#     top_indices = sorted_indices[:k]

#     return top_indices
# arr = np.array([[85, 90, 95],
#                 [70, 80, 75],
#                 [90, 92, 88],
#                 [60,75,80]])

# k = 2

# top_indices = top_students(arr, k)
# print(top_indices)


# # Q2

# class BankAccount:
#     def __init__(self, account_number, holder_name, balance=0):
#         self._account_number = account_number
#         self._holder_name = holder_name
#         self._balance = balance

#     @property
#     def account_number(self):
#         return self._account_number

#     @property
#     def holder_name(self):
#         return self._holder_name

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print("Insufficient balance.")

#     def inquire_balance(self):
#         return self._balance


# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, holder_name, balance=0, interest_rate=0):
#         super().__init__(account_number, holder_name, balance)
#         self._interest_rate = interest_rate

#     def calculate_interest(self):
#         return self._balance * self._interest_rate


# class CheckingAccount(BankAccount):
#     def __init__(self, account_number, holder_name, balance=0, transaction_limit=3):
#         super().__init__(account_number, holder_name, balance)
#         self._transaction_limit = transaction_limit
#         self._transaction_count = 0

#     def deposit(self, amount):
#         if self._transaction_count < self._transaction_limit:
#             super().deposit(amount)
#             self._transaction_count += 1
#         else:
#             print("Transaction limit exceeded.")

#     def withdraw(self, amount):
#         if self._transaction_count < self._transaction_limit:
#             super().withdraw(amount)
#             self._transaction_count += 1
#         else:
#             print("Transaction limit exceeded.")

#     def has_exceeded_transaction_limit(self):
#         return self._transaction_count >= self._transaction_limit



# # Creating bank accounts
# account1 = BankAccount("121324325", "Saransh Sharma", 1000)
# account2 = SavingsAccount("987654321", "Netra Sharma", 2000, 0.5)
# account3 = CheckingAccount("567890123", "Mannan Sharma", 1500, 2)

# # Performing operations on bank accounts
# account1.deposit(500)
# account1.withdraw(200)
# print("Account1 balance :",account1.inquire_balance())
# print("Account1 holder name : ",account1.holder_name)

# account2.deposit(1000)
# interest = account2.calculate_interest()
# print(f"Interest : {interest}")
# print("Account2 holder name : ",account2.holder_name)

# account3.deposit(100)
# account3.withdraw(300)
# print("Account3 balance : ",account3.inquire_balance())
# print("Account3 holder name : ",account3.holder_name)
# print(f"Exceeded transaction limit: {account3.has_exceeded_transaction_limit()}")



# # Q4
# def longest_substring(text, k):
#     if k <= 0:
#         return 0

#     max_length = 0
#     left = 0
#     char_count = {}
    
#     for right in range(len(text)):

#         char_count[text[right]] = char_count.get(text[right], 0) + 1

 
#         while len(char_count) > k:
#             char_count[text[left]] -= 1
#             if char_count[text[left]] == 0:
#                 del char_count[text[left]]
#             left += 1

    
#         max_length = max(max_length, right - left + 1)

#     return max_length
# text = 'abccabb'
# k = 2
# result = longest_substring(text, k)
# print("Longest Substring : ",result) 


# Q3

import sqlite3

def get_total_sales_by_country(country):
    # Connect to the database
    conn = sqlite3.connect('mydatabase_db')
    cursor = conn.cursor()

    # Execute the SQL query
    query = """
    SELECT SUM(total_amount)
    FROM order
    JOIN customers ON order.customer_id = customers.customer_id
    WHERE Customers.country = ?
    """
    cursor.execute(query, (country,))

    # Retrieve the result
    total_sales = cursor.fetchone()[0]

    # Close the database connection
    conn.close()

    return float(total_sales) if total_sales else 0.0
country = 'USA'
total_sales = get_total_sales_by_country(country)
print(f'Total sales for {country}: {total_sales}')
