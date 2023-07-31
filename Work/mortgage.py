# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

# Exercise 1.8
# Add 1000$/month more payment for firt 12 months

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# extra_payment = 1000.0
# extra_months = 12
# months_paid = 0

# while principal > 0:
#     if extra_months > 0:
#         principal = principal * (1+rate/12) - (payment + extra_payment)
#         total_paid = total_paid + payment + extra_payment
#         extra_months -= 1
#         months_paid += 1
#     else:
#         principal = principal * (1+rate/12) - payment
#         total_paid = total_paid + payment
#         months_paid += 1

# print('Total paid', total_paid)
# print('Months paid', months_paid)

# Exercise 1.9
# Make program more flexible for extra payment

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months_paid = 0

while principal > 0:
    months_paid += 1
    if months_paid >= extra_payment_start_month and months_paid <=extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)
print('Months paid', months_paid)