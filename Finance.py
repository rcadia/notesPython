#
# Hands on exercises # 3
# Modules - Finance
#
# Ross Alejandro A. Bendal
# Wednesday - June 19 2013 - 9:08
#
# Module that will be called in another python file.
def addTax(price,tax):
    newPrice = price / 100 * (100 + tax)
    return newPrice
