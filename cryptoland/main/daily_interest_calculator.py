'''simple interest calculator '''
def daily_interest_calc(principal, time, rate, percentage_increase):
    '''variables'''
    # daily percentage rate
    daily_percentage_rate = percentage_increase / time / 100

    # amount invested daily 
    daily_invested_amount = daily_percentage_rate * principal 