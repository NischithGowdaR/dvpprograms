import matplotlib.pyplot as plt

cars = ['Mercedes', 'BMW', 'Audi', 'Tata', 'Kia', 'Bolero', 'Hyundai']
data = [20, 30, 60, 70, 90, 100, 70]

plt.figure(figsize=(10, 5))
plt.pie(data, labels=cars)
plt.title("Nischith Gowda R - 1K23CS122")
plt.show()