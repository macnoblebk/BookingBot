from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_sign_in_info()
    bot.change_currency("USD")
    bot.set_destination("New York")
    bot.select_dates()
    bot.select_party_size(5)
    bot.click_search()
    bot.apply_filter()


