#exercise 1
def letter_indices(word):
    index_dict = {}
    for index, letter in enumerate(word):
        if letter in index_dict:
            index_dict[letter].append(index)
        else:
            index_dict[letter] = [index]
    return index_dict

word = input("Enter a word: ").strip()
indices_dict = letter_indices(word)
print(indices_dict)

#exercise 2
def parse_price(price_str):
    return float(price_str.replace('$', '').replace(',', ''))

def affordable_items(items, wallet):
    wallet_amount = parse_price(wallet)
    affordable = []

    for item, price_str in items.items():
        if parse_price(price_str) <= wallet_amount:
            affordable.append(item)

    if not affordable:
        return "Nothing"

    return sorted(affordable)

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
print(affordable_items(items_purchase, wallet))

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100"
print(affordable_items(items_purchase, wallet))

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1,200"
}

wallet = "$1"
print(affordable_items(items_purchase, wallet))
