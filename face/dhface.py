import requests

class FaceManage():

    def face_register(self, url, action, faceid, base64):
        """
            desc:人脸注册
        """
        payload = {'action':action, 'faceid':faceid, 'base64':base64}
        response = requests.post(url, params=payload)
        print(response.url)
        if response['status'] == 0:
            return True
        else:
            return False

    def face_update(self, url, action, faceid, base64):
        """
            desc:人脸更新
        """
        payload = {'action': action, 'faceid': faceid, 'base64': base64}
        response = requests.post(url, params=payload)
        print(response.url)
        if response['status'] == 0:
            return True
        else:
            return False

    def face_delete(self, url, action, faceid):
        """
            desc:人脸删除
        """
        payload = {'action': action, 'faceid': faceid}
        response = requests.post(url, params=payload)
        print(response.url)
        if response['status'] == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    face = FaceManage()
    face.face_register("http://设备 IP:25000/service")
