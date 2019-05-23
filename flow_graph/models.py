from sqlalchemy import Column, Integer, String, DateTime
from flow_graph.database import Base
import datetime

class FlowForm(Base):
    __tablename__ = 'flow_form'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    activity = Column(String(255), nullable=False)
    category = Column(String(40), nullable=False)
    difficulty = Column(Integer, nullable=False)
    skill = Column(Integer, nullable=False)
    skill_feel = Column(Integer, nullable=False)
    immersed = Column(Integer, nullable=False)
    objective = Column(Integer, nullable=False)
    control = Column(Integer, nullable=False)
    other = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
    fail = Column(Integer, nullable=False)
    learn = Column(Integer, nullable=False)
    want = Column(Integer, nullable=False)
    happiness = Column(Integer, nullable=False)
    social = Column(String(40), nullable=False)

    def __init__(self, activity=None, category=None, difficulty=None, skill=None, skill_feel=None, immersed=None, objective=None, control=None, other=None, time=None, fail=None, learn=None, want=None, happiness=None, social=None):
        self.activity = activity
        self.category = category
        self.difficulty = difficulty
        self.skill = skill
        self.skill_feel = skill_feel
        self.immersed = immersed
        self.objective = objective
        self.control = control
        self.other = other
        self.time = time
        self.fail = fail
        self.learn = learn
        self.want = want
        self.happiness = happiness
        self.social = social

    def get_theoretical_flow(self):
        """
        Calculation of theoretical flow due of difficulty and skill level
        @TODO Calculation with average of difficulty and skill level
        :param difficulty:
        :param skill_level:
        :return:
        """
        if self.difficulty > 3:
            if  self.skill > 3:
                t_flow =  "flow"
            if  self.skill < 3:
                t_flow = "angoisse"
            if  self.skill == 3:
                t_flow = "stimulé"
        if  self.difficulty == 3:
            if  self.skill > 3:
                t_flow = "contrôle"
            if  self.skill < 3:
                t_flow = "inquetude"
            if  self.skill == 3:
                t_flow = "neutre"
        if  self.difficulty < 3:
            if  self.skill > 3:
                t_flow = "relaxation"
            if  self.skill < 3:
                t_flow = "apathie"
            if  self.skill == 3:
                t_flow = "ennui"

        return t_flow

    def get_flow_indicator(self):
        return round(((self.skill_feel + self.immersed + self.objective + self.control + self.other + self.time + self.fail + self.learn) / 8),1)

    def get_want(self):
        return 'Oui' if self.want == 1 else 'Non'