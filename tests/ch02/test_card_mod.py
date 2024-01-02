from dataclasses import asdict, dataclass, field
from typing import Optional


@dataclass
class Card:
    """Base class for the Cards."""

    summary: Optional[str] = "NaN"
    owner: Optional[str] = "NaN"
    state: str = "todo"
    id: Optional[int] = field(default=None, compare=True)

    @classmethod
    def from_dict(cls, d):
        """This method create a card from a dict."""
        return Card(**d)

    def to_dict(self):
        """This method export a card to a dict."""
        return asdict(self)


class BookTests:
    """
    These tests was provided by the book author.
    The class Card was changed to solve the exercices.
    """

    def test_field_access(self):
        c = Card("something", "brian", "todo", 123)
        assert c.summary == "something"
        assert c.owner == "brian"
        assert c.state == "todo"
        assert c.id == 123

    def test_defaults(self):
        c = Card()
        assert c.summary == "NaN"
        assert c.owner == "NaN"
        assert c.state == "todo"
        assert c.id is None

    def test_equality(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("something", "brian", "todo", 123)
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("something", "brian", "todo", 4567)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("completely different", "okken", "done", 123)
        assert c1 != c2

    def test_from_dict(self):
        c1 = Card("something", "brian", "todo", 123)
        c2_dict = {
            "summary": "something",
            "owner": "brian",
            "state": "todo",
            "id": 123,
        }
        c2 = Card.from_dict(c2_dict)
        assert c1 == c2

    def test_to_dict(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = c1.to_dict()
        c2_expected = {
            "summary": "something",
            "owner": "brian",
            "state": "todo",
            "id": 123,
        }
        assert c2 == c2_expected


class OwnTest:
    """
    I author these tests to fix my knowledge.
    However, due my lack of knowledge, I will just write test structures.
    When I fill more confortable, I will return and complete the code.
    """

    def test_update_info_card(self):
        """
        Given: a Card object.
        When: we call the method update.
        Then: the Card should be updated.

        There are two scenarios that we may cover:
        - update one field per time and assert that other fields
        remain the same; and,
        - update all the fields and assert that all fields have changed.
        """
        assert True

    def test_start_card(self):
        """
        Given: a Card object.
        When: we call the method start.
        Then: the Card status should be updated to in prog.
        """
        assert True

    def test_finish_card(self):
        """
        Given: a Card object.
        When: we call the method finish.
        Then: the Card status should be updated to done.
        """
        assert True
