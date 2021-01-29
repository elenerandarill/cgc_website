# Class for collecting only selected language translations for each services item.
from typing import List

from landing_page.models import ServicesItem


class ServicesItemView:
    def __init__(self, id_name, lang, headline, content):
        self.id_name = id_name
        self.lang = lang
        self.headline = headline
        self.content = content

    @staticmethod
    def collect_lang_services_items(current_language, items_list: List[ServicesItem]):
        lang_items = []
        for i in items_list:
            translations = i.servicesitemtrans_set.filter(lang=current_language)
            for t in translations:
                item = ServicesItemView(
                    id_name=i.id,
                    lang=t.lang,
                    headline=t.headline,
                    content=t.content
                )
                lang_items.append(item)
        return lang_items

