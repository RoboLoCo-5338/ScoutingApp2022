# ScoutingApp2022

This is  the scouting app that will be used to keep track of other teams' performance at competitions.

## To Download Python

First download Python by going to this link:
https://www.python.org/downloads/

![Alt text](assets/python_download_btn_img.png?raw=true "Download Python button")

Click the big yellow button that says `Download Python 3.X.X`. Once downloaded, wait for instructions. If you already know how to install Python, continue as usual, but **make sure to click the checkbox to add Python to the PATH**.

![Alt text](assets/python_path_img.png?raw=true "Add to PATH button")

## To Download This Application

Once Python is downloaded, go back to the GitHub page with this ReadMe. Now download the code by clicking the green `Code` button and click `Download ZIP` from the menu that drops down.

![Alt text](assets/download_zip_img.png?raw=true "Downloading the ZIP file")

Extract the contents of the ZIP file and put them in a location that is easy for you to access. To do this, open the ZIP file and you should see a single folder inside. Click and drag this folder to the outer folder that contains the ZIP file. This action is demonstrated below.

![Alt text](assets/extract_folder_gif.gif?raw=true "Demonstrating how to extract the ZIP")

Open the folder titled `ScoutingApp2022-main` and then click the address bar containing the file path (click on the empty right side of the address bar, where there is just whitespace and no text), so that it highlights the path in blue. Then type `cmd` and press enter. This action is demnstrated below. A black terminal window should appear with white text in which the bottom line has the file path that you just clicked on.

![Alt text](assets/open_cmd_gif.gif?raw=true "Demonstrating how to open cmd")

![Alt text](assets/address_bar_img.png?raw=true "The file explorer address bar")
![Alt text](assets/address_bar_clicked_img.png?raw=true "The highlighted address bar")
![Alt text](assets/address_bar_cmd_img.png?raw=true "Typing cmd in the address bar")

Then with the blinking cursor active on that line, paste in the following command:
`pip install -r requirements.txt`

![Alt text](assets/cmd_requirements_img.png?raw=true "Installing dependencies in cmd")

Press enter and wait for all of those dependencies to install. **Do not type anything until a new terminal line has appeared with your file path followed by a blinking cursor.**

Then paste this command into the next terminal line: `python app.py`. Press enter. Ignore the red warning that appears. Finally, paste the url given in the last line of the output (seen in the red box in the image below) into a browser. Do not close the terminal while using the scouting app.

![Alt text](assets/cmd_app_img.png?raw=true "Running app.py in cmd")

## To Use This Application

First you will see a page to enter the team name/number of the team that you will be scouting. After entering the name, click the blue button.

The observation page comes up. Here you will enter information about the team's performance. Click the `High Goal` and `Low Goal` buttons each time the team scores a high or low goal, respectively. Click the `Oopsy` button to subtract a goal that was accidentally added.

During the autonomous period, select autonomous mode at the top. Track the team's performance during this period. When autonomous is over, click the blue `Submit Session` button at the bottom.

During the rest of the match, have the `Teleop` mode selected, and track the team's performance in the same manner as before. Enter any additional notes on the team's performance in the `Notes` section.

At the end of the match, select the highest climbing bar reached by the robot.

Click the blue `Submit Session` button at the bottom to submit the data.
