

class Todo:
    
    def __init__(self,*,id=0,title,completed) -> None:
        self._id = id
        self._title = title
        self._completed = completed

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        self._id = id
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        self._title = title
    
    @property
    def completed(self):
        return self._completed
    
    @completed.setter
    def completed(self,completed):
        self._completed = completed
