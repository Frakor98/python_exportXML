class Card:
    def __init__(
            self
            , adrenaline_cost
            , description
            , name):
        self.adrenaline_cost = adrenaline_cost
        self.description = description
        self.name = name
    def __repr__(self) -> str:
        f"{self.adrenaline_cost} {self.description} {self.name}"