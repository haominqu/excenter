base_url="http://192.168.221.182:8003";
// base_url="http://192.168.188.171:8000";
var login_url = base_url + "";
var lamp_url = base_url + "";
var curtain_url = base_url + "";
var air_url = base_url + "";
var change_pwd_url = base_url + "";
var ctr_mac_list = base_url + "/onlinemac/controllm/list/";
var ctr_mac_url = base_url + "/onlinemac/lamp/";
var mac_mode_url = base_url + "/onlinemac/mac/mode/";
var logout_url = base_url + "/userinfo/staff_guest/logout/";
var token = localStorage.getItem("token");
$(function () {
    if(token==null){
        location.href="/phone/";
    }
    var username = localStorage.getItem("username");
    var userid = localStorage.getItem("userid");
    var role = localStorage.getItem("role");
    var position = localStorage.getItem("position");
    var department = localStorage.getItem("department");
    var face_picture = localStorage.getItem("face_picture");
    var socket = new WebSocket("ws:" + window.location.host + "/userinfo/" + "build_socket/" + userid);
    socket.onopen = function () {
        console.log('WebSocket open');//成功连接上Websocket
    };
    socket.onmessage = function (e) {
        var bdata = $.parseJSON(e.data);
        if(bdata.mac_type==1){
            $("input[_mid='"+bdata.mac_id+"']").attr("disabled",false);
            if(bdata.mac_st==1){
               $("div[_mid='"+bdata.mac_id+"'] img").attr("src","../static/images/icon/lamp2.png");
               $("input[_mid='"+bdata.mac_id+"']").val("关");
               $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_mac(0,'+bdata.mac_id+')');
            }else {
               $("div[_mid='"+bdata.mac_id+"'] img").attr("src","../static/images/icon/lamp.png");

               $("input[_mid='"+bdata.mac_id+"']").val("开");
               $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_mac(1,'+bdata.mac_id+')');
            };
        }else if(bdata.mac_type==2){
            // 光感
            if(bdata.mac_sty=='19'){
                console.log(bdata.mac_st);
                $('#light').text(bdata.mac_st);
            }else{
                console.log("a");
            }
        }


    };

    // 基础信息
    $(".hm_avater").attr("src",face_picture);
    $("span[name='realname']").text(username);
    $("span[name='position']").text(position);

    // 显示用户信息
    //页面切换
    // var on_c = "showpsecond";
    // $(".hm_footer_btn").on("click",'div',function () {
    //     var now_c = $(this).attr("_pg");
    //     if(now_c!=on_c){
    //         $('.hm_totle div[name=\''+now_c+'\']').css("display","block");
    //         $('.hm_totle div[name=\''+now_c+'\']').siblings().css("display","none");
    //         on_c = $(this).attr("_pg");
    //     }
    //
    // });

    $("#showpfirst").on("click",function () {
        var now_c = $(this).attr("_pg");
        if(now_c=="showpfirst"){
             $('.hm_totle div[name=\''+now_c+'\']').css("display","block");
             $('.hm_totle div[name=\''+now_c+'\']').siblings().css("display","none");
             $(this).attr("_pg","showpsecond");
             $(this).children("img").attr("src","../static/images/icon/back.png");
        }else{
            $('.hm_totle div[name=\'showpsecond\']').css("display","block");
             $('.hm_totle div[name=\'showpsecond\']').siblings().css("display","none");
             $(this).attr("_pg","showpfirst")
            $(this).children("img").attr("src","../static/images/icon/home.png")
        }

    })
      $("#showpthird").on("click",function () {
        var now_c = $(this).attr("_pg");
             $('.hm_totle div[name=\''+now_c+'\']').css("display","block");
             $('.hm_totle div[name=\''+now_c+'\']').siblings().css("display","none");
             $("#showpfirst").attr("_pg","showpsecond");
             $("#showpfirst").children("img").attr("src","../static/images/icon/back.png");
    })

 //获取可控设备列表
    $.ajax({
        url:ctr_mac_list,
        type:'get',
        dataType:'json',
        headers:{'Authorization':'hm JWT '+token},
        async:false,
        data:{
        },
        success:function (res) {
            var data = res.data;
            var showt = "";
            for(let index in data) {

                var showit1 = "<div class=\"hm_ctr_block\"><div>"+data[index].mac.mac_name+"</div>";
                var showit2 = "";
                if(data[index].mac_status==0){
                    showit2= "<div _mid=\""+data[index].mac.id+"\"><img src=\"../static/images/icon/lamp.png\"></div><div class=\"switch\"><input type=\"checkbox\" onclick=\"ctr_mac(1,"+data[index].mac.id+")\" _mid=\""+data[index].mac.id+"\"  id=\"control\" class=\"control\"><label for=\"control\" class=\"checkbox\"></label></div></div>";
                }else {
                    showit2= "<div _mid=\""+data[index].mac.id+"\"><img src=\"../static/images/icon/lamp2.png\"></div><div class=\"switch\"><input type=\"checkbox\" onclick=\"ctr_mac(0,"+data[index].mac.id+")\" _mid=\""+data[index].mac.id+"\"  id=\"control\" class=\"control\" checked><label for=\"control\" class=\"checkbox\"></label></div></div>";
                }



                //var showit1 = "<div><span>"+data[index].mac.mac_name+"</span>";
                //var showit2 = "";
                //if(data[index].mac_status==0){
                //    showit2= "<span _mid='"+data[index].mac.id+"'>关</span><span><input type='button' name='ctr_btn' _mid='"+data[index].mac.id+"'  onclick='ctr_mac(1,"+data[index].mac.id+")' value='开'></span></span></div>";
                //}else {
                //    showit2= "<span _mid='"+data[index].mac.id+"'>开</span><span><input type='button' name='ctr_btn' _mid='"+data[index].mac.id+"'  onclick='ctr_mac(0,"+data[index].mac.id+")' value='关'></span></span></div>";
                //}
                showt = showt+showit1+showit2;
            };
            $("div[name='showpfirst']").children(".hm_ctr_tol").append(showt);
        },
        error:function (error) {

        }
    })

     $.ajax({
            url:mac_mode_url,
            type:'get',
            dataType:'json',
            headers:{'Authorization':'hm JWT '+token},
            data:{
            },
            success:function (res) {
                var data = res.data;
                if (data == 1){
                    $(".show").text("自动");

                    $(".control").attr("disabled",true);
                    console.log($(".control").disabled);
                }
                else{
                    $(".show").text("手动");
                }
            }
        })
    
    
    
    $(".show").on("click",function () {
        var btn_value = $(".show").text();
        console.log(btn_value);
        if (btn_value == "自动"){
            this.classList.add("selected");
            $(".show").text("手动");
            $.ajax({
            url:mac_mode_url,
            type:'put',
            dataType:'json',
            headers:{'Authorization':'hm JWT '+token},
            data:{
                "mac_mode":2
            },
            success:function (res) {

            }
        })
            $(".hm_ctr_tol input").attr("disabled",false);
        }
        else{
            this.classList.remove("selected");
            $(".show").text("自动");
            $.ajax({
            url:mac_mode_url,
            type:'put',
            dataType:'json',
            headers:{'Authorization':'hm JWT '+token},
            data:{
                "mac_mode":1
            },
            success:function (res) {

            }
        });
            $(".control").attr("disabled",true);

        }
    })


    // 跳转
    $("div[name='ch_pwd']").on('click',function () {
        console.log("s");
        location.href="/phchpwd/";
    });
    if(role==3){
        $("div[name='invite']").css("display","none");
    }
    else {
        $("div[name='invite']").on('click', function () {
            location.href = "/invite/";
        });
    }

    // 注销
    $(".logout").on('click',function () {
        console.log(token);
        $.ajax({
            url:logout_url,
            type:'post',
            dataType:'json',
            headers:{'Authorization':'hm JWT '+token},
            data:{
            },
            success:function (res) {
                location.href="/phoned/";
            }
        })
    });


});




// 开关灯点击
function ctr_mac(mac_st,mac_id) {
    $.ajax({
        url:ctr_mac_url,
        type:'get',
        dataType:'json',
        headers:{'Authorization':'JWT '+token},
        data:{
            mac_id:mac_id,
            mac_st:mac_st,
        },
        success:function (res) {
            $("input[_mid='"+mac_id+"']").attr("disabled",true);
            return false

        },
        error:function (error) {
            return false
        }
    })

}


