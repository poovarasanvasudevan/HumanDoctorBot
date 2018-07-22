from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction, EntityFormField, BooleanFormField, FreeTextFormField
from rasa_core.events import SlotSet


class ActionListSlots(Action):
    def name(self):
        return 'action_list_slots'

    def run(self, dispatcher, tracker, domain):
        for key in tracker.slots:
            dispatcher.utter_message(
                "{}: {}".format(key, tracker.slots[key].value)
            )
        return []


class ActionUserProblemForm(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            FreeTextFormField("user_problem"),
            FreeTextFormField("user_location"),
            EntityFormField("user_gender" , 'user_gender'),
            FreeTextFormField("user_doctor_preference"),
        ]

    def name(self):
        return 'action_user_problem_form'

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Submitting your problem...')
        dispatcher.utter_message(
            'Problem: {} Location: {} Gender: {}'.format(
                tracker.get_slot("user_problem"),
                tracker.get_slot("user_location"),
                tracker.get_slot("user_gender"),
            )
        )

        return []
