class Insured:
    """
    Třída pro pojištěnce
    """

    _list_of_ensured = []

    def __init__(self, name, surname, phone, age):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._age = age
        Insured._list_of_ensured.append((self._name, self._surname, self._phone, self._age))
