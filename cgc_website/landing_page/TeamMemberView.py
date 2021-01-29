# Class for collecting only selected language translations for each team member.
from typing import List

from landing_page.models import TeamMember


class TeamMemberView:
    def __init__(self, name, image, lang, role, description):
        self.name = name
        self.image = image
        self.lang = lang
        self.role = role
        self.description = description

    @staticmethod
    def collect_lang_members(current_language, members_list: List[TeamMember]):
        lang_members = []
        for m in members_list:
            translations = m.teammembertrans_set.filter(lang=current_language)
            for t in translations:
                memeber = TeamMemberView(
                    name=m.name,
                    image=m.image,
                    lang=t.lang,
                    role=t.role,
                    description=t.description
                )
                lang_members.append(memeber)
        return lang_members


