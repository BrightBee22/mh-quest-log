# MH Rise Quest Log App

## Table of Contents
* [Introduction](#intro)
* [Design](#design)
    * [Entity Diagram](#entity-diagram)
    * [Risk Assessment](#risk-assessment)
    * [Trello Board](#trello-board)
* [App Design](#app)
* [Automation and Testing](#testing)
* [Future Improvements](#future-improvements)
* [Final Thoughts](#final-thoughts)
* [Presentation](#presentation)

## Introduction <a name="intro"></a>
Specifications for this project required a CRUD application utilising "supporting tools, methodologies and technologies that encapsulate all core modules covered during training." 

Based on this, I decided to create a simple application based on one of my favourite games, Monster Hunter. In the game, players go on individual quests where they hunt behemoth sized creatures. My application will store the details of quests for the user and act as a collection to remind them of the details they need for when they want to go on the intended hunt.

## Design <a name="design"></a>
My quest log app should allow users to be able to:
* Create a quest log using (achieving 'Create'):
    * *Hunter Name*
    * *Hunter Rank* - Rank of hunter
    * *Monster Name* - Name of monster that will be hunted
    * *Weapon Used* - Name of weapon that will be used to hunt
* Be able to see their quest log (achieving 'Read')
* Be able to update the quest based on if it's completed (achieving 'Update').
* Be able to delete individual quests (achieving 'Delete').

### Entity Diagram <a name="entity-diagram"></a>
![erd]
The Entity Diagram establishes there will be a one to many relationship between Hunter entities and Quest Log entities, as one hunter can go on many quests but one quest can only contain one hunter. This should allow multiple quest log entries to be linked to one user.


### Risk Assessment <a name="risk-assessment"></a>
![riskassess]
Screenshot of the risk assessment created for the project. Detailing potential issues and how to control/mitigate them.

### Trello Board
To track my progress on the project I used a Trello board (screenshot below). Full link available here: https://trello.com/b/sKPkX93j/mh-rise-quest-log
![trello]
The board allows elements created to be moved section to another easily, meaning they can be tracked from initial creating to completion in implementing code.

* *Epic* - General idea of which the user stories will come from.
* *User Stories* - Functionality implemented into the project based on the user's perspective. Tasks are formed from these stories.
* *Task* - Elements being considered for implemenation in the app. Each task is colour coded based on the MoSCoW system. Green being "Must Have", Yellow being "Should Have", Amber being "Could Have" and Red being "Won't Have".
* *Doing* - Elements that are currently in progress of having code written
* *Finished* - Any element that is considered to be finished 

## App Design <a name="app"></a>
The programming language for the application was Python and the front-end app design was done using Flask, with the database and virtual machine being hosted by GCP. Using WTForms, my app populates 2 separate databases based on user input and calls it back to be read. Coding was done using a feature-branch model
The image below shows the create functionality of the app.
![createapp]
I added a select field for the weapon as there are only 14 weapons in the game and providing them in a drop down box limits user putting in incorrect data.
![validapp]
Another validator I added was having users only be able to set their rank between 1-999, as these are the only possible ranks in the game. Error in the image above shows what happens when users exceed it.
![updateapp]
On the home page, users can see the details are able to read details of the quest they have created and also update it based on if they have completed it or not. The default is set to false, but can be set to true if you click the "complete" button. This results in the hunt completed being set to true and the "complete" button being changed to "incomplete" as you can see from the image.
![deleteapp]
If the user clicks the delete button, the entry is deleted from the database and no longer displayed. As you can see from above, the entry from Hunter Name "Bee" is now gone.

## Automation and Testing <a name="automation"></a>
The CI pipeline for this project is project tracking from Trello and the work load is placed on a code repostitory in GitHub, code development done using Python and edited from Visual Studio Code (VSC) which is pushed back to the GitHub repository and can be pulled to the virtual machine. Jenkins is the CI server I used to automate the testing and building of the application, using a webhook connected to my github repo, allowing me to run the tests automatically and makes it clear where there are areas of issues as a report is formed from this.

Pytest is used to run the unit tests on the application. They assert if a certain function is run, the output has a known value. The table below shows console outputs when Jenkins runs a pytest showing how many passed and how many failed (image below).
![pytest]

Unit tests that were used for the project:
![test]

A coverage report can also be formed which Jenkins can archive as an artifact html document. Image for the coverage report of the project can be found below.
![pycov]

I also used it to build and run the flask app.

## Future Improvements <a name="future-improvements"></a>
Things I would like to do in the future regarding the app are:
* Create a user login feature so each entry is accessible to the user-only and not available to everyone who accesses the website.
* Create another database for monsters, so information can be displayed of monster parts dropped and location.
* Create a many to many relationship, as the model is based on a single player model but in a multiplayer model, multiple hunters can go on the same quest and multiple monsters can be the target of a hunt.
* Add an about page and disclaimer to let people know what the app is about and that there is no official affiliation with the official MH Team.

## Final Thoughts <a name="final-thoughts"></a>
I have created an application that meets the required specifications of the project, using a trello board, relational database with 2 tables and even implemented a feature branch model to my project. However, there are still aspects to work on to make sure users have a great experience, with user login feature being the most important to achieve.

[erd]:https://i.imgur.com/EbNfXDV.png
[riskassess]:https://i.imgur.com/mFqiPx7.png
[trello]:https://i.imgur.com/gZTmmMg.png
[createapp]:https://i.imgur.com/qvy7z3k.png
[readapp]:https://i.imgur.com/fSkZ4YJ.png
[updateapp]:https://i.imgur.com/Ts3ENlj.png
[deleteapp]:https://i.imgur.com/eF3PKtv.png
[validapp]:https://i.imgur.com/y6rjISJ.png
[pytest]:https://i.imgur.com/rKm5nzT.png
[pycov]:https://i.imgur.com/3kI4P0i.png
[test]:https://i.imgur.com/4f9hQNm.png

## Presentation <a name="presentation"></a>
Link to presentation:
https://drive.google.com/file/d/1KyjT4BDp9ZIz2QO6ToIvRaLk1PupGA1S/view?usp=sharing