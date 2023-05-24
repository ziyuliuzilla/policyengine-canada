from policyengine_canada.model_api import *


class nu_age_amount_credit(Variable):
    value_type = float
    entity = person
    label = "Nunvaut age amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        income = person("total_individual_pre_tax_income", period)
        eligible = person("nu_age_amount_credit_eligible_person", period)
        p = parameters(period).gov.provinces.nu.tax.income.credits.age_amount
        phase_out_amount = p.phase_out_rate.calc(income)
        max_amount = p.amount
        return eligible * min_(max_amount - phase_out_amount, 0)