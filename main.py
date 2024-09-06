from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_sign_in_info()
    # bot.change_currency()  # StaleElementReferenceException if commented
    bot.set_destination("New York")
    bot.select_dates()
    bot.select_party_size(0)