from calendar import c


def get_lowest_plush(data, plushie_id):
    returndict = {}
    middledict = {}
    for i in data["bazaar"]:
        middledict.update({"cost":i["cost"]})
        middledict.update({"quantity":i["quantity"]})
        returndict.update({plushie_id:[middledict]})
        return returndict

def sum_the_cost(data):
    sum = 0
    for i in data["plushies"]:
        for val in i.values():
            cost = val[0].get("cost")
            sum += cost
            break
    return sum

def lowest_quantity(data):
    lowest = 0
    for i in data["plushies"]:
        for val in i.values():
            current = val[0].get("quantity")
            if current < lowest or lowest == 0:
                lowest = current
                break
            break
    return lowest

def pretty_print_for_all_plushies(data):
    for i in data["plushies"]:
        print("")
        print(list(i)[0])
        for val in i.values():
            quantity = val[0].get("quantity")
            cost = val[0].get("cost")
            print(f"quantity : {quantity}\ncost : {cost}")