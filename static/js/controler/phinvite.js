// base_url="http://192.168.221.170:8003";
base_url="http://192.168.188.171:8000";
var invite_list_url = base_url + "/staff/guest/list/";
var token = localStorage.getItem("token");

$(function () {
    $.ajax({
        url:invite_list_url,
        type:'get',
        dataType:'json',
        headers:{'Authorization':'hm JWT '+token},
        data:{
        },
        success:function (res) {
            console.log(res);
            var datas = res.data;
            datas.forEach(v=>{
                console.log(v);
            });
        },
        error:function () {

        }
    })






})