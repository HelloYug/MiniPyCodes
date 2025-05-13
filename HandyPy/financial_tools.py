# SuccessiveDiscount --> Calculates Successive discounts on a given amount.

def SuccessiveDiscount (DiscountList, Amount):
    '''
    Returns a tuple: (Total Discount Percent, Price After Discount, Discounted Amount).\n
    DiscountList --> Provide a list of the successive amount percentages.\n
    Amount --> Provide the amount on which the discount is to be calculated.\n
    Example;\n
    \tFunc([20, 25], 200) --> (40.0, 120.0, 80)
    \tFunc([8, 6, 2], 250) --> (15.25, 211.88, 38)
    '''
    s = 100
    for i in DiscountList:
        s -= i*s/100

    TotalDiscountPercent = round (100 - s, 2)
    PriceAfterDiscount = round (Amount * s / 100, 2)
    DiscountedAmount = round (Amount - PriceAfterDiscount)

    return TotalDiscountPercent, PriceAfterDiscount, DiscountedAmount