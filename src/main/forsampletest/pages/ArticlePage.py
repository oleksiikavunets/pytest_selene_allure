from selene.support.jquery_style_selectors import s, ss

from src.main.forsampletest.widgets.ContentWidget import ContentWidget


class ArticlePage:

    def __init__(self):
        self.heading = s(".firstHeading")
        self.sections = ss('[class="mw-headline"]')
        self.content_widget = ContentWidget("[id=toc]")

    def get_heading(self):
        return self.heading

