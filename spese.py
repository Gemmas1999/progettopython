mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
spese = [820, 760, 910, 700, 680, 1250, 890, 1420, 730, 770, 800, 1100]
budget = 900

print ("Mesi sopra il budget")
for i in range(12):
    if spese[i]>budget:
        print(mesi[i], spese [i])
totale = sum(spese)
print ("totale dell'anno:", totale)

media=totale/12
print("media mensile:,", media)

                