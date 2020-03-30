
var xPos, yPos, points = [];
var xhttp = new XMLHttpRequest();
var tim;
var sec = 60;

function init() {

    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext('2d');
    var isDrawing;
    var canvasLeft = canvas.getBoundingClientRect().left;
    var canvasTop = canvas.getBoundingClientRect().top;

    canvas.onmousedown = function(event) {
        isDrawing = true;
        ctx.lineWidth = 10;
        ctx.lineJoin = ctx.lineCap = 'round';
        points.push({ x: event.clientX - canvasLeft, y: event.clientY - canvasTop });
        ctx.moveTo(event.clientX - canvasLeft, event.clientY - canvasTop);
        ctx.lineTo(event.clientX - canvasLeft, event.clientY - canvasTop);
        ctx.stroke();
    };
      
    canvas.onmousemove = function(event) {
        if (isDrawing) {
            points.push({ x: event.clientX - canvasLeft, y: event.clientY - canvasTop });
            ctx.lineTo(event.clientX - canvasLeft, event.clientY - canvasTop);
            ctx.stroke();
        }
    };
      
    canvas.onmouseup = function() {
        isDrawing = false;
    };
}

window.addEventListener('load', init, false);

window.setInterval(function(){
    if(points.length != 0) {

        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                // console.log(this.responseText);
                document.getElementById("predict").innerHTML = this.responseText;
           }
        };

        xhttp.open("GET", "http://127.0.0.1:8000/model/predict/", true);
        var jsonData = JSON.stringify(points);
        xhttp.setRequestHeader("stroke", jsonData);
        xhttp.send();
    }
    points = [];
  }, 1000);

window.onload = function drawTimer() {
    if(sec > 0) {
        document.getElementById("showtimer").innerHTML = "Time left " + sec.toString() + "Seconds";
        sec = parseInt(sec) - 1;
        tim = setTimeout(drawTimer, 1000);
    }
    else if(parseInt(sec) == 0) {
        document.getElementById("showtimer").innerHTML = "Time left " + sec.toString() + "Seconds";
        window.location.replace("http://127.0.0.1:8000/");
    }
}