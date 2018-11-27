class Staff:
    def __init__(self, name, pay_rate, dependants, allowances):
        self.name = name
        self.pay_rate = pay_rate
        self.dependants = dependants
        self.allowances = allowances

    def __str__(self):
        res = "Name: {}".format(self.name)
        res += "\n"
        res += 'Pay rate: {}'.format(self.pay_rate)
        res += '\n'
        res += 'Dependants: {}'.format(self.dependants)
        res += '\n'
        res += 'Allowances: {:,.0f}'.format(self.allowances)
        return res

    def income(self):
        basic_pay = 1260000
        return self.pay_rate * basic_pay + self.allowances

    def taxable_incomes(self):
        return self.income() - 9000000 - self.dependants * 3600000

    def personal_tax(self):
        tax_income = self.taxable_incomes()
        if tax_income < 5 * 10e6:
            return min(tax_income * 5 / 100, 250000)
        if tax_income < 10 * 10e6:
            return min(tax_income * 10 / 100, 500000)
        if tax_income < 18 * 10e6:
            return min(tax_income * 15 / 100, 1200000)
        if tax_income < 32 * 10e6:
            return min(tax_income * 20 / 100, 2800000)
        if tax_income < 52 * 10e6:
            return min(tax_income * 25 / 100, 5 * 10e6)
        if tax_income < 80 * 10e6:
            return min(tax_income * 30 / 100, 8.4 * 10e6)
        return tax_income * 35 / 100

    def net_wage(self):
        return self.income() - self.personal_tax()

    def print_salary(self):
        print("Result".center(20, "-"))
        print(f"Income: {self.income():,.0f}")
        print(f"Taxable incomes: {self.taxable_incomes():,.0f}")
        print(f"Personal income tax: {self.personal_tax():,.0f}")
        print(f"Net wage: {self.net_wage():,.0f}")


if __name__ == '__main__':
    staff = Staff("Nguyen Van An", 2.67, 1, 12000000)
    print(staff)
    staff.print_salary()
