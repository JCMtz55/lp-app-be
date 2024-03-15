from typing import List


class RecordRequest:
    limit: int
    page: int
    sort: str
    search: str

    def __init__(self, r=None):
        if r is not None:
            self.limit = r["limit"] or 10
            self.page = r["page"] or 1
            self.sort = r["sort"] or ""
            self.search = r["search"] or ""

