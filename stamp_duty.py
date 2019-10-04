%matplotlib
import numpy as np
import matplotlib.pyplot as plt
# I got the rules from here - https://www.thinkconveyancing.com.au/stamp-duty-calculator-nsw
price = np.linspace(650000, 850000, num=1000)
# Assuming a 5% deposit
deposit = price * 0.05
# Stamp duty for properties in that range
stamp_duty = 8990 + .045 * (price - 300000)
# First Home Buyers in NSW pay no stamp duty on properties costing $650,000
# Properties under $800,000 are charged a concessional rate
# Properties over $800,000 receive no discount
concession = np.zeros_like(price)
concession[price < 800000] = price[price < 800000] * .21 - 136510.
concession[0] = 0
stamp_duty[0] = 0
plt.plot(price, deposit + stamp_duty - concession)
plt.xlabel('House price')
plt.ylabel('Deposit + Stamp duty - Concession')
plt.title("Not so sure I've got these rules right")
