import os
import pickle
import numpy as np
from keras.models import load_model
from mydecorate import GeneticSelector
from androguard.core.bytecodes.apk import APK

class CustomUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        try:
            return super().find_class(__name__, name)
        except AttributeError:
            return super().find_class(module, name)



permissions = []
with open('DefaultPermList.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        cur_perm = line[:-1]
        permissions.append(cur_perm)

sel = CustomUnpickler(open('temp.pkl', 'rb')).load()

def classify(file):
    vector = {}
    result = 0
    name, sdk, size = 'unknown', 'unknown', 'unknown'
    app = APK(file)
    perm = app.get_permissions()
    name, sdk, size = meta_fetch(file)
    for p in permissions:
        if p in perm:
            vector[p] = 1
        else:
            vector[p] = 0
    data = [v for v in vector.values()]
    data = np.array(data)

    SVC = pickle.load(open('first_model.pkl', 'rb'))
    mysel = sel.support_[0:409]
    # print('#'*50,sel.support_)
    # print('@'*50, len(mysel))
    # print('%'*50, data[mysel], len(data[mysel]))
    remain = 409 - len(data[mysel])

    myinput = np.zeros((409,))
    for (x,), value in np.ndenumerate(data[mysel]):
        # print(x,'#', value)
        myinput[x] = value
        # print('myinput['+ str(x) + ']=',myinput[x])
    # print('-'*50, myinput, len(myinput))
    result = SVC.predict([myinput])
    if result == 'benign':
        result = 'Benign(safe)'
    else:
        result = 'Malware(harm)'
    return result, name, sdk, size


def meta_fetch(apk):
    app = APK(apk)
    return app.get_app_name(), app.get_target_sdk_version(), str(round(os.stat(apk).st_size / (1024 * 1024), 2)) + ' MB'
