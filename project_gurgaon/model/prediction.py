from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func

from database.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    locality = Column(String(255))
    bhk = Column(Integer)
    area = Column(Float)

    predicted_price = Column(Float)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )