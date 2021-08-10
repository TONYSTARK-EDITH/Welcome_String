class CharacterExpectedGotStringException(Exception):
    def __init__(self, val) -> None:
        self.val = val

    def __str__(self) -> str:
        return self.val


class EmptyCharacterFoundException(Exception):
    def __init__(self, val) -> None:
        self.val = val

    def __str__(self) -> str:
        return self.val
