

class DivBy12Exception(Exception):

    def __init__(self) -> None:
        super().__init__("Division par 12 !")
