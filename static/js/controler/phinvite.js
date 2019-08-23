// base_url="http://192.168.221.170:8003";
base_url="http://localhost:8000";
var login_url = base_url + "/userinfo/staff_guest/login/";
var lamp_url = base_url + "";
var curtain_url = base_url + "";
var air_url = base_url + "";
var change_pwd_url = base_url + "";

$(function () {
    //登录
    $("#btn_login").on("click",function () {
        var username = $("#username").val();
        var password = $("#password").val();
        if(username==""||password==""){
            alert("a");
        }else {
            $.ajax({
                url:login_url,
                type:'post',
                dataType:'json',
                data:{
                    user_name:username,
                    password:password
                },
                success:function (res) {
                    console.log(res);
                    localStorage.setItem("username",res.data.role_name);
                    localStorage.setItem("userid",res.data.user_id);
                    localStorage.setItem("position",res.data.position);
                    localStorage.setItem("department",res.data.department);
                    localStorage.setItem("token",res.data.token);
                },
                error:function () {
 // localStorage.setItem("key","value");//以“key”为名称存储一个值“value”
 //
 //    localStorage.getItem("key");//获取名称为“key”的值
 //
 //    localStorage.removeItem("key");//删除名称为“key”的信息。
 //
 //    localStorage.clear();​//清空localStorage中所有信息
                }
            })
        }
    });





})