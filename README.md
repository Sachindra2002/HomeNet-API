# Research

This research mainly focuses on how natural sound-based context recognition can be applied on mainstream home security systems and the author thought about the possibilities of using sound to infer context and after some research the author found that the power of sound is often overlooked. Research also shows that enormous amount of context information can be deduced from sound. For example, the sound of fireworks may indicate that an event or a festival is going on, the sound of honking may indicate a traffic congestion nearby, a baby crying may indicate the baby is hungry, etc. the “noise” surrounding us is a very good indicator of context.

Even though there is a huge potential of natural sound, there has not been a sound-based context recognition system for home security in the market. To find all the possibilities of using sound-based context recognition in home security, this research will also focus on finding and evaluating an efficient algorithm that can be used to recognize sound or audio.

The main goal of this project is to recognize a certain set of sounds which can happen inside a house using the help of Machine Learning and Deep Learning to learn the differences between the sounds and what features it makes to form a specific sound. Various techniques and technologies will be used to develop this system and evaluate the performance and check what the best and apply it to the final product.

# Problem

Home Security is important for the protection and wellbeing of the people living in their houses and it is the first and foremost protection to the people’s property and those living inside it from a burglary, home intrusion and other environmental disasters. This further gives a peace of mind that your home is protected when you’re sleeping or away and with the modern wireless security systems, people can check in on their houses miles away using the internet. While security systems are a significance expense, the cost of a burglary averages $2,400 per victim and not to mention the psychological impact it can have. 

To solve the above issues, houses are fitted with advance security systems which would contain CCTV cameras to capture and record various angles of the property and motion sensors to detect movements in particular sections of the property, while the above two are good ways in protecting and securing a property, it has some caveats to it.
As images and video data is the most promising and widely available data types to recognize context, images and video data can be affected by the line of sight and the cameras should be positioned towards a specific direction as it only has a field of view between 60° to 110° degrees which also does not provide full coverage.

# Solution

A sound recognition API will be developed where it will have all the capabilities in identifying sound and more functions to cater the user experience. 
To better demonstrate how this product can be applied to smart homes and its use cases, a Raspberry Pi will be used as an IOT device, and an Android mobile app will be developed around the implemented API. The IOT device will act as an input channel for recording natural sound, while the application will be used to connect the IOT device and get the alerts based on the sound detected.

The IOT device could be placed on certain areas of a house and once its installed and connected the IOT device will continuously send audio data to the REST API, When the audio data arrives at the server, the audio data will be sent to the imported Machine Learning model, where the sound will be recognized. After the sound is recognized, based on the sound an alert will be sent to the users’ mobile using Firebase Cloud Messaging Services. Mongo DB will be used as the primary database to this system where it will store all user data and information of the IOT devices and will be used to determine which IOT device is associated with the user.

Currently, this system can only recognize four types of sound, which are the sound of dogs barking which might indicate a person is trespassing, sound of glass breaking which might indicate an intruder, sound of door knocking which might indicate that someone has arrived and sound of a baby crying to wake up sleeping parents. Some of the above sounds may not indicate a threat to a house even though this project is about home security, but the beauty of the smart home is that it could be used much more than a security system and recognize sounds which are not direct threats but could be useful to the users.


![image](https://user-images.githubusercontent.com/52739523/154854366-ba953185-7526-40b7-985d-d1866b79359c.png)

# Related Repositories

- RESTful API Repository - [https://github.com/Sachindra2002/HomeNet-API](https://github.com/Sachindra2002/HomeNet-API)
- Raspberry Pi Code - [https://github.com/Sachindra2002/HomeNet-Raspberry-Pi](https://github.com/Sachindra2002/HomeNet-Raspberry-Pi)
- Jupyter Notebooks - `Not publicly available`

# Neural Netowrks

Two Neural Netowrks were trained as follows

- 11 layer CNN model built from scratch to perform classification for four types of sounds
- Sequential model built using transfer learning from the YAMNet pre-trained model and build a new sequential model to fit the new dataset

# Technologies Used

![ alt text ](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![ alt text ](https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black)
![ alt text ](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![ alt text ](https://camo.githubusercontent.com/2667ec9ca32204207bf4b7e999a3d26874759a9b5aeec22ebb4682ce936d2955/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d4b6572617326636f6c6f723d443030303030266c6f676f3d4b65726173266c6f676f436f6c6f723d464646464646266c6162656c3d)
![ alt text ](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![ alt text ](https://camo.githubusercontent.com/028e2fa50d07bd7e228b89255fa1bd5ad310d1b3d7c327f67e9510398a045272/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d416e64726f696426636f6c6f723d323232323232266c6f676f3d416e64726f6964266c6f676f436f6c6f723d334444433834266c6162656c3d)


# Future Enhancements

- Train a model to identify a huge vareity of sounds
- Integrate home automation (Trigger actions when a certain sound is detected)
- Only start recording when a sound is detected
