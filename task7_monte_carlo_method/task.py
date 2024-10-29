import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_simulations):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

    probabilities = {sum_val: (count / num_simulations) * 100 for sum_val, count in sums_count.items()}

    return sums_count, probabilities

num_simulations = 100000

sums_count, probabilities = monte_carlo_simulation(num_simulations)

analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

print("Результати симуляції методом Монте Карло:")
for sum_val in range(2, 13):
    print(f"Сума: {sum_val}, Ймовірність (симуляція): {probabilities[sum_val]:.2f}%, Йомвірність (аналітика): {analytical_probabilities[sum_val]:.2f}%")

plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), alpha=0.6, color='blue', label='Монте-Карло')
plt.plot(analytical_probabilities.keys(), analytical_probabilities.values(), color='red', marker='o', label='Аналітичні')
plt.title("Ймовірності сум чисел при киданні двох кубиків")
plt.xlabel("Сума чисел")
plt.ylabel("Ймовірність (%)")
plt.legend()
plt.grid(True)
plt.show()
