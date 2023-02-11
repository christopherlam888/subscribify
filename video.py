from dataclasses import dataclass


@dataclass(eq=True)
class Video:
    title: str
    author: str
    published: str
    videoId: str

    def __lt__(self, other):
        return self.published < other.published
