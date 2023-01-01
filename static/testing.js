let colors = ['#F06543','#2E294E','#D9BBF9','#DDF8E8','#05B2DC'];
let index = 0;

function changeColor() {
  let box = document.getElementById('box1');
  box.style.borderColor = colors[index];
  index = (index + 1) % colors.length;
}

setInterval(changeColor, 400); // change color every 1000 milliseconds (1 second)