from decisions import Decisions


class BasicPrisoner(object):
    def __init__(self):
        self.judgement_history = []
        self.treatment_history = {}

    def accept_judgement(self, judgement):
        self.judgement_history.append(judgement)

    def get_judgement_total(self):
        return sum(self.judgement_history)

    def decide(self, other_prisoner, context=None):
        raise Exception('This is the base class, please use a derived class')


class CooperativePrisoner(BasicPrisoner):
    """ Always cooperates. """
    def decide(self, other_prisoner, context=None):
        return Decisions.COOPERATE


class DefectingPrisoner(BasicPrisoner):
    """ Always defects. Tempted to call them 'DefectivePrisoner'. """
    def decide(self, other_prisoner, context=None):
        return Decisions.DEFECT


class TitForTat(BasicPrisoner):
    """ Reacts like they were treated before. Starts trusting. """
    def decide(self, other_prisoner, context=None):
        personal_history = context.treatment_history[(self, other_prisoner)]
        if not personal_history:
            return Decisions.COOPERATE
        else:
            last_round = personal_history[-1]
            return last_round.opponent_move
