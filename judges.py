from decisions import Decisions


DecisionMatrix = {
    (Decisions.COOPERATE, Decisions.COOPERATE): (1, 1),
    (Decisions.COOPERATE, Decisions.DEFECT): (3, 0),
    (Decisions.DEFECT, Decisions.COOPERATE): (0, 3),
    (Decisions.DEFECT, Decisions.DEFECT): (2, 2)
}


class Judge(object):

    def sentence(self, prisoner1, prisoner2, context=None):
        decision1 = prisoner1.decide(prisoner2, context)
        decision2 = prisoner2.decide(prisoner1, context)

        judgement1, judgement2 = DecisionMatrix[(decision1, decision2)]

        prisoner1.accept_judgement(judgement1)
        prisoner2.accept_judgement(judgement2)

        return judgement1, judgement2


