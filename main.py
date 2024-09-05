from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_sign_in_info()
    # bot.change_currency()  # StaleElementReferenceException if commented
    bot.set_destination("New York")
    # bot.select_dates(check_in_date='2024-09-04', check_out_date='2024-09-14')
    bot.select_dates()
