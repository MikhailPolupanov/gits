def discounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
            raise ValueError("Максимальная скидка не должна быть больше 100")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return(price_with_discount)

print(discounted(100,5))
print(discounted(100,50))
print(discounted(100,59,max_discount=60))

product = {"name": "iPhone 12", "stock": 24, "price": 65432.5,"discount": 21}
product['with_discount'] = (discounted(product["price"], product['discount']))
print (product)