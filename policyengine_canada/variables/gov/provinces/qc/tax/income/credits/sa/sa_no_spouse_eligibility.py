from policyengine_canada.model_api import *


class sa_no_spouse_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec senior assistance tax credits eligible senior did not have a spouse"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        head = person("sa_age_eligibility", period)

        if_spouse = person("is_spouse", period)

        return head & (~if_spouse)
