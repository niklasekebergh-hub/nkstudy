# nkstudy
HTML based web application that turns user input into study guide or practice questions using OPENAI's API. 

Prompt.py (Backend): Uses Flask to send user input from website to OPENAI API, where the gpt4-o-mini model is assigned as a helpful study assistent, and is given the topic and the terms(as a list) from the user input. The API then either generates a study guide or short answer practice questions based on the Flask directions, which is they outputted back onto the page.

Design.html (Frontend): The input is taken in two text boxes. If both are not used, the code will not run and will direct the user to fill both text boxes. Then when either "Study Guide" or "Practice Questions" buttons are pressed, the objects will fade and a loading screen will appear while the API is generating the output. Once the output has been generated, the loading screen will disappear and the output can be found under the original objects.
