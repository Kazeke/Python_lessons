class BankAccoun:
    def __init__(self):
        self.accountNumber = 10
        self.name = 'Kazeke'
        self.balance = 0
    
    def Deposit(self):
        popolnenie = float(input('Vvedite summu: '))
        self.balance = self.balance + popolnenie
        print('Na s4et za4isleno: ', popolnenie)

s = BankAccoun()
s.Deposit()