# Create constructor
class Ale:
    def __init__(self, name, abv):
        self.name = name
        self.abv = abv
    def alcohol_content(self, volume_in_oz):
        return self.abv * volume_in_oz
    def description(self):
        return f"{self.name}: {self.abv*100:.1f}% ABV"
# Rewriting individual subclasses using constructor
class PaleAle(Ale):
    def __init__(self):
        super().__init__("PaleAle", 0.055)
class IPA(Ale):
    def __init__(self):
        super().__init__("IPA", 0.065)
class Stout(Ale):
    def __init__(self):
        super().__init__("Stout", 0.07)
class Porter(Ale):
    def __init__(self):
        super().__init__("Porter", 0.06)
# Testing
if __name__=="__main__":
    ales = [PaleAle(),IPA(),Stout(),Porter()]
    # Iterate through each instance of the subclass in list
    for ale in ales:
        # Calls description from each object
        print(ale.description())
        print (f"Alcohol content in 16 oz: {ale.alcohol_content(16):.2f} oz.")


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 