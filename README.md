# Weather Predictor App
_I’m working with Courtney Whitson, Linete Estrada, Robby Wilcox, Nick Wilkins to build a weather app so 
that end users can be aware of weather conditions for the day or week, and can properly prepare for the day with tips provided by the app. We are building a weather app to prevent weather confusion throughout the day. _

__General Info:__

* ![weather icon](https://www.iconfinder.com/data/icons/luchesa-vol-9/128/Weather-512.png)
* /* Optional to add missing things that we could of used in our project */

__Technologies Used:__

* [BitBucket](https://bitbucket.org/product)
* [SourceTree](https://www.sourcetreeapp.com/)
* [Jira](https://www.atlassian.com/software/jira)

__Features:__

1. Clothing Predictor
    * In progress by Linete Estrada. This is located in the main.py file as well as the main.kv file.
	* This feature will use current weather conditions to recommend clothing articles to users, such as student, daily. 
	* As a student, I can get recommendations on clothing articles to wear so that I dress appropriately for the current weather conditions 
	
2. Weather Pattern Detector 
	* This feature will notify users, such as students, of changing weather patterns throughout the day  
	* As a student, I can receive weather notifications so that I am up to date with current weather patterns.
	
2. Weather API
	* Completed by Robby Wilcox. This is the way that the weatherapp is getting information to run the rest of the application. This is located in the WeatherAPI.py file
3. Weatherapp site
	* The base layout is completed,  but it is still a blank slate because we have not implemented the code in yet
Status of Project: We currently have a running program that is not connected to the back end where all the information enters. Next step is to get all of the files talking with one another so that we can start compiling a running demo of weather information.	
	
__Robby Wilcox's Next Steps:__

1. Polish up the weather API file so that it prints out the information in a way that meshes well with the other aspects of our program. In the end it will create easy to read and easy to manipulate data so that any team member can work on the data with little more than a quick brushup on the readme file.

__Linete Estrada's Next Steps:__

1. Design a mock version of our GUI to know exactly what we want the actual GUI to look like 
2. Clean up the current UI to match the GUI mock version 

Status of the Project: Currently have a mock version of the Clothing Predictor notifications that the user will be able to see. Next step is to expand the notification tab and include it into the main updated UI.

__Courtney Whitson's Next Steps:__

Status of Project: The Main executable file is functional, but only displays a Label to verify that the window launches.  


2. Connect all the modules to the main executable, and build up the GUI and UI design. Will also begin writing up the test cases for verifying the functionality of the weather app. 


__Nick Wilkins's Next Steps:__
1. Fix the website up and start to work with other team members so that we can get the code runnin.


__Sprint 3 Retrospective:__

__Courtney Whitson's Next Steps:__

Status of Project: We have linked all the '.kv' files to the main executable, and are able to click buttons and navigate the app.
Artifact: Within our source files you will find files ending with the extension '.kv' and 'main.py'. These files contain the GUI design and actions for any clickable items on the page.
		  These files are used when loading the window or any time a button is pressed.

1. Will connect the Weather API to the GUI, to display the weather
2. Create unit tests to verify the functionality of the app
3. Create a downloadable installation for app

__Robby Wilcox's Accomplishments:__

Accomplishments for sprint 3: Successfully completed the weather API for the application. It properly pulls weather information from the internet. I have also completed a weather API DRIVER file so that it can be tested.

* Next Steps:
	1. Create a second API to pull the 7 day forecast.
	2. Wrap both APIs into an easy-to-use format for the other team members.
	3. Create the tips and tricks for weather that is occuring
	
__Linete Estrada's Accomplishments:__

Accomplishments for sprint 3: Succesfully completed a working GUI application which displays a main window as well as a 7 day forecast window and a notification window. The GUI application can be seen in the main.py file which uses the main.kv, forecast.kv, and weather.kv files to add widgets to the windows.

* Next Steps: 
	1. Give the GUI a cleaner, more professional look. 
	2. Replace the buttons with a navigation bar to give users easier access between screens. 
	3. Finish the creation of the notification pop up window that will display information to users.
	
__Kristopher  Wilkins's Next Steps:__

Accomplishments for sprint 3: created a base UML diagram for the application but due to technical problems i have to restart my work on another device.
* Next Steps:
1. Fully the complete the UML using the code provided by team in the master branch
2. Try to create a working application on my device so that we can showcase our product for sprint 3
3. Get with team so that i can figure out who i can help once  my portion is finished 

__Sprint 3 Completed Tasks__

__Robby's Accomplishments:__

Completed the full API with proper documentation for other developers to easily use. Also completed the multi day outlook for a week in advance. Stores the information into an easy to use format that can be routed into the GUI.

__Linete Estrada's Accomplishments:__

Succesfully improved the GUI to give it a cleaner/more professional look and updated the builder to access the correct files. This can be shown in the main.py file and the 'kv' files.

__Kristopher Wilkins's Accomplishments:__

Completed the UML diagram using the code provided by team membes on the master branch, also helped create and format the standard documentation