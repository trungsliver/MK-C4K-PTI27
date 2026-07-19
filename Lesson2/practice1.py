# Bài 1: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
hcn1 = Rectangle(5, 3)
print("Diện tích hình chữ nhật:", hcn1.area())
print("Chu vi hình chữ nhật:", hcn1.perimeter())
        
# Bài 2: Tạo lớp BankAccount với các thuộc tính: 
            # account_number: số tài khoản 
            # owner: tên chủ tài khoản
            # balance: số dư tài khoản
# Tạo phương thức:
            # deposit(amount): nạp tiền vào tài khoản
            # withdraw(amount): rút tiền từ tài khoản
            # display_balance(): hiển thị số dư tài khoản
            # (amount: số tiền nạp/rút theo đơn vị $)

class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        print('===== ACCOUNT INFO =====')
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}$")
        print('========================')

    def deposit(self):
        amount = float(input('Nhập số tiền nạp: $'))
        if amount <= 0:
            print('Số tiền nạp không hợp lệ')
        else:
            # Cộng tiền vào số dư tài khoản
            self.balance += amount
            print(f"Nạp tiền thành công!")
            # Hiển thị số dư tài khoản sau khi nạp tiền
            self.display_balance()

    def withdraw(self, amount:float):
        if amount <= 0:
            print('Số tiền rút không hợp lệ')
        elif amount > self.balance:
            print('Số dư tài khoản không đủ để rút')
        else:
            # Trừ tiền từ số dư tài khoản
            self.balance -= amount
            print(f"Rút tiền thành công!")
            # Hiển thị số dư tài khoản sau khi rút tiền
            self.display_balance()

acc1 = BankAccount('123', 'Vũ Hoàng', 100)
acc1.display_balance()
acc1.deposit()
acc1.withdraw(50)
acc1.withdraw(5000)  