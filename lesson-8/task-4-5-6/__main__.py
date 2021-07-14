class MyInventoryNumberError(Exception):
    txt = 'inventory_number must be string'


class MyMonochromeError(Exception):
    txt = 'monochrome must be boolean'


class OfficeEquipment:
    inventory_number = None

    def __init__(self, inventory_number):
        if not(type(inventory_number) is str):
            raise MyInventoryNumberError()

        self.inventory_number = inventory_number


class Printer(OfficeEquipment):
    monochrome = False

    def __init__(self, inventory_number, monochrome):
        if not(type(monochrome) is bool):
            raise MyMonochromeError()

        super().__init__(inventory_number)
        self.monochrome = monochrome


class Scanner(OfficeEquipment):
    pages_per_second = 20

    def __init__(self, inventory_number, pages_per_second):
        super().__init__(inventory_number)
        self.pages_per_second = pages_per_second


class Xerox(OfficeEquipment):
    tonner_level = None

    def __init__(self, inventory_number, tonner_level):
        super().__init__(inventory_number)
        self.tonner_level = tonner_level


class OfficeEquipmentStore:
    tech_list = []
    passed = {}

    def receive(self, tech):
        self.tech_list.append(tech)

    def pass_to_department(self, tech, department):
        self.tech_list = list(filter(
            lambda t: t.inventory_number != tech.inventory_number, self.tech_list))

        if department in self.passed:
            self.passed[department].append(tech)
        else:
            self.passed[department] = tech
