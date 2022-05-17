import requests
import json
import calculators.Plushie_calculator as Plushie_calculator
import calculators.points_calculator as points_calculator
import calculators.misc_calculators as misc_calculators
import writers.csv_writer as writer

pricing_file = "csv_files/pricing.csv" #pricing file header timestamp,Camel,Chamois,Jaguar,Kitten,Lion,Monkey,Nessie,Panda,Red_Fox,Sheep,Stingray,Teddy_bear,Wolverine
plushie_dict = {}
plushie_ids = {"Camel":384, "Chamois":273, "Jaguar":258, "Kitten":215, "Lion":281, "Monkey":269, "Nessie":266, "Panda":274, "Red_Fox":268, "Sheep":186, "Stingray":618, "Teddy_bear":187, "Wolverine":261}

API_KEY = "npz0wZV93I0Bkjco"
for ke, val in plushie_ids.items():
    item_market_request = requests.get("https://api.torn.com/market/" + str(val) + "?selections=&key=" + API_KEY)
    item_market_d = json.loads(item_market_request.text)
    lowest = Plushie_calculator.get_lowest_plush(item_market_d,ke)
    if len(plushie_dict) < 1:
        plushie_dict.update({"plushies":[lowest]})
    else:
        plushie_dict["plushies"].append(lowest)

point_market_request = requests.get("https://api.torn.com/market/?selections=pointsmarket&key=" + API_KEY)
point_market_d = json.loads(point_market_request.text)

sum_of_all_plushies = Plushie_calculator.sum_the_cost(plushie_dict)
total_available_sets = Plushie_calculator.lowest_quantity(plushie_dict)
lowest_point_cost = points_calculator.get_lowest_point(point_market_d)
set_sell_value = points_calculator.get_set_value(lowest_point_cost)



Plushie_calculator.pretty_print_for_all_plushies(plushie_dict)
print("")
print(f"Sum of all plushies: {sum_of_all_plushies}")
print("")
print(f"Total available sets at the price of {sum_of_all_plushies} : {total_available_sets}")
print("")
print(f"Lowest price of points: {lowest_point_cost}")
print(f"Sell price of one set : {set_sell_value}")
print(f"Profit/loss on a set buy : {set_sell_value-sum_of_all_plushies}")
print("")
write_q = input("Do you want to write current statistics to pricing.csv? (Y/N) : ")

if write_q.lower() == "y":
    print("... Writing ...")
    f = writer.openfile(pricing_file)
    writer.write_data(f, plushie_dict)
    f.close()
 





