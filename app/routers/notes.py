from fastapi import APIRouter, HTTPException
from app.schemas.note import NoteCreate
from app.schemas.note import NoteResponse


router = APIRouter(prefix="/notes", tags=["Notes"])

notes = []
notesResponse = []


@router.post("/post")
def create_note(note: NoteCreate):
    notes.append(note)

    response = NoteResponse(
        id=len(notes),
        title=note.title,
        content=note.content
    )
    notesResponse.append(response)
    return response


@router.get("/")
def get_notes():
    return notesResponse

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):

    for note in notesResponse:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )


@router.delete("/{note_id}")
def delete_note(note_id: int):

    for note in notes:
        if note.id == note_id:
            notes.remove(note)
            return {"message": "Note deleted"}

    raise HTTPException(
        status_code=404,
        detail="Note not found"
    )