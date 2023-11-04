from otree.api import *


doc = """
Mini Ultimatum Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'mini_ultimatum'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    offer_amount = models.CurrencyField(
        doc='Provide an amount between 0 and 200 to send to player 2',
        label='Amount to send to player 2',
        initial=0,
        min=0, max=200)
    offer_punished = models.BooleanField(
        choices=[[True, 'Punish'], [False, 'Not Punish']],
        widget=widgets.RadioSelect,
        label='Do you want to punish player 1 for their offer?',
        doc='Whether player 3 decided to punish or not punish player 1'
    )


class Player(BasePlayer):
    pass

# PAGES


class WaitForPlayer1(WaitPage):
    pass


class WaitForJudge(WaitPage):

    @staticmethod
    def after_all_players_arrive(group: Group):
        # Set the payoff amount for player 1 and player 2
        if group.offer_punished:
            group.get_player_by_id(1).payoff = 0
            group.get_player_by_id(2).payoff = 0
        else:
            group.get_player_by_id(1).payoff -= group.offer_amount
            group.get_player_by_id(2).payoff = group.offer_amount


class OfferStage(Page):
    form_model = 'group'
    form_fields = ['offer_amount']
    timeout_seconds = 30

    @staticmethod
    def is_displayed(player):
        # Endow player 1 with KSH 200
        if player.id_in_group == 1:
            player.payoff = 200
        # Only display the page for Player 1
        return player.id_in_group == 1


class JudgeStage(Page):
    form_model = 'group'
    form_fields = ['offer_punished']
    timeout_seconds = 30

    @staticmethod
    def is_displayed(player):
        # Only display the page for Player 3
        return player.id_in_group == 3

    @staticmethod
    def before_next_page(player: Player, timeout_happened: bool):
        if timeout_happened:
            # Set the default value for the offer_punished field to False
            player.group.offer_punished = False


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        # Print the offer status to Punished or Not Punished
        status: str
        if player.group.offer_punished:
            status = 'Punished'
        else:
            status = 'Did not Punish'
        return dict(
            offer_status=status,
        )


page_sequence = [OfferStage, WaitForPlayer1, JudgeStage, WaitForJudge, Results]
