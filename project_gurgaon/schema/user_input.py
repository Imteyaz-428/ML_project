from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated





# validate incoming data using pydantics
class UserInput(BaseModel) :
    Status: Literal["Ready to Move", "Under Construction"]
    Area : Annotated[int, Field(..., description="Area of the flate")]
    Rate_per_sqft: Annotated[int,Field(..., gt=0,description="Rate of the Area per sqft")]
    Property_Type : Annotated[str, Field(..., description="properperty type")]
    Locality: Annotated[str, Field(..., description=" Locality")]
    RERA_Approval: Annotated[str, Field(..., description="RERA approval or not")]
    BHK_Count: Annotated[int, Field(..., description="total bhk")]
    Flat_type: Literal["Apartment", "Villa", "Plot"]
    model_config = {

        "populate_by_name": True

    }
  

