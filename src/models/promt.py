from datetime import datetime

from sqlalchemy import (Column, Date, Integer, Text)

from src.service.database import Base


class Prompt(Base):
    __tablename__ = 'prompts'

    promt_id = Column(Integer, primary_key=True)
    content = Column(Text, unique=True, nullable=False)
    created_on = Column(Date, default=datetime.now)
    update_on = Column(Date, default=datetime.now, onupdate=datetime.now)
