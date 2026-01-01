from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.auth import get_current_user
from app.db.database import get_db
from app.db.models import Note
from app.schemas.schemas import NoteCreate, NoteOut
from app.core.crypto import encrypt_text, decrypt_text

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post(
    "/",
    response_model=NoteOut,
    status_code=status.HTTP_201_CREATED,
)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    encrypted_content = encrypt_text(note.content)

    new_note = Note(
        title=note.title,
        content=encrypted_content,
        owner_id=user.id,
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    # Расшифровываем перед отдачей клиенту
    new_note.content = decrypt_text(new_note.content)
    return new_note


@router.get("/", response_model=list[NoteOut])
def get_notes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    notes = (
        db.query(Note)
        .filter(Note.owner_id == user.id)
        .all()
    )

    for note in notes:
        note.content = decrypt_text(note.content)

    return notes


@router.delete(
    "/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    note = db.get(Note, note_id)

    if not note or note.owner_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    db.delete(note)
    db.commit()
