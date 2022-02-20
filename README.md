# Problem

Home Security is important for the protection and wellbeing of the people living in their houses and it is the first and foremost protection to the people’s property and those living inside it from a burglary, home intrusion and other environmental disasters. This further gives a peace of mind that your home is protected when you’re sleeping or away and with the modern wireless security systems, people can check in on their houses miles away using the internet. While security systems are a significance expense, the cost of a burglary averages $2,400 per victim and not to mention the psychological impact it can have. 

To solve the above issues, houses are fitted with advance security systems which would contain CCTV cameras to capture and record various angles of the property and motion sensors to detect movements in particular sections of the property, while the above two are good ways in protecting and securing a property, it has some caveats to it.
As images and video data is the most promising and widely available data types to recognize context, images and video data can be affected by the line of sight and the cameras should be positioned towards a specific direction as it only has a field of view between 60° to 110° degrees which also does not provide full coverage.

# Solution

a sound recognition API will be developed where it will have all the capabilities in identifying sound and more functions to cater the user experience. 
To better demonstrate how this product can be applied to smart homes and its use cases, a Raspberry Pi will be used as an IOT device, and an Android mobile app will be developed around the implemented API. The IOT device will act as an input channel for recording natural sound, while the application will be used to connect the IOT device and get the alerts based on the sound detected.

The IOT device could be placed on certain areas of a house and once its installed and connected the IOT device will continuously send audio data to the REST API, When the audio data arrives at the server, the audio data will be sent to the imported Machine Learning model, where the sound will be recognized. After the sound is recognized, based on the sound an alert will be sent to the users’ mobile using Firebase Cloud Messaging Services. Mongo DB will be used as the primary database to this system where it will store all user data and information of the IOT devices and will be used to determine which IOT device is associated with the user.

Currently, this system can only recognize four types of sound, which are the sound of dogs barking which might indicate a person is trespassing, sound of glass breaking which might indicate an intruder, sound of door knocking which might indicate that someone has arrived and sound of a baby crying to wake up sleeping parents. Some of the above sounds may not indicate a threat to a house even though this project is about home security, but the beauty of the smart home is that it could be used much more than a security system and recognize sounds which are not direct threats but could be useful to the users.


<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/52739523/154853960-483ca32d-e532-4946-bf64-624f9d084a1e.png">
   <img width="300" src="https://user-images.githubusercontent.com/52739523/154853969-46d2341e-a73b-4f71-b56e-b4c2b30038aa.png">
</p>

![image](https://user-images.githubusercontent.com/52739523/154854366-ba953185-7526-40b7-985d-d1866b79359c.png)




