from plotter import *

menuchoices = {
    '1': plot1,
    '2': plot2,
    '3': plot3,
    '4': plot4
}
print(
    "Meny:\n"
    "1. Plot 7x**2 − 8x + 1\n"
    "2. Plot sin(x)\n"
    "3. Plot (1 - x) / ((x + 3) ** 2)\n"
    "4. Plot sqrt(1 + (x ** 2))\n"
)

ret = menuchoices[input()]()
