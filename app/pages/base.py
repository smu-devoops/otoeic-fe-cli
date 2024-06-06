from __future__ import annotations

from typing import Optional


class Page:
    def render(self) -> Optional[Page]:
        """현재 페이지를 방문하고, 다음에 방문할 페이지 객체를 반환한다.

        만약, 더 이상 방문할 페이지가 없다면 `None`을 반환한다.
        """
        raise NotImplementedError
