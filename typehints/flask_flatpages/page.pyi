from _typeshed import Incomplete

class Page:
    path: Incomplete
    body: Incomplete
    html_renderer: Incomplete
    folder: Incomplete
    def __init__(self, path, meta, body, html_renderer, folder) -> None: ...
    def __getitem__(self, name): ...
    def __html__(self): ...
    def html(self): ...
    def meta(self): ...
