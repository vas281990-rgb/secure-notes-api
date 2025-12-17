from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .auth import get_current_user, get_db
from .models import Note
from .schemas import NoteCreate, NoteOut

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("/", response_model=NoteOut)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/", response_model=list[NoteOut])
def get_notes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return db.query(Note).filter(Note.owner_id == user.id).all()
