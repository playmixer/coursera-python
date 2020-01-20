from abc import ABC, abstractmethod
# from heroes import Hero


class AbstractEffect(Hero, ABC):        
    def __init__(self, base):
        self.base = base
            
    def get_positive_effects(self):
        return self.positive_effects.copy()
   
    def get_negative_effects(self):
        return self.negative_effects.copy()
       
    @abstractmethod
    def get_stats():
        pass


class AbstractPositive(AbstractEffect):        
    @abstractmethod
    def get_positive_effects(self):
        pass
    
    
class AbstractNegative(AbstractEffect):
    @abstractmethod
    def get_negative_effects(self):
        pass


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        return self.base.get_positive_effects()  + ["Berserk"]
    
    def get_negative_effects(self):
        return self.base.get_negative_effects()
        
    def get_stats(self):
        change = {
            "HP": 50,  # health points
            "Strength": 7,  # сила
            "Perception": -3,  # восприятие
            "Endurance": 7,  # выносливость
            "Charisma": -3,  # харизма
            "Intelligence": -3,  # интеллект
            "Agility": 7,  # ловкость 
            "Luck": 7  # удача
        }
        stats = self.base.get_stats()
        for key, value in change.items():
            stats[key] += value
            
        return stats
        

class Blessing(AbstractPositive):    
    def get_positive_effects(self):
        return self.base.get_positive_effects()  + ["Blessing"]
    
    def get_negative_effects(self):
        return self.base.get_negative_effects()
    
    def get_stats(self):
        change = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость 
            "Luck": 2  # удача
        }
        stats = self.base.get_stats()
        for key, value in change.items():
            stats[key] += value
            
        return stats
        

class Curse(AbstractNegative):    
    def get_positive_effects(self):
        return self.base.get_positive_effects()
        
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]
    
    def get_stats(self):
        change = {
            "Strength": -2,  # сила
            "Perception": -2,  # восприятие
            "Endurance": -2,  # выносливость
            "Charisma": -2,  # харизма
            "Intelligence": -2,  # интеллект
            "Agility": -2,  # ловкость 
            "Luck": -2  # удача
        }
        stats = self.base.get_stats()
        for key, value in change.items():
            stats[key] += value
            
        return stats
        

class EvilEye(AbstractNegative):    
    def get_positive_effects(self):
        return self.base.get_positive_effects()
        
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]
    
    def get_stats(self):
        change = {
            "Luck": -10  # удача
        }
        stats = self.base.get_stats()
        for key, value in change.items():
            stats[key] += value
            
        return stats
        

class Weakness(AbstractNegative):   
    def get_positive_effects(self):
        return self.base.get_positive_effects()
        
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]
    
    def get_stats(self):
        change = {
            "Strength": -4,  # сила
            "Endurance": -4,  # выносливость
            "Agility": -4,  # ловкость 
        }
        stats = self.base.get_stats()
        for key, value in change.items():
            stats[key] += value
            
        return stats

if __name__ == "__main__":
    hero = Hero()
    print(hero.stats)
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    bers = Berserk(hero)
    print("bers", "="*50)
    print(bers.get_stats())
    print(bers.get_positive_effects())
    print(bers.get_negative_effects())
    print("bers2", "="*50)
    bers2 = Berserk(bers)
    print(bers2.get_stats())
    print(bers2.get_positive_effects())
    print(bers2.get_negative_effects())
    print("curs", "="*50)
    bles = Blessing(bers2)
    print(bles.get_stats())
    print(bles.get_positive_effects())
    print(bles.get_negative_effects())
    print("bles", "="*50)
    bles2 = Blessing(bles)
    print(bles2.get_stats())
    print(bles2.get_positive_effects())
    print(bles2.get_negative_effects())
    print("bles2", "="*50)
    bles3 = Blessing(bles2)
    print(bles3.get_stats())
    print(bles3.get_positive_effects())
    print(bles3.get_negative_effects())
    print("bles3", "="*50)
    
    curs = Curse(bers2)
    print(curs.get_stats())
    print(curs.get_positive_effects())
    print(curs.get_negative_effects())
    curs.base = curs.base.base
    print(curs.get_stats())
    print(curs.get_positive_effects())
    print(curs.get_negative_effects())
    