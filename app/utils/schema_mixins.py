from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict, RootModel


class BaseInDBMixin(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID

    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime]


class ListModelsMixin(RootModel, BaseModel):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
