import cards


def test_update_summary(cards_db):
    """
    Given: a Card object.
    When: we call the method update to change the summary.
    Then: the Card summary sould be updated and the owner should not be.
    """
    cards_db.add_card(cards.Card(summary="first", owner="me"))

    cards_db.update_card(card_id=1, card_mods=cards.Card(summary="second"))

    assert cards_db.get_card(card_id=1) == cards.Card(
        summary="second", owner="me",
    )


def test_update_owner(cards_db):
    """
    Given: a Card object.
    When: we call the method update to change the owner.
    Then: the Card owner sould be updated and the owner should not be.
    """
    cards_db.add_card(cards.Card(summary="first", owner="me"))

    cards_db.update_card(card_id=1, card_mods=cards.Card(owner="you"))

    assert cards_db.get_card(card_id=1) == cards.Card(
        summary="first", owner="you",
    )


def test_update_start(cards_db):
    """
    Given: a Card object.
    When: we call the method start.
    Then: the Card state sould be updated to in prog.
    """
    cards_db.add_card(cards.Card(summary="first", owner="me"))

    cards_db.start(card_id=1)

    assert cards_db.get_card(card_id=1) == cards.Card(
        summary="first", owner="me", state="in prog",
    )


def test_update_finish(cards_db):
    """
    Given: a Card object.
    When: we call the method start.
    Then: the Card state sould be updated to done.
    """
    cards_db.add_card(cards.Card(summary="first", owner="me", state="in prog"))

    cards_db.finish(card_id=1)

    assert cards_db.get_card(card_id=1) == cards.Card(
        summary="first", owner="me", state="done",
    )
