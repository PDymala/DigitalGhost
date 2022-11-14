import base64
import io
import urllib.request

import cv2
import numpy as np
from PIL import Image
from django.shortcuts import render


def detector(request):
    if request.method == 'POST':
        try:
            url = request.POST.get('img_url', "")
            # url = "https://storage.googleapis.com/diplabs/digital_ghost/assets/img/face43580.bmp"

            url_response = urllib.request.urlopen(url)

            img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(img, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            im_pil = Image.fromarray(img)
            data = io.BytesIO()
            im_pil.save(data, "JPEG")
            encoded_img = base64.b64encode(data.getvalue())
            decoded_img = encoded_img.decode('utf-8')
            img_data = f"data:image/jpeg;base64,{decoded_img}"
            return render(request, "detector.html", {'img_data': img_data})
        # nie poleca sie tak robic ale dziala, nevermind
        except Exception as e:
            return render(request, "detector.html",
                          {'alert': 'Error in fetching the file. Check your url and try again'})


    else:

        return render(request, 'detector.html', {})
