
// base_url="http://192.168.188.239:8003";
base_url="http://192.168.188.171:8000";

// base_url="http://192.168.188.171:8000";
var login_url = base_url + "";
var lamp_url = base_url + "";
var curtain_url = base_url + "";
var air_url = base_url + "";
var change_pwd_url = base_url + "";
var ctr_mac_list = base_url + "/onlinemac/controllm/list/";
var ctr_mac_url = base_url + "/onlinemac/lamp/";
var ctr_mac_url_curtain = base_url + "/onlinemac/curtain/";

var  ctr_mac_atmt = base_url + "/onlinemac/mac/mode/";
var token = localStorage.getItem("token");




$(function () {
    if(token!=null){
        var username = localStorage.getItem("username");
        var userid = localStorage.getItem("userid");
        var position = localStorage.getItem("position");
        var department = localStorage.getItem("department");
        var role = localStorage.getItem("role");
        var socket = new WebSocket("ws:" + window.location.host + "/userinfo/" + "build_socket/" + userid);
        socket.onopen = function () {
            console.log('WebSocket open');//成功连接上Websocket
        };
        socket.onmessage = function (e) {
            var bdata = $.parseJSON(e.data);
            if(bdata.mac_type==1){
                console.log("####",bdata);

                $("input[_mid='"+bdata.mac_id+"']").attr("disabled",false);
                if(bdata.mac_st==1){

                   $("div[_mid='"+bdata.mac_id+"'] img").attr("src","../static/images/icon/lamp2.png");
                   $("input[_mid='"+bdata.mac_id+"']").val("关");
                   $("input[_mid='"+bdata.mac_id+"']").attr("checked",true);
                   $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_mac(0,'+bdata.mac_id+')');
                }else {
                   $("div[_mid='"+bdata.mac_id+"'] img").attr("src","../static/images/icon/lamp.png");

                   $("input[_mid='"+bdata.mac_id+"']").val("开");
                   $("input[_mid='"+bdata.mac_id+"']").attr("checked",false);

                   $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_mac(1,'+bdata.mac_id+')');
                };
            }else if(bdata.mac_type==2){
                console.log();
                // 光感
                if(bdata.mac_sty=='19'){
                    console.log(bdata.mac_st);
                    $('#light').text(bdata.mac_st);
                }else if(bdata.mac_sty=="Ar"){
                    // 窗帘
                    console.log("a"+bdata.mac_st);
                     $("input[_mid='"+bdata.mac_id+"']").attr("disabled",false);
                if(bdata.mac_st==100){

                   $("div[_mid='"+bdata.mac_id+"'] img").attr("src","../static/images/icon/lamp2.png");
                   $("input[_mid='"+bdata.mac_id+"']").val("关");
                   $("input[_mid='"+bdata.mac_id+"']").attr("checked",true);
                   $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_ar_mac(0,'+bdata.mac_id+')');
                }else {
                   $("div[_mid='"+bdata.mac_id+"'] img").attr("src","../static/images/icon/lamp.png");

                   $("input[_mid='"+bdata.mac_id+"']").val("开");
                   $("input[_mid='"+bdata.mac_id+"']").attr("checked",false);

                   $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_ar_mac(1,'+bdata.mac_id+')');
                };
                }



            }


        };

        // 基础信息
        $("span[name='realname']").text(username);
        $("span[name='position']").text(position);

        // 显示用户信息
        //页面切换
        var on_c = "showpsecond";
        $(".hm_footer_btn").on("click",'div',function () {
            var now_c = $(this).attr("_pg");
            if(now_c!=on_c){
                // $('.hm_totle div[name=\''+now_c+'\']').animate({ left:"100",opacity:1},1000,function(){
                //     $(this).css("display","block");
                //     $(this).siblings().css("display","none");
                //     on_c = $(this).attr("_pg");
                // })
                $('.hm_totle div[name=\''+now_c+'\']').css("display","block");
                $('.hm_totle div[name=\''+now_c+'\']').siblings().css("display","none");
                on_c = $(this).attr("_pg");
            }

            if(now_c=="showpfirst"){

                $(this).children("span").children("img").attr("src","../static/images/icon/eye-fill.png");
                $(this).children("span").css("color","#75a2ff");
                $("div[_pg='showpsecond']").children("span").children("img").attr("src","../static/images/icon/foot_index.png");
                $("div[_pg='showpsecond']").children("span").css("color","#909090");
                $("div[_pg='showpthird']").children("span").children("img").attr("src","../static/images/icon/foot_self.png");
                $("div[_pg='showpthird']").children("span").css("color","#909090");

            }else if(now_c=="showpsecond"){
                $(this).children("span").children("img").attr("src","../static/images/icon/eye-fill.png");
                $(this).children("span").css("color","#75a2ff");
                $("div[_pg='showpfirst']").children("span").children("img").attr("src","../static/images/icon/foot_ctrl.png");
                $("div[_pg='showpfirst']").children("span").css("color","#909090");
                $("div[_pg='showpthird']").children("span").children("img").attr("src","../static/images/icon/foot_self.png");
                $("div[_pg='showpthird']").children("span").css("color","#909090");

            }else if(now_c=="showpthird"){
                $(this).children("span").children("img").attr("src","../static/images/icon/eye-fill.png");
                $(this).children("span").css("color","#75a2ff");
                $("div[_pg='showpsecond']").children("span").children("img").attr("src","../static/images/icon/foot_index.png");
                $("div[_pg='showpsecond']").children("span").css("color","#909090");
                $("div[_pg='showpfirst']").children("span").children("img").attr("src","../static/images/icon/foot_ctrl.png");
                $("div[_pg='showpfirst']").children("span").css("color","#909090");

            }

        });

        // 获取个人权限

;        if(role==3){
             $("div[name='invite']").css("display","none");
        }


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
                console.log(res);

                var data = res.data;
                var showt = "";

                for(let index in data) {
                    console.log(data[index]);
                    var showit1 = "<div class=\"hm_ctr_block\"><div>"+data[index].mac.mac_name+"</div>";
                    var showit2 = "";
                    console.log(data[index].mac.mac_type);
                    if(data[index].mac.mac_type=="62"){
                        if(data[index].mac_status==0){
                            showit2= "<div _mid=\""+data[index].mac.id+"\"><img src=\"../static/images/icon/lamp.png\"></div><div class=\"switch\"><input type=\"checkbox\" onclick=\"ctr_mac(1,"+data[index].mac.id+")\" _mid=\""+data[index].mac.id+"\" class=\"control\"><label for=\"control\" class=\"checkbox\"></label></div></div>";
                        }else {
                            showit2= "<div _mid=\""+data[index].mac.id+"\"><img src=\"../static/images/icon/lamp2.png\"></div><div class=\"switch\"><input type=\"checkbox\" onclick=\"ctr_mac(0,"+data[index].mac.id+")\" _mid=\""+data[index].mac.id+"\" class=\"control\" checked=\"true\"><label for=\"control\" class=\"checkbox\"></label></div></div>";
                        }
                    }else if(data[index].mac.mac_type=="Ar"){
                        if(data[index].mac_status==0){
                            showit2= "<div _mid=\""+data[index].mac.id+"\"><img src=\"../static/images/icon/arclose.png\"></div><div class=\"switch\"><input type=\"checkbox\" onclick=\"ctr_ar_mac(1,"+data[index].mac.id+")\" _mid=\""+data[index].mac.id+"\" class=\"control\"><label for=\"control\" class=\"checkbox\"></label></div></div>";
                        }else {
                            showit2= "<div _mid=\""+data[index].mac.id+"\"><img src=\"../static/images/icon/aropen.png\"></div><div class=\"switch\"><input type=\"checkbox\" onclick=\"ctr_ar_mac(0,"+data[index].mac.id+")\" _mid=\""+data[index].mac.id+"\" class=\"control\" checked=\"true\"><label for=\"control\" class=\"checkbox\"></label></div></div>";
                        }
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
        });



// 获取自动手动
         $.ajax({
            url:ctr_mac_atmt,
            type:'get',
            dataType:'json',
            headers:{'Authorization':'hm JWT '+token},
            data:{
            },
            success:function (res) {
                // console.log("***res");
                if(res.data==1){

                    $("#atmt").text("自动");
                    $("#atmt").attr("_atmt","at");
                    $(".control").attr("disabled",true);

                }else {
                    $("#atmt").text("手动");
                    $("#atmt").attr("_atmt","mt");
                    $(".control").attr("disabled",false);

                };
                },
            error:function (error) {

            }
        });

        // 自动手动
        $("#atmt").on("click",function () {
            var atmt = $(this).attr("_atmt");
            if(atmt == "at"){
                $.ajax({
                    url:ctr_mac_atmt,
                    type:'put',
                    dataType:'json',
                    headers:{'Authorization':'hm JWT '+token},
                    data:{
                        mac_mode:2,
                    },
                    success:function (res){
                        $("#atmt").text("手动");
                        $("#atmt").attr("_atmt","mt");
                        $(".control").attr("disabled",false);
                    },
                    error:function (error){

                    }
                })
            }else {
                $.ajax({
                    url:ctr_mac_atmt,
                    type:'put',
                    dataType:'json',
                    headers:{'Authorization':'hm JWT '+token},
                    data:{
                        mac_mode:1,
                    },
                    success:function (res){
                        $("#atmt").text("自动");
                        $("#atmt").attr("_atmt","at");
                        $(".control").attr("disabled",true);
                    },
                    error:function (error){


                    }
                })





            }

        })

        // 跳转
        $("div[name='ch_pwd']").on('click',function () {
            // console.log("s");
            location.href="/phchpwd/";
        });
        $("div[name='invite']").on('click',function () {
            location.href="/invite/";
        });
        $("#logout").on('click',function () {
            localStorage.clear();
            location.href="/phone/";
        });

    }else {
        location.href="/phone/";
    }


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

// 开关灯点击
function ctr_ar_mac(mac_st,mac_id) {
    $.ajax({
        url:ctr_mac_url_curtain,
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


