from plotter import *

menuchoices = {
    '1': plot1,
    '2': plot2,
    '3': plot3,
    '4': plot4,
    '5': plotderivative1,
    '6': plotderivative2,
    '7': plotderivative3,
    '8': plotderivative4,
    '9': vekst1,
    '10': vekst2,
    '11': vekst3,
    '12': vekst4,
    '13': feil1,
    '14': feil2,
    '15': feil3,
    '16': feil4
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
    "13. Plot feilverdi for den deriverte av 7x**2 − 8x + 1\n"
    "14. Plot feilverdi for den deriverte av sin(x)\n"
    "15. Plot feilverdi for den deriverte av (1 - x) / ((x + 3) ** 2)\n"
    "16. Plot feilverdi for den deriverte av sqrt(1 + (x ** 2))"
)

ret = menuchoices[input()]()
