
// base_url="http://192.168.188.239:8003";
base_url="http://39.106.16.34:8001";

// base_url="http://192.168.188.171:8000";
var invite_list_url = base_url + "/staff/guest/list/";
var invite_add_url = base_url + "/staff/guest/manage/";
var invite_image_url = base_url + "/staff/upload/image/";
var token = localStorage.getItem("token");

$(function () {
    if(token==null){
        location.href="/phone/";
    }
    $("input[name='user_name']").blur(function(){
        var phone = $(this).val();
        if(!(/^1[3456789]\d{9}$/.test(phone))){
            $("span[name='mobilewderr']").text("手机号码有误，请重填");
            $(this).focus();
        }else{
           $("span[name='mobilewderr']").text("");
        }
    });

    $("#file-input").on("change",function(){
        var form_data = new FormData();
        form_data.append('myfiles', this.files[0]);
        var u = navigator.userAgent;
        var phonesys="ABC";
        if (u.indexOf('Android') > -1 || u.indexOf('Linux') > -1) {
            phonesys="android";
            localStorage.setItem("phonesys","android");
        } else if (u.indexOf('iPhone') > -1) {          //苹果手机
            phonesys="iphone";
            localStorage.setItem("phonesys","iphone");
        } else if (u.indexOf('Windows Phone') > -1) {           //winphone手机
            phonesys="wp";
            localStorage.setItem("phonesys","wp");
        };

        // form_data.append('phonesys', phonesys);
       $.ajax({
             url: invite_image_url,
             type: 'POST',
             data:form_data,
             timeout: 200000,
             headers:{'Authorization':'hm JWT '+token,'Phonesys':phonesys},
             processData: false,
             contentType: false,

             beforeSend: function () {
                $("img[name='face_picture']").attr("src","../static/images/icon/timg.gif");
             },
             error:function (err) {
                 console.log(err);
             },
             success:function (res) {

                $("#face_picture").val(res.data);
                console.log(res.data);
                $("img[name='face_picture']").attr("src",res.data);
             },
             complete: function () {
                console.log("aaaa");
             },
        });
    });

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
            var apdom = $("#invite_list");
            datas.forEach(v=>{
                var initemf = "<div class=\"invite_list_it\"><span class=\"invite_list_it_o\">"+v.realname+"</span><span class=\"invite_list_it_s\">"+v.department+"</span>";
                var initems = "";
                if(v.audit_status==0){
                    initems="<span class=\"invite_list_it_t\"><img src='../static/images/icon/nosh.png' alt=''></span></div>";
                    // initems="<span class=\"invite_list_it_t\">未审核</span></div>";
                }else if(v.audit_status==1){
                    initems="<span class=\"invite_list_it_t\"><img src='../static/images/icon/pass.png' alt=''></span></div>";
                    // initems="<span class=\"invite_list_it_t\">通过</span></div>";
                }else{
                    initems="<span class=\"invite_list_it_t\"><img src='../static/images/icon/nopass.png' alt=''></span></div>";
                    // initems="<span class=\"invite_list_it_t\">未通过</span></div>";
                }
                apdom.append(initemf+initems);
            });
        },
        error:function () {

        }
    });


    $("#subinvite").on("click",function () {
        var user_name = $("#user_name").val();
        var real_name = $("#real_name").val();
        var position = $("#position").val();
        var department = $("#department").val();
        var face_picture = $("#face_picture").val();
        if(user_name==""||real_name==""||position==""||department==""||face_picture==""){
            $("span[name='invitewderr']").text("请正确填写信息");
        }

        if(user_name!=""&&real_name!=""&&position!=""&&department!=""&&face_picture!=""){
            $.ajax({
                url:invite_add_url,
                type:'post',
                dataType:'json',
                headers:{'Authorization':'hm JWT '+token},
                data:{
                    user_name:user_name,
                    real_name:real_name,
                    position:position,
                    department:department,
                    face_picture:face_picture,

                },
                success:function (res) {
                    if(res.result==true){
                        location.href="/invite/";
                    }

                },
                error:function () {

                }
            })
        }


    })


});

//
// <script>
//         $(function(){
//  $('input[name=logo]').on('change', function(){
//    //lrz(this.files[0], {width: 640})
//    //.then(function (rst) {
//         var form_data = new FormData();
//         form_data.append('myfiles', this.files[0]);
//        $.ajax({
//              url: 'http://localhost:8000/staff/upload/image/',
//              type: 'POST',
//              data:form_data,
//              timeout: 200000,
//              processData: false,
//              contentType: false,
//              error:function (err) {
//                  console.log(err);
//              },
//              success:function (res) {
//                 $("img[name='face_picture']").attr("src",res.data);
//              },
//         });
//
//   // })
//   // .catch(function (err) {
// //
//   // })
//   //.always(function () {
//
//   // });
//  });
// });
//     </script>