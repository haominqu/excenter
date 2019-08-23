// base_url="http://192.168.221.170:8003";
base_url="http://localhost:8000";
var login_url = base_url + "";
var lamp_url = base_url + "";
var curtain_url = base_url + "";
var air_url = base_url + "";
var change_pwd_url = base_url + "";
var ctr_mac_list = base_url + "/onlinemac/controll/list/";
var ctr_mac_url = base_url + "/onlinemac/lamp/";
var token = localStorage.getItem("token");
$(function () {

    var username = localStorage.getItem("username");
    var userid = localStorage.getItem("userid");
    var position = localStorage.getItem("position");
    var department = localStorage.getItem("department");
    var socket = new WebSocket("ws:" + window.location.host + "/userinfo/" + "build_socket/" + userid);
    socket.onopen = function () {

        console.log('WebSocket open');//成功连接上Websocket
    };
    socket.onmessage = function (e) {
        var bdata = $.parseJSON(e.data);
        if(bdata.mac_type==1){
            console.log(bdata);
            if(bdata.mac_st==1){

               $("span[_mid='"+bdata.mac_id+"']").text("开");
               $("input[_mid='"+bdata.mac_id+"']").val("关");
               $("input[_mid='"+bdata.mac_id+"']").attr('onclick','ctr_mac(0,'+bdata.mac_id+')');
            }else {
               $("span[_mid='"+bdata.mac_id+"']").text("关");
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

    // 显示用户信息
    //页面切换
    var on_c = "showpsecond";
    $(".hm_footer_btn").on("click",'div',function () {
        var now_c = $(this).attr("_pg");
        if(now_c!=on_c){
            $('.hm_totle div[name=\''+now_c+'\']').css("display","block");
            $('.hm_totle div[name=\''+now_c+'\']').siblings().css("display","none");
            on_c = $(this).attr("_pg");
        }

    });

    //获取可控设备列表
    $.ajax({
        url:ctr_mac_list,
        type:'get',
        dataType:'json',
        headers:{'Authorization':'JWT '+token},
        data:{
        },
        success:function (res) {
            var data = res.data;
            var showt = "";
            for(let index in data) {
                var showit1 = "<div><span>"+data[index].mac.mac_name+"</span>";
                var showit2 = "";
                if(data[index].mac_status==0){
                    showit2= "<span _mid='"+data[index].mac.id+"'>关</span><span><input type='button' name='ctr_btn' _mid='"+data[index].mac.id+"'  onclick='ctr_mac(1,"+data[index].mac.id+")' value='开'></span></span></div>";
                }else {
                    showit2= "<span _mid='"+data[index].mac.id+"'>开</span><span><input type='button' name='ctr_btn' _mid='"+data[index].mac.id+"'  onclick='ctr_mac(0,"+data[index].mac.id+")' value='关'></span></span></div>";
                }
                showt = showt+showit1+showit2;
            };
            $("div[name='showpfirst']").append(showt);
        },
        error:function (error) {

        }
    })

    // 跳转
    $("div[name='ch_pwd']").on('click',function () {
        console.log("s");
        location.href="/phchpwd/";
    });
    $("div[name='invite']").on('click',function () {
        location.href="/invite/";
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
            console.log(res);

        },
        error:function (error) {
            console.log(error)
        }
    })

}


