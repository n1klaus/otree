from otree.api import *


doc = """
Mini Ultimatum Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'mini_ultimatum'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    offer_amount = models.CurrencyField(
        doc='Provide an amount between 0 and 200 to send to player 2',
        label='Amount to send to player 2',
        min=0, max=200)
    offer_accepted = models.BooleanField(
        choices=[[True, 'Punish'], [False, 'Not Punish']],
        widget=widgets.RadioSelect,
        label='Do you want to punish player 1 for their offer?',
        doc='Whether player 3 accepted or rejected the offer from player 1'
    )


class Player(BasePlayer):
    pass

# PAGES


class WaitForPlayer1(WaitPage):
    pass


class WaitForJudge(WaitPage):

    @staticmethod
    def after_all_players_arrive(group: Group):
        # Set the payout amount for player 1 and player 2
        if not group.offer_accepted:
            group.get_player_by_id(1).payoff = 0
            group.get_player_by_id(2).payoff = 0
        else:
            group.get_player_by_id(1).payoff = 200 - group.offer_amount
            group.get_player_by_id(2).payoff = group.offer_amount
        print("{0}, {1}".format(group.offer_accepted, group.offer_amount))
        print(
            "{0}, {1}".format(
                group.get_player_by_id(1).payoff,
                group.get_player_by_id(2).payoff))


class OfferStage(Page):
    form_model = 'group'
    form_fields = ['offer_amount']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1


class JudgeStage(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']
    timeout_seconds = 30

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 3

    @staticmethod
    def before_next_page(player: Player, timeout_happened: bool):
        if timeout_happened:
            # Set the default value for the offer_accepted field to False
            player.group.offer_accepted = False


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        # Print the offer status to Accepted or Rejected
        status: str = 'Accepted' if player.group.offer_accepted else 'Rejected'
        return dict(
            offer_status=status,
        )


page_sequence = [OfferStage, WaitForPlayer1, JudgeStage, WaitForJudge, Results]
