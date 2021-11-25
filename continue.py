

manifest = [('bannas', 15), ('mattresses', 34), ('palm_oil', 42), ('machine', 120)]

weight1 = 0
items = []
for cargo_name, cargo_weight in manifest:
    print('Current weight: {}'.format(weight1))
    if weight1 >= 100:
        print('Breaking from the loop now')
        break
    elif weight1 + cargo_weight > 100:
        print('Skipping {} ({})'.format(cargo_name,cargo_weight))
        continue
    else:
        print('Adding {} ({})'.format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight1 = weight1 + cargo_weight 
        
print('\nFinal Weight: {}'.format(weight1))
print('Final items: {}'.format(items))




headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for ticker1 in headlines :
    news_ticker = news_ticker + ticker1 + ' '
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
print(news_ticker)


news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


