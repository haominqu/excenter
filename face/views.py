# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

# self_project
from userinfo.models import UserInfo, Guest, UserDetail


# base
import logging

# Create your views here.


class StaffFaceView(APIView):
    """
        desc:员工对来宾人脸管理
    """

    def get(self, request, **kwargs):
        """
        desc:查看申请状态, 可查询该员工邀请的所有来宾信息, 也可查询具体某个来宾
        :param request:
        :return:
        """
        token = kwargs['token']
        staff_id = token['user_id']
        guest_id = request.GET.get("guest_id", "")
        if guest_id:
            guest = Guest.objects.filter(user_id=guest_id, invite_id=staff_id)
            guest_se = GuestSerializer(guest, many=False)
        else:
            guest = UserInfo.objects.filter(invite_id=staff_id)
            guest_se = GuestSerializer(guest, many=True)
        guest_data = guest_se.data
        result = True
        data = guest_data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})



    def delete(self, request, **kwargs):
        """
        desc:取消申请
        :param request:
        :return:
        """
        token = kwargs['token']
        staff_id = token['user_id']
        guest_id = request.GET.get("guest_id", "")
        if guest_id == "":
            result = False
            data = ""
            error = "来宾信息错误"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            guest = Guest.objects.filter(user_id=staff_id, invite_id=guest_id)
            guest[0].user.delete()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = "取消失败"
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "已取消"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class AdminReviewFace(APIView):

    def post(self, request):
        """
        desc:管理员审核人脸
        :param request:
        :return:
        """
        guest_id = request.data.get("guest_id", "")
        audit_status = request.data.get("audit_status", "")
        if guest_id == "":
            result = False
            data = ""
            error = "来宾信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        guest = Guest.objects.filter(user_id=guest_id)
        if not guest:
            result = False
            data = ""
            error = "未查询到来宾信息"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            guest[0].audit_status = audit_status
            guest.save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = "操作失败"
            return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "审核成功"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class AdminAlterFace(APIView):

    def put(self, request):
        """
        desc:管理员修改人脸信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user_id = request.data.get('user_id')
        face_picture = request.FILES.get('face_picture', '')
        if user_id == "" or face_picture == "":
            result = False
            data = ""
            error = "用户信息不能为空"
            return JsonResponse({"result": result, "data": data, "error": error})
        user = UserInfo.objects.filter(id=user_id)
        if not user:
            result = False
            data = ""
            error = "未查询到用户信息"
            return JsonResponse({"result": result, "data": data, "error": error})
        if user[0].role == int(2):
            try:
                UserDetail.objects.filter(user_id=user[0].id).update(face_picture=face_picture)
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                data = ""
                error = "未修改成功"
                return JsonResponse({"result": result, "data": data, "error": error})
        elif user[0].role == int(3):
            try:
                Guest.objects.filter(user_id=user[0].id).update(face_picture=face_picture)
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                data = ""
                error = "未修改成功"
                return JsonResponse({"result": result, "data": data, "error": error})
        result = True
        data = "人脸已修改"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class AdminDeleteFace(APIView):

    def delete(self, request):
        """
        desc:管理员删除人脸
        :param request:
        :return:
        """
        user_id = request.data.get("user_id", "")
        user = UserInfo.objects.filter(id=user_id)
        if not user:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            user.delete()
        except ObjectDoesNotExist as e:
            logging.warning()
        result = True
        data = "删除成功"
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})






