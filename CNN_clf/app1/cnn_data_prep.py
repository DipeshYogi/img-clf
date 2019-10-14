from PIL import Image
import numpy as np
import pickle

def image_predict(data):
    print ('Hey i was called')
    print (data.id)
    print ("."+data.img.url)

    img1 = Image.open("."+data.img.url)
    img1 = img1.convert('L')
    img1 = img1.resize((120,120), Image.ANTIALIAS)
    img1 = np.array(img1)
    img1 = img1.reshape(-1,120,120,1)
    img1 = img1/255
    img1 = img1.astype('float32')
    print (img1)
    print (img1.shape)

    model = pickle.load(open('cnn_model.sav','rb'))

    pred = model.predict(img1)

    print(pred)

    for pred1 in pred:
        if pred1[0] < pred1[1]:
            return 'Adidas'
        else:
            return 'Nike'
