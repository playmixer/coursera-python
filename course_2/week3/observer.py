from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscriber = set()
        
    def subscribe(self, subscriber):
        self.__subscriber.add(subscriber)
        
    def unsubscribe(self, subscriber):
        self.__subscriber.remove(subscriber)
        
    def notify(self, message):
        for subscriber in self.__subscriber:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()
        
    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()
        
    def update(self, message):
        if not message in self.achievements:
            self.achievements.append(message)
