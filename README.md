# text-to-speech
 Python script to convert text to speech, utilizing Google's Text-to-Speech

##Usage
To use the Text-to-Speech script, follow these steps:

Create a new text file named "_content.txt" in the same directory as the script file.
Open the "_content.txt" file and add the text that you want to convert to speech.
Save and close the "_content.txt" file.
Run the script by executing the following command in your command prompt or terminal: python text_to_speech.py
The script will generate an MP3 file named "#sample_YYYY-MM-DD_HH-MM-SS.mp3" in the same directory as the script file, where "YYYY-MM-DD_HH-MM-SS" represents the current date and time.

##Customization
You can customize the script to suit your needs by modifying the following variables:

lang: The language of the speech. By default, this is set to "en" for English. You can change this to a different language code to generate speech in a different language.
slow: The speed of the speech. By default, this is set to False for normal speed. You can change this to True for slower speech.
You can also modify the filename format of the generated MP3 file by changing the filename variable. For example, you can change "sample" to a different name or remove the timestamp from the filename.

##Troubleshooting
If the script does not generate an MP3 file, check the following:

Make sure that the "_content.txt" file is in the same directory as the script file.
Make sure that the "_content.txt" file contains text that you want to convert to speech.
Make sure that the gtts library is installed in your Python environment.