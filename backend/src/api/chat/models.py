from datetime import datetime, timezone

from sqlmodel import SQLModel, Field, DateTime, func

def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)

class ChatMessagePayload(SQLModel):
    # pydantic model for validation, serialization, deserialization
    # validation
    message: str

class ChatMessage(SQLModel, table=True):
    # database table
    # saving, retrieving, updating, deleting from database
    id: int | None = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now, # this will ensure that the created_at field is always set to the current UTC time when a new ChatMessage is created, regardless of the timezone of the server or client. This is important for consistency and to avoid issues with timezone differences when storing and retrieving data from the database.
        sa_type=DateTime(timezone=True), # sqlalchemy && check out analytics api course for timescaledb 
        primary_key=False,
        nullable=False
    )

class ChatMessageListItem(SQLModel):
    # this is a pydantic model for the response of the chat_list_messages endpoint, it is used to serialize the data from the database into a format that can be returned to the client. It is not a database table, so it does not have the table=True parameter.
    id: int | None = Field(default=None)
    message: str
    created_at: datetime = Field(default=None)
