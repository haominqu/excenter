base_url="http://192.168.221.182:8003";
// base_url="http://192.168.188.171:8000";
var login_url = base_url + "/userinfo/staff_guest/login/";
var lamp_url = base_url + "";
var curtain_url = base_url + "";
var air_url = base_url + "";
var change_pwd_url = base_url + "/userinfo/alter/pwd/";
var token = localStorage.getItem("token");
$(function () {
    if(token==null){
        location.href="/phone/";
    }
    var userid = localStorage.getItem("userid");
    $("input[name='oldpwd']").blur(function(){
        if($(this).val()==""){
            $("span[name='oldpwderr']").text("旧密码不能为空");
            $(this).focus();
        }else{
           $("span[name='oldpwderr']").text("");
        }
    });
    $("input[name='newpwd']").blur(function(){
        if($(this).val()==""){
            $("span[name='newpwderr']").text("密码不能为空");
            $(this).focus();
        }else{
           $("span[name='newpwderr']").text("");
        }
    });
    $("input[name='cnewpwd']").blur(function(){
        if($(this).val()==""){
            $("span[name='cnewpwderr']").text("密码不能为空");
            $(this).focus();
        }else{
            if($(this).val()!=$("input[name='newpwd']").val()){
                $("span[name='cnewpwderr']").text("两次密码不一致");

            }else{
                $("span[name='cnewpwderr']").text("");
            }
        }
    });
    // 提交
    $("input[name='cpwd_btn']").on('click',function () {
        var oldpwd = $("input[name='oldpwd']").val();
        var newpwd = $("input[name='newpwd']").val();
        var cnewpwd = $("input[name='cnewpwd']").val();
        if(oldpwd!=""&&newpwd!=""&&cnewpwd!=""&&newpwd==cnewpwd){
            $.ajax({
                url:change_pwd_url,
                type:'put',
                dataType:'json',
                headers:{'Authorization':'JWT '+token},
                data:{
                    user_id:userid,
                    old_pwd:oldpwd,
                    new_pwd:newpwd,
                    c_pwd:cnewpwd,
                },
                success:function (res) {
                    location.href="/phoned/";
                },
                error:function (error) {

                }
            })
        }
    })





})



