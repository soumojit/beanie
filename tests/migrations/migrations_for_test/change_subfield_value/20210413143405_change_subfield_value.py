from pydantic.main import BaseModel

from beanie import Document, iterative_migration


class Tag(BaseModel):
    color: str
    name: str


class Note(Document):
    title: str
    tag: Tag

    class Collection:
        name = "notes"


class Forward:
    @iterative_migration()
    async def change_color(self, input_document: Note, output_document: Note):
        output_document.tag.color = "blue"


class Backward:
    @iterative_migration()
    async def change_title(self, input_document: Note, output_document: Note):
        output_document.tag.color = "red"
