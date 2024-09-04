from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency("GBP")  # destination_field_clear() fails on commenting this line
    bot.set_destination("New York")
