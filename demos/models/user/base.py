# -*- coding:utf-8 -*-

from models.base import *


class Model(BaseModel):

    def __init__(self):
        super(Model, self).__init__(db_name='user')


class MotorModel(MotorBaseModel):
    def __init__(self):
        super(MotorModel, self).__init__(db_name='tag')
