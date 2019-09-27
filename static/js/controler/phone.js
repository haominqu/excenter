
base_url="http://192.168.221.151:8000";

// base_url="http://192.168.188.171:8000";

// base_url="http://192.168.188.171:8000";
// var login_url = base_url + "/userinfo/staff_guest/login/";
var login_url =base_url+ "/userinfo/staff_guest/login/";
var lamp_url = base_url + "";
var curtain_url = base_url + "";
var air_url = base_url + "";
var change_pwd_url = base_url + "";

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');


$(function () {
    //登录
    $("input[name='username']").blur(function(){
        if($(this).val()==""){
            $("span[name='namewderr']").text("用户名不能为空");
            $(this).focus();
        }else{
           $("span[name='namewderr']").text("");
        }
    });
    $("input[name='password']").blur(function(){
        if($(this).val()==""){
            $("span[name='pwdwderr']").text("密码不能为空");
            $(this).focus();
        }else{
           $("span[name='pwdwderr']").text("");
        }
    });
    $("#btn_login").on("click",function () {
        var username = $("#username").val();
        var password = $("#password").val();
        if(username==""||password==""){

            $("#error").text("用户名密码不能为空");


        }else {
            $.ajax({
                url:login_url,
                type:'post',
                dataType:'json',
                data:{
                    user_name:username,
                    password:password,
                    csrfmiddlewaretoken:csrftoken,
                },
                success:function (res) {
                        if(res.result==false){
                            $("#error").text(res.error);
                        }else {
                                // console.log("$$$$$",res.data.user_id);
                              localStorage.setItem("username",res.data.role_name);
                              localStorage.setItem("userid",res.data.user_id);
                              localStorage.setItem("position",res.data.position);
                              localStorage.setItem("department",res.data.department);
                              localStorage.setItem("token",res.data.token);
                              localStorage.setItem("role",res.data.role);
                              localStorage.setItem("face_picture",res.data.face_picture);
                              location.href="/phoned/";
                        }

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
