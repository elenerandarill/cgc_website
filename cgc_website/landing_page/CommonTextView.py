# Class for collecting only selected language translations for each team member.
from typing import List

from landing_page.models import CommonText


class CommonTextView:
    def __init__(self, text_id, lang, translation):
        self.id = text_id
        self.lang = lang
        self.translation = translation

    @staticmethod
    def collect_lang_text_translations(current_language, list_of_texts: List[CommonText]):
        lang_texts = []
        for text in list_of_texts:
            translations = text.commontexttrans_set.filter(lang=current_language)
            for t in translations:
                common_text = CommonTextView(
                    text_id=text.id,
                    lang=t.lang,
                    translation=t.translation
                )
                lang_texts.append(common_text)
        return lang_texts
