## path1
* greet
  - utter_greet
  - action_user_problem_form
  - slot{"requested_slot": "user_problem"}
* inform_user_problem{"user_problem: "Eye Problem"}
  - action_user_problem_form
  - slot{"user_problem" : "eye"}   
  - slot{"requested_slot": "user_location"} 
* inform_user_location{"user_location": "my zipcode is 12345"}
  - action_user_problem_form
  - slot{"user_location": "my zipcode is 12345"}
  - slot{"requested_slot": "user_gender"}
* inform_user_gender{"user_gender": "male"}
  - action_user_problem_form
  - slot{"user_gender": "male"}
  - slot{"requested_slot": "user_doctor_preference"}
* inform_user_doctor_preference{"user_doctor_preference": "male"}
  - action_user_problem_form
  - slot{"user_doctor_preference": "male"}
  - slot{"requested_slot": "user_problem_check"}  
* affirm{"user_problem_check": true}
  - slot{"user_problem_check": true}
  - utter_thanks
* bye
  - action_list_slots
  - utter_bye

## path2
* greet
  - utter_greet
  - action_user_problem_form
  - slot{"requested_slot": "user_problem"}
* inform_user_problem{"user_problem: "Eye Problem"}
  - action_user_problem_form
  - slot{"user_problem" : "eye"}   
  - slot{"requested_slot": "user_location"} 
* inform_user_location{"user_location": "my zipcode is 12345"}
  - action_user_problem_form
  - slot{"user_location": "my zipcode is 12345"}
  - slot{"requested_slot": "user_gender"}
* inform_user_gender{"user_gender": "male"}
  - action_user_problem_form
  - slot{"user_gender": "male"}
  - slot{"requested_slot": "user_doctor_preference"}
* inform_user_doctor_preference{"user_doctor_preference": "male"}
  - action_user_problem_form
  - slot{"user_doctor_preference": "male"}
  - slot{"requested_slot": "user_problem_check"}  
* affirm{"user_problem_check": false}
  - slot{"user_problem_check": false}
  - utter_thanks
* bye
  - action_list_slots
  - utter_bye
