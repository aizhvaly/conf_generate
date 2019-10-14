$("#sendForm").on("click", function(){

   var dir0 = $("#dir0").val();
   var dir1 = $("#dir1").val();
   var dir2 = $("#dir2").val();
   var dir3 = $("#dir3").val();
   var dir4 = $("#dir4").val();
   var net_details_s = $("#net_details_s").val();
   var hostname = $("#hostname").val();
   var mgmt_vlan = $("#mgmt_vlan").val();
   var user_vlan = $("#user_vlan").val();
   var other_user_vlans = $("#other_user_vlans").val();

   if(net_details_s == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(hostname == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(mgmt_vlan == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(user_vlan == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(other_user_vlans == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(dir0 == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(dir1 == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(dir2 == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(dir3 == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   } else if(dir4 == "") {
      $("#errMess").text("Не все поля заполнены");
      return false;
   }
    var path = dir0 + dir1 + dir2 + dir3 + dir4
   $("#errMess").text("");

   $.ajax({
       url: 'pyapp/',
       type: 'GET',
       cache: false,
       data: {'net_details_s': net_details_s, 'hostname': hostname, 'mgmt_vlan': mgmt_vlan,
               'user_vlan': user_vlan, 'other_user_vlans': other_user_vlans, 'path': path},
       dataType: 'html',

       beforeSend: function(){
       $("#sendForm").prop("disabled", true);
       },

       success: function (res) {
       if (res.indexOf('phpipam')== -1){
          $("#Response").text("Success")
          $("#Response").attr("href", res);
          $("#Response").attr("hidden", false);
          $("#sendForm").prop("disabled", false);
       }else
           $("#Response").text("IP is already busy. See more...")
           $("#Response").attr("href", res);
           $("#Response").attr("hidden", false);
           $("#sendForm").prop("disabled", false);
           },

       error: function(error){
       $("#errMess").text("OOPS! Smth wrong! Try it again ");
       $("#sendForm").prop("disabled", false);
       }
   });
});

