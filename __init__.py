from mycroft import MycroftSkill, intent_file_handler


class GinaGreet(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('greet.gina.intent')
    def handle_greet_gina(self, message):
        self.speak_dialog('greet.gina')


def create_skill():
    return GinaGreet()

