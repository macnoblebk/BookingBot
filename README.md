# Booking.com Automation Bot

## Description
This project is a Selenium-based automation bot that interacts with Booking.com to search for properties, set travel dates, 
and apply filters (e.g., star rating and currency) during the booking process. The bot can be customized to suit various 
search requirements such as destination, party size, and more.

## Program Output
(Insert video Demo)

## Technologies and Skills 
- Programming Languages: Python, JavaScript
- Libraries/Modules: Selenium, PrettyTable
- Concepts: Web Automation, Object-Oriented Programming
- Tools: Command-line interface, ChromeDriver, Google Chrome


## Achievements and Contributions
- Successfully automated the process of searching for properties on Booking.com, including setting destinations, 
  selecting travel dates, and adjusting party size, without manual intervention.
- Implemented flexible date handling for check-in and check-out using multiple date formats, making the bot adaptable for 
  various input formats.
- Automated the selection of party size with logic to ensure valid guest counts, including adjusting adults using 
  interactive buttons dynamically.
- Enabled automatic currency change functionality, supporting different currencies based on user preference (defaulted to USD).
- Integrated property filter logic with support for star rating, allowing for refined search results based on user preferences.
- Built-in error handling for common scenarios like missing sign-in pop-ups and ensuring filters are applied only once 
  to avoid multiple clicks.

## Impact
- The automated bot reduces the need for manual searches on Booking.com, allowing users to find properties faster and more 
  efficiently. It can complete tasks like setting travel details, adjusting guest counts, and applying filters in a fraction 
  of the time it would take a human user.
- By automating repetitive tasks such as selecting dates, changing currencies, and filtering search results, the bot 
  ensures accuracy and consistency, reducing the risk of mistakes that could occur in manual booking searches.

## Future Enhancements
- Expand the range of filters to include price ranges, property types (e.g., hotels, apartments), and user review ratings.
- Implement sorting by different criteria such as price, distance from the city center, or guest ratings to provide more 
  refined search results.
- Add functionality to support searching for multiple destinations in a single session. This would allow users to automate 
  searches across multiple cities or regions without restarting the bot.
- Extend the project to support automation in other web browsers like Firefox, Safari, and Microsoft Edge by integrating 
  their respective WebDrivers. This will make the bot more versatile and platform-independent.
- Implement headless browsing to allow the bot to run in the background without opening a visible browser window. 
  This would be especially useful for large-scale automated testing and data extraction tasks.
- Improved Error Handling: Enhance the bot’s ability to handle errors gracefully, such as network issues, missing elements, 
  or changes in the website's structure. Provide detailed error messages and retry mechanisms.
- Logging and Monitoring: Add logging functionality to track the bot’s activities and detect issues during execution. 
  This would be useful for debugging and monitoring large-scale automation tasks.
- Integrate the bot with external APIs such as Google Maps or TripAdvisor to enrich the search results with additional 
  information like nearby attractions, transit options, and user reviews.
- Add functionality for automated price tracking, allowing users to monitor prices for specific hotels or destinations 
  over time and get notified of price drops or promotions.
- Develop a simple user interface where users can input their search preferences, such as destination, dates, and filters, 
  without needing to modify the code directly. This would make the bot more accessible to non-programmers.
- Implement parallel searches to run multiple instances of the bot simultaneously, allowing for faster processing of large 
  datasets or multiple destinations.
- Add functionality to export search results (e.g., hotel names, prices, ratings) to a CSV or Excel file for easy 
 analysis or reporting.