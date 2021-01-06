from uuid import uuid4

class Identity(object):
    def __init__(self, id_pool, id=uuid4()): 
        self.id = id
        self.id_pool = id_pool

    def get_id(self):
        return self.id