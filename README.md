# Plant Habitability Calculator

## Downloads

1. Make sure you have the Arduino IDE downloaded. This will allow you to interact with the sensor and see the data coming from it. You can find the download here: https://www.arduino.cc/en/software 
2. Download the DHT11_Temp_Humidity.ino file from this GitHub, and open it in the Arduino IDE.
2. Download CoolTerm, which reads the data from the sensor and can write it into a text file. To configure CoolTerm, under options, make sure the COM port number is the same port number in the ArduinoIDE port number. Then, go to Connection, and click "File Capture" to start reading the input. Then, click "Connect" to start writing to the new text file.
3. Download the HabitabilityCheckerWindow.py file from this GitHub, and open it in an IDE of your preference that can run Python. We used Visual Studio Code, which you can find here: https://code.visualstudio.com/download 
4. In the terminal of your Python IDE, use “pip3 install PyQt6” to install the required modules.


## Usage

1. Run the Arduino code on the Arduino microcontroller.
2. Start the CoolTerm process to record the data, making sure to name the text file created to “SensorData.txt”.
3. After letting it gather data, open the same text file in the Python IDE.
4. Run the Python program, which should pull up a window. It should list the recorded temperature and humidity.
5. Use the dropdown menu to see how various plants would do in your recorded conditions!
