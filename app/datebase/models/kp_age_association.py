from sqlalchemy import Column, ForeignKey, String

from .base import AbstractModelForTime


class KpAgeAssociation(AbstractModelForTime):
    """Модель связывания ManyToMany.

    Модель содержит:
    - kontrol_point_id: ссылка на id КП
    - ages_category_id: Ссылка на id возрастной категории.
    """

    kontrol_point_id = Column(
        String,
        ForeignKey("kontrolpoints.unique_id"),
    )
    ages_category_id = Column(
        String,
        ForeignKey("agecategorys.unique_id"),
    )
