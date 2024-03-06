from django.urls import path
from .views import (question_list, question_detail, question_vote,
                    question_result, create_polls, all_form, create_option)

urlpatterns = [
    path("", question_list),
    path("<int:question_id>/detail", question_detail, name="detail"),
    path("<int:question_id>/vote", question_vote, name="vote"),
    path("<int:question_id>/result", question_result, name="result"),
    path("add/", create_polls, name='create-polls'),
    path("all/forms", all_form, name="forms"),
    path("add/option", create_option, name="create-option")
]
