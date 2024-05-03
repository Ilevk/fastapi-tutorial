from dataclasses import dataclass


@dataclass
class PageDTO:
    total: int
    page: int
    limit: int
