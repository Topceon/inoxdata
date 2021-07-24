console.log('kwargs')
$(document).ready(function(){
    $('.btn').click(function(){
        $('.button').append('а')
    })
})

function copyFunction() {
  /* Get the text field */
  var copyText = document.getElementById("for_copy");

  /* Select the text field */
  copyText.select();

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
//  alert("Copied the text: " + copyText.value);
}