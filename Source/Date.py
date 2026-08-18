class Date:
    def valid(year: int, month: int, day: int):
        if day <= 0:
            return False
        if month <= 12 and month >= 1:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day <= 31:
                    return True
                else:
                    return False
            if month in [4, 6, 9, 11]:
                if day <= 30:
                    return True
                else:
                    return False
            else:
                if year % 4 == 0 or year % 400 == 0:
                    if day <= 29:
                        return True
                    else:
                        return False
                else:
                    if day <= 28:
                        return True
                    else:
                        return False
        else:
            return False
