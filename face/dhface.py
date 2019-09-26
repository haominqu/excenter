from django.conf import settings
from userinfo.models import Guest, UserInfo, UserDetail
from userinfo.fourrandom import generate_code
from urllib import parse
from urllib import request
import uuid
import base64
import requests
import os
import json
import time


class AccessControlFaceManage():

    def face_regist(self, guest_id):
        url = "http://10.11.30.89:25000/service"
        action = "addface"
        guest = Guest.objects.filter(user_id=guest_id)
        faceid = int(str(guest[0].id) + generate_code())
        realname = guest[0].realname
        face_db_path = guest[0].face_picture
        face_path = "/media" + str(face_db_path)
        abs_path = settings.BASE_DIR + face_path
        with open(abs_path, 'rb') as f:
            face_base64 = base64.b64encode(f.read())
        payload = {'action': action, 'faceid': faceid, 'base64': face_base64, 'realname':realname}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        print(res_status)
        if res_status == 0:
            UserInfo.objects.filter(id=guest[0].user_id).update(dh_id=faceid)
            return 0
        else:
            return res_status

    def staff_face_regist(self, staff_id):
        url = "http://10.11.30.89:25000/service"
        action = "addface"
        guest = UserDetail.objects.filter(user_id=staff_id)
        faceid = int(str(guest[0].id) + generate_code())
        realname = guest[0].realname
        face_db_path = guest[0].face_picture
        face_path = "/media" + str(face_db_path)
        abs_path = settings.BASE_DIR + face_path
        with open(abs_path, 'rb') as f:
            face_base64 = base64.b64encode(f.read())
        payload = {'action': action, 'faceid': faceid, 'base64': face_base64, 'realname':realname}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        if res_status == 0:
            UserInfo.objects.filter(id=guest[0].user_id).update(dh_id=faceid)
            return 0
        else:
            return res_status

    def get_face_list(self):
        url = "http://10.11.30.89:25000/service"
        action = "regedfacelist"
        payload = {'action': action}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        return response.text

    def member_clear(self):
        url = "http://10.11.30.89:25000/service"
        action = "clearface"
        payload = {'action': action}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        return response.text


    def face_delete(self, face_id):
        url = "http://10.11.30.89:25000/service"
        action = "del"
        payload = {'action': action, 'faceid':face_id}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        if res_status == 0:
            UserInfo.objects.filter(id=guest[0].user_id).update(dh_id=None)
            return 0
        else:
            return res_status



class YiTiFaceManage():

    def face_regist(self, guest_id):
        url = "http://10.11.30.91:25000/service"
        action = "addface"
        guest = Guest.objects.filter(user_id=guest_id)
        faceid = int(str(guest[0].id) + generate_code())
        realname = guest[0].realname
        face_db_path = guest[0].face_picture
        face_path = "/media" + str(face_db_path)
        abs_path = settings.BASE_DIR + face_path
        with open(abs_path, 'rb') as f:
            face_base64 = base64.b64encode(f.read())
        payload = {'action': action, 'faceid': faceid, 'base64': face_base64, 'realname':realname}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        print(res_status)
        if res_status == 0:
            UserInfo.objects.filter(id=guest[0].user_id).update(dh_id=faceid)
            return 0
        else:
            return res_status

    def staff_face_regist(self, staff_id):
        url = "http://10.11.30.91:25000/service"
        action = "addface"
        guest = UserDetail.objects.filter(user_id=staff_id)
        print(len(guest))
        faceid = int(str(guest[0].id) + generate_code())
        realname = guest[0].realname
        face_db_path = guest[0].face_picture
        face_path = "/media" + str(face_db_path)
        abs_path = settings.BASE_DIR + face_path
        with open(abs_path, 'rb') as f:
            face_base64 = base64.b64encode(f.read())
        payload = {'action': action, 'faceid': faceid, 'base64': face_base64, 'realname':realname}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        print(response.text)
        if res_status == 0:
            UserInfo.objects.filter(id=guest[0].user_id).update(dh_id=faceid)
            return 0
        else:
            return res_status


    def get_face_list(self):
        url = "http://10.11.30.91:25000/service"
        action = "regedfacelist"
        payload = {'action': action}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        return response.text

    def member_clear(self):
        url = "http://10.11.30.91:25000/service"
        action = "clearface"
        payload = {'action': action}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        return response.text


    def face_delete(self, face_id):
        url = "http://10.11.30.91:25000/service"
        action = "del"
        payload = {'action': action, 'faceid':face_id}
        response = requests.post(url=url, data=payload)
        response.encoding = 'utf-8-sig'
        res_status = json.loads(response.text)['status']
        if res_status == 0:
            UserInfo.objects.filter(id=guest[0].user_id).update(dh_id=None)
            return 0
        else:
            return res_status










































