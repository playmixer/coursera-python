
class AbstractLevel:
    @classmethod
    def get_map(Class):
        return Class.Map()
    
    @classmethod
    def get_objects(Class):
        return Class.Objects()


class EasyLevel(AbstractLevel):
    class Objects:
        def __init__(self):
            self.objects = EasyObjects()
        
        def get_objects(self):
            return self.objects
        
    class Map:
        def __init__(self):
            self.map_ = EasyMap()
        
        def get_map(self):
            return self.map_


class MediumLevel(AbstractLevel):
    class Objects:
        def __init__(self):
            self.objects = MediumObjects()
        
        def get_objects(self):
            return self.objects
        
    class Map:
        def __init__(self):
            self.map_ = MediumMap()
        
        def get_map(self):
            return self.map_


class HardLevel(AbstractLevel):
    class Objects:
        def __init__(self):
            self.objects = HardObjects()
        
        def get_objects(self):
            return self.objects
        
    class Map:
        def __init__(self):
            self.map_ = HardObjects()
        
        def get_map(self):
            return self.map_

