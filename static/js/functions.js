$(document).ready(function () {
    $("#submit").click(function (e) {
        var r1 = $("#r1").children("option:selected").val();
        var r2 = $("#r2").children("option:selected").val();
        var r3 = $("#r3").children("option:selected").val();
        if (r1 === r2 ||
            r1 === r3 ||
            r2 === r3) {
            alert("Each Rotor must be unique. You must not select the same rotor more than once. Please change your rotor selection and try again.");
            console.log(r1, r2, r3);
            e.preventDefault(e);
        }
    })
});


// $(document).ready(function () {
//     var el = $("#r1")
//     $('#r2 option[value=' + el.val() + ']').attr('disabled', 'disabled');
//     $('#r3 option[value=' + el.val() + ']').attr('disabled', 'disabled');
//     var el = $("#r2")
//     $('#r1 option[value=' + el.val() + ']').attr('disabled', 'disabled');
//     $('#r3 option[value=' + el.val() + ']').attr('disabled', 'disabled');
//     var el = $("#r3")
//     $('#r2 option[value=' + el.val() + ']').attr('disabled', 'disabled');
//     $('#r1 option[value=' + el.val() + ']').attr('disabled', 'disabled');
//     $("#r1").change(function () {
//         var el = $(this);
//         $('#r1 option[value=' + el.val() + ']').siblings().removeAttr('disabled'); 
//         var r2 =  $("#r2").children("option:selected").val();
//         var r3 =  $("#r3").children("option:selected").val();
//         $('#r2 option[value=' + el.val() + ']').attr('disabled', 'disabled').siblings().removeAttr('disabled');
//         $('#r3 option[value=' + el.val() + ']').attr('disabled', 'disabled').siblings().removeAttr('disabled');
//         $('#r2 option[value=' + r2 + ']').attr('disabled', 'disabled');
//         $('#r3 option[value=' + r3 + ']').attr('disabled', 'disabled');
//         $('#r1 option[value=' + r2 + ']').attr('disabled', 'disabled');
//         $('#r1 option[value=' + r3 + ']').attr('disabled', 'disabled');
//     });
//     $("#r2").change(function () {
//         var el = $(this);
//         $('#r2 option[value=' + el.val() + ']').siblings().removeAttr('disabled'); 
//         var r1 =  $("#r1").children("option:selected").val();
//         var r3 =  $("#r3").children("option:selected").val();
//         $('#r1 option[value=' + el.val() + ']').attr('disabled', 'disabled').siblings().removeAttr('disabled');
//         $('#r3 option[value=' + el.val() + ']').attr('disabled', 'disabled').siblings().removeAttr('disabled');
//         $('#r1 option[value=' + r1 + ']').attr('disabled', 'disabled');
//         $('#r3 option[value=' + r3 + ']').attr('disabled', 'disabled');
//         $('#r2 option[value=' + r1 + ']').attr('disabled', 'disabled');
//         $('#r2 option[value=' + r3 + ']').attr('disabled', 'disabled');
//     });
//     $("#r3").change(function () {
//         var el = $(this);
//         $('#r3 option[value=' + el.val() + ']').siblings().removeAttr('disabled'); 
//         var r2 =  $("#r2").children("option:selected").val();
//         var r1 =  $("#r1").children("option:selected").val();
//         $('#r2 option[value=' + el.val() + ']').attr('disabled', 'disabled').siblings().removeAttr('disabled');
//         $('#r1 option[value=' + el.val() + ']').attr('disabled', 'disabled').siblings().removeAttr('disabled');
//         $('#r2 option[value=' + r2 + ']').attr('disabled', 'disabled');
//         $('#r1 option[value=' + r1 + ']').attr('disabled', 'disabled');
//         $('#r3 option[value=' + r2 + ']').attr('disabled', 'disabled');
//         $('#r3 option[value=' + r1 + ']').attr('disabled', 'disabled');
//     });



// });