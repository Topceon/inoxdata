console.log('kwargs')
$(document).ready(function(){
    $('.btn').click(function(){
        $('.button').append('а')
    })
})

var text = document.getElementById("inputText");

/* return button to variable btn */
var btn = document.getElementById("copyText");

/* call function on button click */
btn.onclick = function() {
  text.select();
  document.execCommand("copy");
}