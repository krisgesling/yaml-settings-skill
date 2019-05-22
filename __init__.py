from mycroft import MycroftSkill, intent_file_handler


class YamlSettings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('settings.yaml.intent')
    def handle_settings_yaml(self, message):
        self.speak_dialog('settings.yaml')


def create_skill():
    return YamlSettings()

