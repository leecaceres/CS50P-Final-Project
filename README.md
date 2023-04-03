# CS50P-Final-Project

Program that uses an API to tell user their horoscope based on their birth month and day.

I created a program where the user inputs their date of birth (dob) and used regex to allow multiple date formats:
- variations of mm/dd/yyyy
- variationf of month dd, yyyy
- variations of dd month yyyy

From the user's dob, the month and day were extracted and used to iterate through data on the astrological sun signs.
- Sign and symbol found for each user

The user is asked which horoscope they would like to see:
- Daily
- Weekly
- Monthly

If the user chooses Daily, they are asked again to choose:
- Today's
- Tomorrow's
- Yesterday's

Then, a get request to a locally hosted Horoscope API is executed based on user's choice– 
(API not included, I created it using this tutorial: https://www.freecodecamp.org/news/python-project-build-an-api-with-beautiful-soup-and-flask/)

Then a JSON object of the response is returned and iterated through to find the horoscope.

Output:
- The user's sign printed using ascii art (Pyfiglet).
- The date range the user chose and the user's astrological symbol are printed.
- The horoscope corresponding to the user's sign and chose date range is printed.
