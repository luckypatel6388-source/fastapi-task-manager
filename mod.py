from sqlalchemy import String,Integer,Column,Enum
from sqlalchemy.orm import Mapped,mapped_column
from db_td import Base
import enum

class Taskstatus(enum.Enum):
    incomplete="Incomplete"
    completed="Done"
    in_progress="In Progress"

class Task(Base):
    __tablename__="Task"
    id:Mapped[int]=mapped_column(Integer,primary_key=True ,index=True, autoincrement=True )
    task:Mapped[str]=mapped_column(String(50))
    #Three option for task status
    status:Mapped[Taskstatus]=mapped_column(Enum(Taskstatus), default=Taskstatus.incomplete, nullable=False)
    description:Mapped[str|None]=mapped_column(String(100), nullable=True)