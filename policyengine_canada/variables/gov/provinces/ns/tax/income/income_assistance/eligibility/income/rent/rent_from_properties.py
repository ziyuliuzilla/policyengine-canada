from policyengine_canada.model_api import *


class rent_from_properties(Variable):
    value_type = float
    entity = Person
    label = "rent income from properties"
    unit = CAD
    documentation = "rent income received from properties"
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/just/regulations/regs/esiaregs.htm#TOC2_4"
    )
