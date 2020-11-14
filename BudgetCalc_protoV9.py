name = "budget calc for poor old hags"
print(name.upper() + "\n")
#all financial accounts, numbers and relations fictional

#date and time to display current date, link fixed costs to it and auto substract them
import datetime
import time

today = datetime.datetime.today()
print("STATUS:\n" + today.strftime("%Y-%m-%d\n"))

#to be adjusted monthly depending on circumstances
income = 1000
monthly_brut_budget = income

#fixed costs
rent = 400
rentdate = datetime.datetime.strptime('01/10/2020', "%d/%m/%Y")
print("Rent date: ")
print(rentdate)

#loan to be set to -60 from Nov on!
loan = 60
loandate = datetime.datetime.strptime('01/10/2020', "%d/%m/%Y")
print("loan date: ")
print(loandate)

audible = 9.95
audibledate = datetime.datetime.strptime('04/10/2020', "%d/%m/%Y")
print("Audible date: ")
print(audibledate)

prime = 7.99 
primedate = datetime.datetime.strptime('11/10/2020', "%d/%m/%Y")
print("Prime date: ")
print(primedate)

netflix = 15.59
netflixdate = datetime.datetime.strptime('23/10/2020', "%d/%m/%Y")
print("Netflix date: ")
print(netflixdate)

#add when date set
#warranty_lt = 6.99
#warranty_lt_date = datetime.datetime.strptime('23/10/2020', "%d/%m/%Y")
#print("Warranty LT date: ")
#print(warranty_lt_date)

endofmonth = datetime.datetime.strptime('31/10/2020', "%d/%m/%Y")

#extra costs - not automatically subtracted on a date, but used in daily/weekly net calcs (optional)
luxuries = 75

print("\n----------------------------------------\n")

#calculate approx weekly net budget
#add warranty_lt when date set
monthly_net_budget = income - (rent + loan + audible + prime + netflix + luxuries)

print("---OCTOBER 2020---\n")
print("Monthly Netto Budget: \n {:0.2f} Euro.".format(monthly_net_budget) + "\n(fix costs decucted for netto prognosis; \nwill be substracted automatically below)\n")
days_10 = 31
weeks_10 = 4.5
daily_net_budget_10 = monthly_net_budget / days_10
weekly_net_budget_10 = monthly_net_budget / weeks_10
print("Daily Netto Budget September 2020: \n {:0.2f} Euro.".format(daily_net_budget_10) + "\n")
print("Weekly Netto Budget September 2020: \n {:0.2f} Euro.".format(weekly_net_budget_10) + "\n")

print("\n----------------------------------------\n")


status_9 = 300
status_10 = status_9
print("Account starting Oct20 \n(former status minus monthly brut income): \n {:0.2f} Euro.".format(status_10) + "\n")

spent_10 = [-13.7, -3.6, -34.26, -2.5]
spent_10 = sum(spent_10)

#either 
# a) add to earned_10 if displayed in account, or 
# b) add here if received in cash and substract immediataley by also adding it to spent_10 negatively
earned_10 = [20, 80, 30]
earned_10 = sum(earned_10)

balance_10 = spent_10 + earned_10
print("Money spent in September so far: \n {:0.2f} Euro.".format(spent_10) + "\n")
print("Money earned in September so far: \n {:0.2f} Euro.".format(earned_10) + "\n")
print("(---> Balance: {:0.2f} Euro)\n".format(balance_10))

if today >= rentdate and today < audibledate:
  status_10 = status_10 - rent - loan
  print("Rent and loan have been charged.")

if today >= audibledate and today < primedate:
  status_9 = status_10 - audible - rent - loan
  print("Rent, loan and Aubible have been charged.")

if today >= primedate and today < netflixdate:
  status_9 = status_10 - prime - audible - rent - loan
  print("Rent, loan, Audible and Prime have been charged.")

if today >= netflixdate and today < loandate:
  status_9 = status_10 - netflix - prime - audible - rent - loan
  print("Rent, loan, Audible, Prime and Netflix have been charged.")

end_1 = datetime.datetime.strptime('08/10/2020', "%d/%m/%Y")
end_2 = datetime.datetime.strptime('15/10/2020', "%d/%m/%Y")
end_3 = datetime.datetime.strptime('22/10/2020', "%d/%m/%Y")
end_4 = datetime.datetime.strptime('29/10/2020', "%d/%m/%Y")
end_5 = datetime.datetime.strptime('31/10/2020', "%d/%m/%Y")

if today > end_1 and today < end_2:
  print("You reached past week one.\n")
elif today > end_2 and today < end_3:
  print("You reached past week two.\n")
elif today > end_3 and today < end_4:
  print("You reached past week three.\n")
elif today > end_4 and today < end_5:
  print("You reached past week four.\n")
elif today > end_5:
  print("The month has ended. This is your final balance:\n")
else:
  print("Still in week one... behave.")

if weekly_net_budget_10 > abs(balance_10):
  print("You spent {:0.2f} Euro and earned {:0.2f} Euro so far. Your cost balance is {:0.2f}. \nYou are still below your first weekly allowence - great, keep saving!".format(spent_10, earned_10, balance_10) + "\n")
elif weekly_net_budget_10 <= abs(balance_10) and abs(balance_10) < 2 * weekly_net_budget_10:
  print("You spent {:0.2f} Euro and earned {:0.2f} Euro so far. Your cost balance is {0.2f}. \nYou exceeded your first weekly allowence for this month.".format(spent_10, earned_10, balance_10) + "\n")
elif 2 * weekly_net_budget_10 <= abs(balance_10) and abs(balance_10) < 3 * weekly_net_budget_10:
  print("You spent {:0.2f} Euro and earned {:0.2f} Euro so far. You exceeded your second weekly allowence for this month".format(spent_10, earned_10, balance_10) + "\n")
elif 3 * weekly_net_budget_10 <= abs(balance_10) and abs(balance_10) < monthly_net_budget:
  print("You spent {:0.2f} Euro and earned {:0.2f} Euro so far. Your cost balance is {:0.2f}. \nYou exceeded your third weekly allowence for this month".format(spent_10, earned_10, balance_10) + "\n")
elif monthly_net_budget == abs(balance_10):
  print("You have spent all allowence for this month - not a penny more!\n")
else:
  print("You spent {:0.2f} Euro and earned {:0.2f} Euro so far. Your cost balance is {:0.2f}. \nYou exceeded your allowence - this means more saving next month!".format(spent_10, earned_10, balance_10) + "\n")

status_10 = status_10 - spent_10 + earned_10
print("\nACCOUNT AT THE END OF Sept20: \n {:0.2f} Euro.".format(status_10) + "\n")