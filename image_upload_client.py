import base64
import requests
import json

image_file = open("food.jpg", "rb")
#read_file_original_decoded = image_file.read()
encoded_string = base64.b64encode(image_file.read()).decode('utf-8')#base64.b64encode(read_file_original_decoded)
url = "https://vg1g2597w9.execute-api.us-east-1.amazonaws.com/prod/upload-image-s3-function"

payload = {
     "name" : "food444.jpg",
     "file": encoded_string
}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)


# decoded_string = base64.b64decode(encoded_string)
# with open("demofile111.jpg", "wb") as f:
#     f.write(decoded_string)
#
# decoded_string = base64.b64decode(encoded_string)
# with open("demofile222.jpg", "wb") as f:
#     f.write(decoded_string)

print(response)
#print(response.content==read_file_original_decoded)
print(response.content)
print("---")
#print(read_file_original_decoded)
print(len(response.content))
#print(len(read_file_original_decoded))