import re


class astrro_sign:
    #  class declaration

    print (re.match("[A-Z]+", "WELCOME"))
#   regular expression

    def __init__(self):
        self.day = int(input("Enter Day = "))
        self.month = int(input("Enter the Month = "))


class Year(astrro_sign):
    def year(self):
        if self.month == 1:
            astro_sign = 'CAPRICORN' if (self.day < 20) else 'AQUARIUS'
        elif self.month == 2:
            astro_sign = 'AQUARIUS' if (self.day < 19) else 'PISCES'
        elif self.month == 3:
            astro_sign = 'PISCES' if (self.day < 21) else 'ARIES'
        elif self.month == 4:
            astro_sign = 'ARIES' if (day < 20) else 'TAURUS'
        elif self.month == 5:
            astro_sign = 'TAURUS' if (self.day < 21) else 'GEMINI'
        elif self.month == 6:
            astro_sign = 'GEMINI' if (self.day < 21) else 'CANCER'
        elif self.month == 7:
            astro_sign = 'CANCER' if (self.day < 23) else 'LEO'
        elif self.month == 8:
            astro_sign = 'LEO' if (self.day < 23) else 'VIGRO'
        elif self.month == 9:
            astro_sign = 'VIGRO' if (self.day < 23) else 'LIBRA'
        elif self.month == 10:
            astro_sign = 'LIBRA' if (self.day < 23) else 'SCORPIO'
        elif self.month == 11:
            astro_sign = 'SCORPIO' if (self.day < 22) else 'SAGITTARIUS'
        elif self.month == 12:
            astro_sign = 'SAGITTARIUS' if (self.day < 22) else 'CAPRICON'
        print("As per the western calendar  your zodiac sign is", astro_sign)
if __name__ == '__main__':
    def main():
        a = Year()
        a.year()
    main()
