# aws-serverless-image-recognition

Company X is a manufacturing company and produces widgets. Company X is in the process innovating their inspection process which has been completely manual to this point. Inspectors take pictures of widgets to ensure that the widgets are within compliance standards set by the Quality Assurance Group.

In order to ensure that the widget manufacturing process meets or achieves standards, the following manual process is currently used:

A digital picture of the widget is taken by a worker on the assembly line
The image is analyzed by the inspector to determine if each of the expected objects on the widget are present
Once the inspection is complete, a message is sent to the Quality Control group with the results of the inspector's analysis.
The original images as well as the analyzed images are stored for compliance purposes for 3 years
The objective of this new project is to automate and innovate the existing process. Company X has decided to create an AWS serverless architecture that has the following requirements:

The current manual inspection process must be as automated as possible (fully automated)
The design and implementation must be serverless and leverage AWS best practices architecture
The inspection process will be automated using AWS image recognition services
The architecture/implementation will be completely event based starting with the presence of the digital image from the assembly line (assume that there is a camera on the assembly line that is able to take images and store them in the cloud).
