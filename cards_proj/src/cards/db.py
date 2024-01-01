"""DB for the cards project."""
import tinydb


class DB:
    """Original documentation was not provided."""

    def __init__(self, db_path, db_file_prefix):
        """Original documentation was not provided."""
        self._db = tinydb.TinyDB(
            db_path / f"{db_file_prefix}.json",
            create_dirs=True,
        )

    def create(self, item: dict) -> int:
        """Original documentation was not provided."""
        id = self._db.insert(item)
        return id

    def read(self, id: int):
        """Original documentation was not provided."""
        item = self._db.get(doc_id=id)
        return item

    def read_all(self):
        """Original documentation was not provided."""
        return self._db

    def update(self, id: int, mods) -> None:
        """Original documentation was not provided."""
        changes = {k: v for k, v in mods.items() if v is not None}
        self._db.update(changes, doc_ids=[id])

    def delete(self, id: int) -> None:
        """Original documentation was not provided."""
        self._db.remove(doc_ids=[id])

    def delete_all(self) -> None:
        """Original documentation was not provided."""
        self._db.truncate()

    def count(self) -> int:
        """Original documentation was not provided."""
        return len(self._db)

    def close(self):
        """Original documentation was not provided."""
        self._db.close()
