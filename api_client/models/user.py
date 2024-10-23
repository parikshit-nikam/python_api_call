from pydantic import BaseModel, RootModel
from typing import Optional, List, Dict, Any

class MoreData(RootModel):
    root: Dict[str, Any]  # This allows for any key-value pairs

class User(BaseModel):
    id: str
    name: str
    data: Optional[MoreData] = None  # Use MoreData to allow flexibility
