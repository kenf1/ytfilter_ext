from datetime import datetime
from typing import Optional, Any, Dict


class VideoDocument:
    def __init__(
        self,
        _id: str,
        video_id: Optional[str],
        published: Optional[str],
        updated: Optional[str],
        title: Optional[str],
        content_url: Optional[str],
        description: Optional[str],
        star_rating_count: Optional[int],
        star_rating_average: Optional[float],
        star_rating_min: Optional[int],
        star_rating_max: Optional[int],
        views: Optional[int],
    ):
        self._id: str = _id
        self.video_id: Optional[str] = video_id
        self.published: Optional[datetime] = (
            datetime.fromisoformat(published) if published else None
        )
        self.updated: Optional[datetime] = (
            datetime.fromisoformat(updated) if updated else None
        )
        self.title: Optional[str] = title
        self.content_url: Optional[str] = content_url
        self.description: Optional[str] = description
        self.star_rating_count: Optional[int] = star_rating_count
        self.star_rating_average: Optional[float] = star_rating_average
        self.star_rating_min: Optional[int] = star_rating_min
        self.star_rating_max: Optional[int] = star_rating_max
        self.views: Optional[int] = views

    @classmethod
    def from_dict(cls, doc: Dict[str, Any]) -> "VideoDocument":
        return cls(
            _id=str(doc.get("_id")),
            video_id=doc.get("video_id"),
            published=doc.get("published"),
            updated=doc.get("updated"),
            title=doc.get("title"),
            content_url=doc.get("content_url"),
            description=doc.get("description"),
            star_rating_count=doc.get("star_rating_count"),
            star_rating_average=doc.get("star_rating_average"),
            star_rating_min=doc.get("star_rating_min"),
            star_rating_max=doc.get("star_rating_max"),
            views=doc.get("views"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
