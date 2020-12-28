"""

Susciuc Anastasia

"""


from UI.UI_console import UI
from operations.algorithms import Operations, Conversions
from service.service import Service

if __name__ == "__main__":
    operation = Operations()
    conversions = Conversions()
    service = Service(operation, conversions)

    ui = UI(service)
    ui.run()
