import cv2
import os
import requests
import json


addr = 'http://localhost:5000'
test_url = addr + '/api/test'

def send_file_to_server(filepath):
	# prepare headers for http request
	content_type = 'image/jpeg'
	headers = {'content-type': content_type}

	# img = cv2.imread((os.path.join('detected_images', '2021-03-13 21/11/55.010059.jpg')))
	# print('imag=', len(img))
	# # encode image as jpeg
	# img_encoded = cv2.imencode('.jpg', img)

	img = cv2.imread(filepath)
	print('client img=', len(img))
	if len(img) > 10:
		# '.jpg'means that the img of the current picture is encoded in jpg format, and the result of encoding in different formats is different.
		img_encoded = cv2.imencode('.jpg', img)[1]
		# imgg = cv2.imencode('.png', img)


		# send http request with image and receive response
		response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
		# decode response
		print(json.loads(response.text))


if __name__ == "__main__":
	send_file_to_server("detected_images/2021-03-13-22-59-56.jpg")