from pylab import *
from plotter import *
import matplotlib.pyplot as plt


# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')  # Y-aksen
ax.spines['bottom'].set_position('zero')  # X-aksen
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


menu_items = {
    '1': plot1(False, plt),
    '2': plot2(False, plt),
    '3': plot3(False, plt),
    '4': plot4(False, plt),
    '5': plotderivative1(plt),
    '6': plotderivative2(plt),
    '7': plotderivative3(plt),
    '8': plotderivative4(plt),
    '9': plot1(True, plt),
    '10': plot2(True, plt),
    '11': plot3(True, plt),
    '12': plot4(True, plt)
}

print(
    "Meny:\n"
    "1. Plot 7x**2 − 8x + 1\n"
    "2. Plot sin(x)\n"
    "3. Plot (1 - x) / ((x + 3) ** 2)\n"
    "4. Plot sqrt(1 + (x ** 2))\n"
    "5. Plot den deriverte av 7x**2 − 8x + 1\n"
    "6. Plot den deriverte av sin(x)\n"
    "7. Plot den deriverte av (1 - x) / ((x + 3) ** 2)\n"
    "8. Plot den deriverte av sqrt(1 + (x ** 2))\n"
    "9. Plot 7x**2 − 8x + 1 med vekstrate\n"
    "10. Plot sin(x) med vekstrate\n"
    "11. Plot (1 - x) / ((x + 3) ** 2) med vekstrate\n"
    "12. Plot sqrt(1 + (x ** 2)) med vekstrate\n"
)

choice = input("Velg item: ")
plt = menu_items[input()]()

# show the plot
plt.legend(loc='lower right')
plt.show()
