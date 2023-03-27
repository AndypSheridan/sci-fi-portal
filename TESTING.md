**Functionality**

* Implementation 🏭: I wanted to make sure the game performed as expected from start to finish.
* Test 🧪: I played the game on a local terminal and on Heroku over thirty times.
* Result 🏆: The game worked as anticipated with no errors.
* Verdict ✅: Test passed.

<br>

* Implementation 🏭: Check the input validation was working as expected.
* Test 🧪: Invalid inputs and types were entered multiple times at all possible opportunities.
* Result 🏆: The validation worked well. There were no occasions when it was possible to enter an invalid input.
* Verdict ✅: Test passed.

<br>

* Implementation 🏭: I wanted to make sure the game performed as expected from start to finish.
* Test 🧪: I played the game on a local terminal and on Heroku over thirty times.
* Result 🏆: The game worked as anticipated with no errors.
* Verdict ✅: Test passed.

<br>

* Implementation 🏭: Check the game ends as expected and offers the play again option upon completion.
* Test 🧪: I played the game multiple times, winning and losing. I selected play again and quit at random.
* Result 🏆: The game worked as anticipated with no errors.
* Verdict ✅: Test passed.
<br>
​
**Validators**

* The PEP8 Online Validator was down when creating this project, however I added a PEP8 validator to my workspace by running the command: "pip3 install pycodestyle". The results can be found [here](assets/images/bs1977-pycodestyle.png)

* The validator flags a number of minor warnings, all of which are related to the use of the ASCII art used in the start screen, win screen and lose screen functions. In my final mentor session, I was informed these are inconsequential and can essentially be ignored as they do not affect the program itself.

​
​
## **Bugs**
​
The following bugs were identified during user testing:

* 🐞 - When running the game it was possible for the user and CPU to place ships so that they overlapped.
* ⚒️ - There were errors in the check_ship_placement method of the code.
* ✅ - I made adjustments to the method to prevent any overlap.

<br>

* 🐞 - It was possible for both player and CPU to place ships off the board.
* ⚒️ - There was an error in the populate_boards method.
* ✅ - The entire method was re-written to take into account zero indexing.

​<br>

* 🐞 - Upon re-writing the populate boards method, ship x and y coordinates were reversed so ships did not orient correctly.
* ⚒️ - There was an error with the for loop in the nested if statement in the populate boards method.
* ✅ - I reversed the values for row and column and this fixed the bug.

<br>

* 🐞 - The original SCSS background worked well on a MacBook Pro but caused huge lag and unplayable game quality on some devices.
* ⚒️ - The SCSS was too CPU intensive on some devices.
* ✅ - I used a different background animation which was more subtle but works on all devices in testing.

<br>

* 🐞 - The game was printing too much text for the size of the terminal so the screen was overloaded with information.
* ⚒️ - There is a lot of information to deliver to the user and it all displayed at once which could be overwhelming.
* ✅ - Imported the os and time libraries so I could clear the terminal before delivering the next stage of the game, time was used to slow down printing to the terminal and also simulate computer thinking.


<br>

## **Unfixed Bugs**

* At this stage, there are no known unfixed bugs.

<hr>

Back to [README](/README.md)