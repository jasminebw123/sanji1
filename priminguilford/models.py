from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
import itertools

from otree.models import player

author = 'The A Team'

doc = """
A Guilford Task (Alternate Uses Task) + priming - An operation of one's creativity
 by semantic priming of a distant/close to the object the player will be 
 asked to come up with uses to (A within subjects experiment).
"""


class Constants(BaseConstants):
    name_in_url = 'a_team_experiment'
    players_per_group = None
    cond_list = ["close", "close", "far", "far", "control", "control"]
    random.shuffle(cond_list)
    tasks = ["OfficeClip", "SheetProtector", "hanger", "Shoelace", "WineCork", "Bucket"]
    num_rounds = len(tasks)


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # condition:
    condition = models.StringField()
    # Demographics:
    gender = models.StringField(label="Gender", choices=["Male", "Female", "Other"], blank=False)
    yoe = models.IntegerField(label="Years of Education", min=1, max=40, blank=False)
    age = models.IntegerField(label="Age", min=20, max=90, blank=False)
    youth_mov = models.IntegerField(label="How many years did you attend a youth movement?",
                                    min=0, max=30, blank=False)
    psychometric = models.IntegerField(label="Your psychometric grade (If you don't have one, "
                                             "you may skip this question)", min=200, max=800, blank=True)
    # variable names to distinguish the objects from each other in the data:
    training = models.StringField(label="use1", blank=False)
    bucket = models.StringField(label="use1", blank=False)
    paperclip = models.StringField(label="use1", blank=False)
    brick = models.StringField(label="use1", blank=False)
    hanger = models.StringField(label="use1", blank=False)
    shoelace = models.StringField(label="use1", blank=False)
    winecork = models.StringField(label="use1", blank=False)
    # other variables, for other uses:
    use2 = models.StringField(label="use2", blank=True)
    use3 = models.StringField(label="use3", blank=True)
    use4 = models.StringField(label="use4", blank=True)
    use5 = models.StringField(label="use5", blank=True)
    use6 = models.StringField(label="use6", blank=True)
    use7 = models.StringField(label="use7", blank=True)
    use8 = models.StringField(label="use8", blank=True)
    use9 = models.StringField(label="use9", blank=True)
    use10 = models.StringField(label="use10", blank=True)
    use11 = models.StringField(label="use11", blank=True)
    use12 = models.StringField(label="use12", blank=True)
    use13 = models.StringField(label="use13", blank=True)
    use14 = models.StringField(label="use14", blank=True)
    use15 = models.StringField(label="use15", blank=True)
    # Attention check:
    attentioncheck = models.StringField(label="use1", blank=False)
    # consent:
    consent = models.StringField(label="Informed consent", choices=["I do not agree to participate in the experiment",
                                                                    "I agree to participate in the experiment"], blank=False)
