import random
from os import listdir
from os.path import isfile, join
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class InformedConsent(Page):
    form_model = "player"
    form_fields = ["consent"]

    def is_displayed(self):
        return self.round_number == 1


class Instructions(Page):
    form_model = "player"

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == 1
        else:
            return False


class TrainingSheetProtector(Page):
    form_model = "player"
    form_fields = ["training", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == 1
        else:
            return False


class PrimingBucket(Page):
    timeout_seconds = 3
    form_model = "player"
    form_fields = ["condition"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["Bucket"]
        else:
            return False

    def vars_for_template(self):
        pic_path = ""
        if Constants.cond_list[self.round_number-1] == "close":
            pictures = [f for f in listdir("close semdis priming bucket") if isfile(join("close semdis priming bucket", f))]
            pic_path = pictures[random.randrange(0,len(pictures))]
        elif Constants.cond_list[self.round_number-1] == "far":
            pictures = [f for f in listdir("far semdis priming bucket") if isfile(join("far semdis priming bucket", f))]
            pic_path = pictures[random.randrange(0,len(pictures))]

        return dict(image_path=pic_path.format(self.round_number + 1))

    def before_next_page(self):
        self.player.condition = Constants.cond_list[self.round_number-1]


class Bucket(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["bucket", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["Bucket"]
        else:
            return False


class PrimingShoelace(Page):
    timeout_seconds = 3
    form_model = "player"
    form_fields = ["condition"]
    # shoelace_dict = {"far": ["img1", "img2", "img3"], "close": ["img4", "img5", "img6"], "control": "blank"}

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["Shoelace"]
        else:
            return False

    def vars_for_template(self):
        pic_path = ""
        if Constants.cond_list[self.round_number-1] == "close":
            pictures = [f for f in listdir("close semdis priming shoelace") if isfile(join("close semdis priming shoelace", f))]
            pic_path = pictures[random.randrange(0, len(pictures))]
        elif Constants.cond_list[self.round_number-1] == "far":
            pictures= [f for f in listdir("fer semdis priming shoelace") if isfile(join("fer semdis priming shoelace", f))]
            pic_path =pictures[random.randrange(0,len(pictures))]
        condition = dict(image_path=pic_path.format(self.round_number + 1))
        return condition

    def before_next_page(self):
        self.player.condition = Constants.cond_list[self.round_number-1]


class Shoelace(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["shoelace", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["Shoelace"]
        else:
            return False


class PrimingWineCork(Page):
    timeout_seconds = 3
    form_model = "player"
    form_fields = ["condition"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["WineCork"]
        else:
            return False

    def vars_for_template(self):
        pic_path = ""
        if Constants.cond_list[self.round_number-1] == "close":
            pictures = [f for f in listdir("close winecork") if isfile(join("close winecork", f))]
            pic_path = pictures[random.randrange(0, len(pictures))]
        elif Constants.cond_list[self.round_number-1] == "far":
            pictures= [f for f in listdir("far winecork") if isfile(join("far winecork", f))]
            pic_path =pictures[random.randrange(0,len(pictures))]
        condition = dict(image_path=pic_path.format(self.round_number + 1))
        return condition

    def before_next_page(self):
        self.player.condition = Constants.cond_list[self.round_number-1]


class WineCork(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["winecork", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["WineCork"]
        else:
            return False


class PrimingOfficeClip(Page):
    timeout_seconds = 3
    form_model = "player"
    form_fields = ["condition"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["OfficeClip"]
        else:
            return False

    def vars_for_template(self):
        pic_path = ""
        if Constants.cond_list[self.round_number-1] == "close":
            print("close")
            pictures = [f for f in listdir("close paper clip") if isfile(join("close paper clip", f))]
            pic_path = pictures[random.randrange(0, len(pictures))]
        elif Constants.cond_list[self.round_number-1] == "far":
            pictures = [f for f in listdir("far_paperclip") if isfile(join("far_paperclip", f))]
            pic_path = pictures[random.randrange(0, len(pictures))]
        condition = dict(image_path=pic_path.format(self.round_number + 1))
        return condition

    def before_next_page(self):
        self.player.condition = Constants.cond_list[self.round_number-1]


class OfficeClip(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["paperclip", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["OfficeClip"]
        else:
            return False


class PrimingBrick(Page):
    timeout_seconds = 3
    form_model = "player"
    form_fields = ["condition"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["SheetProtector"]
        else:
            return False

    def vars_for_template(self):
        pic_path = ""
        if Constants.cond_list[self.round_number-1] == "close":
            pictures = [f for f in listdir("close semdis priming") if isfile(join("close semdis priming", f))]
            pic_path = pictures[random.randrange(0, len(pictures))]
        elif Constants.cond_list[self.round_number-1] == "far":
            pictures = [f for f in listdir("far semdis priming") if isfile(join("far semdis priming", f))]
            pic_path = pictures[random.randrange(0,len(pictures))]
        condition = dict(image_path=pic_path.format(self.round_number + 1))
        return condition

    def before_next_page(self):
        self.player.condition = Constants.cond_list[self.round_number-1]


class Brick(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["brick", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["SheetProtector"]
        else:
            return False


class PrimingHanger(Page):
    timeout_seconds = 3
    form_model = "player"

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["hanger"]
        else:
            return False

    def vars_for_template(self):

        pic_path = ""
        if Constants.cond_list[self.round_number-1] == "close":
            pictures = [f for f in listdir("close hanger") if isfile(join("close hanger", f))]
            pic_path = pictures[random.randrange(0, len(pictures))]
        elif Constants.cond_list[self.round_number-1] == "far":
            pictures = [f for f in listdir("far hanger") if isfile(join("far hanger", f))]
            pic_path = pictures[random.randrange(0,len(pictures))]
        condition = dict(image_path=pic_path.format(self.round_number + 1))
        return condition

    def before_next_page(self):
        self.player.condition = Constants.cond_list[self.round_number-1]


class Hanger(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["hanger", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == self.participant.vars['task_rounds']["hanger"]
        else:
            return False



class AttentionCheck(Page):
    timeout_seconds = 120
    form_model = "player"
    form_fields = ["attentioncheck", "use2", "use3", "use4", "use5", "use6", "use7", "use8", "use9", "use10", "use11",
                   "use12", "use13", "use14", "use15"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == Constants.num_rounds
        else:
            return False


class Demographics(Page):
    form_model = "player"
    form_fields = ["age", "gender", "yoe", "psychometric", "youth_mov"]

    def is_displayed(self):
        if self.player.in_round(1).consent == "I agree to participate in the experiment":
            return self.round_number == Constants.num_rounds
        else:
            return False


page_sequence = [InformedConsent, Instructions, TrainingSheetProtector, PrimingBucket, Bucket, PrimingShoelace,
                 Shoelace, PrimingOfficeClip, OfficeClip, PrimingWineCork, WineCork,  PrimingBrick, Brick,
                 PrimingHanger, Hanger, AttentionCheck, Demographics]


