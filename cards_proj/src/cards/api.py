"""API for the cards project."""
from dataclasses import asdict, dataclass, field
from typing import Optional

from .db import DB

__all__ = [
    "Card",
    "CardsDB",
    "CardsException",
    "MissingSummary",
    "InvalidCardId",
]


@dataclass
class Card:
    """Original documentation was not provided."""

    summary: Optional[str] = None
    owner: Optional[str] = None
    state: str = "todo"
    id: Optional[int] = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        """Original documentation was not provided."""
        return Card(**d)

    def to_dict(self):
        """Original documentation was not provided."""
        return asdict(self)


class CardsException(Exception):
    """Original documentation was not provided."""

    pass


class MissingSummary(CardsException):
    """Original documentation was not provided."""

    pass


class InvalidCardId(CardsException):
    """Original documentation was not provided."""

    pass


class CardsDB:
    """Original documentation was not provided."""

    def __init__(self, db_path):
        """Original documentation was not provided."""
        self._db_path = db_path
        self._db = DB(db_path, ".cards_db")

    def add_card(self, card: Card) -> int:
        """Add a card, return the id of card."""
        if not card.summary:
            raise MissingSummary
        if card.owner is None:
            card.owner = ""
        id = self._db.create(card.to_dict())
        self._db.update(id, {"id": id})
        return id

    def get_card(self, card_id: int) -> Card:
        """Return a card with a matching id."""
        db_item = self._db.read(card_id)
        if db_item is not None:
            return Card.from_dict(db_item)
        else:
            raise InvalidCardId(card_id)

    def list_cards(self, owner=None, state=None):
        """Return a list of cards."""
        all = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Card.from_dict(t)
                for t in all
                if (t["owner"] == owner and t["state"] == state)
            ]
        elif owner is not None:
            return [Card.from_dict(t) for t in all if t["owner"] == owner]
        elif state is not None:
            return [Card.from_dict(t) for t in all if t["state"] == state]
        else:
            return [Card.from_dict(t) for t in all]

    def count(self) -> int:
        """Return the number of cards in db."""
        return self._db.count()

    def update_card(self, card_id: int, card_mods: Card) -> None:
        """Update a card with modifications."""
        try:
            self._db.update(card_id, card_mods.to_dict())
        except KeyError as exc:
            raise InvalidCardId(card_id) from exc

    def start(self, card_id: int):
        """Set a card state to 'in prog'."""
        self.update_card(card_id, Card(state="in prog"))

    def finish(self, card_id: int):
        """Set a card state to 'done'."""
        self.update_card(card_id, Card(state="done"))

    def delete_card(self, card_id: int) -> None:
        """Remove a card from db with given card_id."""
        try:
            self._db.delete(card_id)
        except KeyError as exc:
            raise InvalidCardId(card_id) from exc

    def delete_all(self) -> None:
        """Remove all cards from db."""
        self._db.delete_all()

    def close(self):
        """Original documentation was not provided."""
        self._db.close()

    def path(self):
        """Original documentation was not provided."""
        return self._db_path
