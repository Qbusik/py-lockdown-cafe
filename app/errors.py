class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        self.message = "Not vaccinated!"

    def __str__(self) -> str:
        return self.message


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        self.message = "Vaccine outdated!"

    def __str__(self) -> str:
        return self.message


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        self.message = "Doesn't have a mask!"

    def __str__(self) -> str:
        return self.message
