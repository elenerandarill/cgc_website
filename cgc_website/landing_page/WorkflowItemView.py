from typing import List

from .models import WorkflowItem


class WorkflowItemView:
    def __init__(self, id_name, lang, title, point01, point02, point03, point04, point05):
        self.id_name = id_name
        self.lang = lang
        self.title = title
        self.point01 = point01
        self.point02 = point02
        self.point03 = point03
        self.point04 = point04
        self.point05 = point05

    @staticmethod
    def collect_lang_workflow_items(current_language, workflow_items_list: List[WorkflowItem]):
        lang_items = []
        for w in workflow_items_list:
            translations = w.workflowitemtrans_set.filter(lang=current_language)
            for t in translations:
                item = WorkflowItemView(
                    id_name=w.id,
                    lang=t.lang,
                    title=t.title,
                    point01=t.point01,
                    point02=t.point02,
                    point03=t.point03,
                    point04=t.point04,
                    point05=t.point05,
                )
                lang_items.append(item)
        return lang_items
