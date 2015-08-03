/**
 * Created with PyCharm.
 * User: ifcheung
 * Date: 13-10-24
 * Time: 下午1:17
 * To change this template use File | Settings | File Templates.
 */
/**
 * when page load,automatically
 * @param  {notype} ) {               var name descriptions
 * @return {type2}   description2
 */
$(document).ready(function () {
    var name = $('#name').val();
    var msg = "0";   /* username has been already existed! */
    $("#name").blur(function (e) {
        username = $(this).val();
        if (username.length < 6) {
            $("#checkusermsg").html("<font color=\'red\'>用户名长度必须大于6！</font>")
        }
        else {
            $.ajax({
                async: false,
                type: "get",
                url: "/checkuser",
                data: "name=" + username,
                success: function (data) {
                    msg = data;
                }
            })
            if (msg == "1") {
                $('#checkusermsg').html("<font color=\'red\'>您输入的用户名已存在！请重新输入！</font>")
            }
            else {
                $('#checkusermsg').html("<font color=\'green\'>该用户名未被注册，可放心使用！</font>")
            }
        }
    })
});





