from otree.api import *


doc = """
Exit Survey
"""


class C(BaseConstants):
    NAME_IN_URL = 'exit_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    capital_city = models.StringField(
        choices=['Kisumu', 'Nairobi', 'Mombasa'],
        label='What is the capital City of Kenya?',
        doc="""Capital City of Kenya"""
    )
    sum_result = models.IntegerField(
        label='What is 14 + 15 ?',
        doc="Result of adding 14 and 15"
    )
    population = models.IntegerField(
        label='What is the population of Kenya?',
        min=1,
        doc="The Population of Kenya",
    )


# PAGES
class GetCapitalCity(Page):
    form_model = 'player'
    form_fields = ['capital_city']


class SumEquation(Page):
    form_model = 'player'
    form_fields = ['sum_result']

    @staticmethod
    def error_message(player: Player, values: dict):
        # Validate the correct answer is provided
        print('value is', values['sum_result'])
        if values['sum_result'] != 29:
            return 'Wrong answer. Please try again'


class GetPopulation(Page):
    form_model = 'player'
    form_fields = ['population']


class SurveyResults(Page):
    pass


page_sequence = [GetCapitalCity, SumEquation, GetPopulation, SurveyResults]
