import matplotlib.pyplot as plt
import visualiserfunctions

pricing_file = "csv_files/pricing.csv"

data = visualiserfunctions.get_data_from_pricing_file(pricing_file)
data.pop(0) # removing header

answer = input("What plushie would you want to look at.\n1.Camel\n2.Chamois\n3.Jaguar\n4.Kitten\n5.Lion\n6.Monkey\n7.Nessie\n8.Panda\n9.Red_Fox\n10.Sheep\n11.Stingray\n12.Teddy_bear\n13.Wolverine\n14.Sum\nAwnser : ")

X, Y = visualiserfunctions.get_query_plushie(data, int(answer))

print(X)
print(Y)

plt.plot(X,Y)
plt.show()
