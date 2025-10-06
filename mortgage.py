# Assignment Part 1
import numpy_financial as npf

# Define the Mortgage_Payments class
class Mortgage_Payments:
    def __init__ (self, r, nper, years, P):
         self.r = r
         self.nper = nper
         self.years = years
         self.P = P
    def payment(self,r,years,P):
         Monthly_n = years * 12
         Semi_monthly_n = years * 24
         Bi_weekly_n = years * 26
         Weekly_n = years * 52

         eff_monthly_rate = ((effectiveRate)**(1/12)) - 1
         eff_semi_monthly_rate = ((effectiveRate)**(1/24)) - 1
         eff_bi_weekly_rate = ((effectiveRate)**(1/26)) - 1
         eff_weekly_rate = ((effectiveRate)**(1/52)) - 1

         if r == 1:
              return (
                   P/Monthly_n,
                   P/Semi_monthly_n,
                   P/Bi_weekly_n,
                   P/Weekly_n
                   )

         return (
              npf.pmt(eff_monthly_rate,Monthly_n,-P),
              npf.pmt(eff_semi_monthly_rate,Semi_monthly_n,-P), 
              npf.pmt(eff_bi_weekly_rate,Bi_weekly_n,-P), 
              npf.pmt(eff_weekly_rate,Weekly_n,-P),
              npf.pmt(eff_monthly_rate,Monthly_n,-P)/2,
              npf.pmt(eff_monthly_rate,Monthly_n,-P)/4
                )

# User inputs
P = float(input ("Please enter the principal amount ($):"))
r = float(input ("Please enter the quoted/prevailing interest rate (%):"))
years = float (input ("Please enter the amortization period in years:"))

# Calculate effective interest rate based on 2 compunding periods per year
annual_rate = r/100
effectiveRate  = ((1+ (annual_rate/2))**2)

# Define the object and calculate payments
Mortgage = Mortgage_Payments(effectiveRate, years*12, years, P)
monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly = Mortgage.payment(effectiveRate, years, P)

print(f"Monthly Payment: ${monthly:.2f}")
print(f"Semi-Monthly Payment: ${semi_monthly:.2f}")
print(f"Bi-Weekly Payment: ${bi_weekly:.2f}")
print(f"Weekly Payment: ${weekly:.2f}")
print(f"Rapid Bi-Weekly Payment: ${rapid_bi_weekly:.2f}")
print(f"Rapid Weekly Payment: ${rapid_weekly:.2f}")

print("-"*40)

# Assignment Part 2
import csv

# Define the Exchange_Rates class
class Exchange_Rates:
    def __init__(self,CAD,USD,amount, From, To):
        self.CAD = CAD
        self.USD = USD
        self.amount = amount
        self.From = From
        self.To = To
    def convert(self,From,To,amount):
        with open("BankOfCanadaExchangeRates.csv", mode='r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                self.CAD = row["USD/CAD"]
                self.USD = row["USD/CAD"]

        if From == "USD" and To == "CAD":
            return amount * float(self.CAD)
        elif From == "CAD" and To == "USD":
            return amount / float(self.USD)
        else:
            return "Error: Please enter a valid currency (USD/CAD)."

# User inputs
From = str(input ("Please enter the FROM currency (USD/CAD):"))
To = str(input ("Please enter the TO currency (USD/CAD):"))
amount = float (input ("Please enter the amount ($):"))

# Define the object and perform conversion
Exchange = Exchange_Rates(0,0,amount, From, To)
result = Exchange.convert(From, To, amount)
print(f"Converted Amount: {result:.2f} {To}")

print("-"*40)