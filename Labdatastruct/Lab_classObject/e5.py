class Email:
    def __init__(self):
        self.s = ''
        self.firstName = ''
        self.lastName = ''

    def E(self):
        if (not self.firstName) and (not self.lastName):
            print("'E' -> Email : Please Enter Your Firstname & Lastname")
        elif not self.firstName:
            print("'E' -> Email : Please Enter Your Firstname")
        elif not self.lastName:
            print("'E' -> Email : Please Enter Your Lastname")
        else:
            print(f"'E' -> Email : {self.s}")

    def A(self, s):
        self.firstName, self.lastName = list(map(cp, s.split()))
        self.s = f'{self.firstName.lower()}.{self.lastName.lower()}@kmitl.ac.th'

    def F(self, s):
        self.firstName = s.capitalize()
        if not ((not self.firstName) and (not self.lastName)):
            self.s = f'{self.firstName.lower()}.{self.lastName.lower()}@kmitl.ac.th'

    def L(self, s):
        self.lastName = s.capitalize()
        if not ((not self.firstName) and (not self.lastName)):
            self.s = f'{self.firstName.lower()}.{self.lastName.lower()}@kmitl.ac.th'

    def SA(self):
        if (not self.firstName) and (not self.lastName):
            print("'SA' -> Fullname : Please Enter Your Firstname & Lastname")
        elif not self.firstName:
            print("'SA' -> Fullname : Please Enter Your Firstname")
        elif not self.lastName:
            print("'SA' -> Fullname : Please Enter Your Lastname")
        else:
            print(f"'SA' -> Fullname : {self.firstName} {self.lastName}")

    def SF(self):
        if not self.firstName:
            print("'SF' -> Firstname : Please Enter Your Firstname")
        else:
            print(f"'SF' -> Firstname : {self.firstName}")

    def SL(self):
        if not self.lastName:
            print("'SL' -> Lastname : Please Enter Your Lastname")
        else:
            print(f"'SL' -> Lastname : {self.lastName}")

def cp(s):
    return s.capitalize()


def main():
    print('*** Create Email < BY KMITL > ***')
    a = input('Enter Input : ').split(',')
    e = Email()
    for i in a:
        if len(i.split()) == 1:
            if i == 'E':
                e.E()
            elif i == 'SA':
                e.SA()
            elif i == 'SL':
                e.SL()
            elif i == 'SF':
                e.SF()
            elif i == 'X':
                return
            else:
                print(f"'{i}' is Invalid Input !!!")
                return
        else:
            m = i.split()
            if m[0] == 'A':
                e.A('{} {}'.format(m[1], m[2]))
            elif m[0] == 'F':
                e.F(m[1])
            elif m[0] == 'L':
                e.L(m[1])
            else:
                print(f"'{i}' is Invalid Input !!!")
                return

main()
