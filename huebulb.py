import requests
import time

# http://192.168.1.223/debug/clip.html
url = 'http://192.168.1.223/api/yQ20XplYuzwIu7vh-9qVEAydYsjjHROYIIXyjoRa/lights'

class Bulb:
    def __init__(self, id):
        self.dest = url
        self.id = id
        self.hue = 0
        self.saturation = 254
        self.value = 254
        self.on = True

    def set_hue(self, hue):
        if hue > 0:
            self.hue = hue if hue < 2**16 else 2**16 - 1
        else:
            self.hue = 0

    def set_saturation(self, saturation):
        if saturation > 0:
            self.saturation = saturation if saturation < 2**8 - 1 else 2**8 - 2
        else:
            self.saturation = 0

    def set_value(self, value):
        self.value = value

    def set_on(self, on):
        self.on = 'True' if on else 'False'

    def get_hue(self):
        return self.hue

    def get_saturation(self):
        return self.saturation

    def get_value(self):
        return self.value

    def show(self):
        json_data = {'on': self.on, 'bri': self.value, 'hue': self.hue, 'saturation': self.saturation}
        requests.put(self.dest + '/' + str(self.id) + '/state', json=json_data)
        # print(self.hue, self.saturation, self.value)

    def rainbow(self, cycles=0, speed=0):
        '''
        Display Rainbow Effect
        '''
        if cycles == 0:
            i = 0
            while(True):
                if i > 2**16 - 1:
                    i = 0
                self.set_hue(i)
                i += 1 + speed
                self.show()
                time.sleep(0.1)
        else:
            for _ in range(cycles):
                for i in range(0, 2**16, 1000):
                    self.set_hue(i)
                    self.show()
                    time.sleep(0.25)

















