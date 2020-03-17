//DIANA get the number of players form backend
function getNumberOfPlayers(){
  return 4;
}

//initialise players
var player = new Array(getNumberOfPlayers());
for (i = 0; i < getNumberOfPlayers(); i++){
  player[i] = new Image();
}

//there is no need for array - you'll get where you were and where to go for the current player; counting starts from STARTX and goes clockwise
var currBoardSquare = 0;
var nextBoardSquare = 0;


//DIANA this is the main function -> get the backend to give in which are the files instead of me writing them
function init() {

  player[0].src = 'squaredpython.png';
  player[1].src = 'jssquared.png';
  player[2].src = 'swiftsquared.png';
  player[3].src = 'rubysquared.png';

  window.requestAnimationFrame(draw);
}


//makes sure the images on top of the canvas are in the original quality
function setupCanvas(canvas) {
  var dpr = window.devicePixelRatio || 1;
  var rect = canvas.getBoundingClientRect();
  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  var ctx1 = canvas.getContext('2d');
  ctx1.scale(dpr, dpr);
  return ctx1;
}



//DIANA tell the player where he has to move exactly
function updatePlayerIcon(){



}

//the actual drawing function, that calls itself
function draw() {
  var ctx = setupCanvas(document.querySelector('canvas'));
  ctx.globalCompositeOperation = 'destination-over';
  var clear = ctx.clearRect(0, 0, 570, 570); // clear canvas
  ctx.save();
  ctx.restore();
  ctx.beginPath();
  ctx.stroke();


  var test = 69;
  ctx.drawImage(player[0], 2, 1+test, 23, 23);
  ctx.drawImage(player[1], 27, 1+test, 23, 23);
  ctx.drawImage(player[2], 2, 24+test, 23, 23);
  ctx.drawImage(player[3], 27, 24+test, 23, 23);

  window.requestAnimationFrame(draw);
}




//calling main function
init();









// DICE STUFF
const sides1 = [...document.querySelectorAll(".die-item1")]

function rollDice1() {
  const dice1 = [...document.querySelectorAll(".die-list1")];
  for (let i = 1; i <= 6; i++){
        sides1[i-1].classList.remove("hide-side1");
        console.log(sides1[i-1])
    }
  dice1.forEach(die1 => {
    die1.dataset.roll = getNumber1();
    toggleClasses1(die1);
    console.log(die1)
  });
}

function removeSides1( callback) {

}

function toggleClasses1(die1) {
  die1.classList.toggle("odd-roll");
  die1.classList.toggle("even-roll");
  setTimeout(() => {for (let i = 1; i <= 6; i++){
      if (i == die1.dataset.roll){
        continue;
      }else {
        sides1[i-1].classList.add("hide-side1");
      }}
    }, 1150)
}
//DIANA - get the value from backend for dice1
function getNumber1() {
  return 2;
}

const sides2 = [...document.querySelectorAll(".die-item2")]

function rollDice2() {
  const dice2 = [...document.querySelectorAll(".die-list2")];
  for (let i = 1; i <= 6; i++){
        sides2[i-1].classList.remove("hide-side2");
        console.log(sides2[i-1])
    }
  dice2.forEach(die2 => {
    die2.dataset.roll = getNumber2();
    toggleClasses2(die2);
    console.log(die2)
  });
}

function removeSides2( callback) {


}

function toggleClasses2(die2) {
  die2.classList.toggle("odd-roll");
  die2.classList.toggle("even-roll");
  setTimeout(() => {for (let i = 1; i <= 6; i++){
      if (i == die2.dataset.roll){
        continue;
      }else {
        sides2[i-1].classList.add("hide-side2");
      }}
    }, 1150)
}
//DIANA - get the value from backend for dice2
function getNumber2() {
return 4;
}


document.getElementById("roll-button").addEventListener("click", rollDice1);
document.getElementById("roll-button").addEventListener("click", rollDice2);

// MUSIC
    var track = document.getElementById('track');
    var controlBtn = document.getElementById('play-pause');
    function playPause() {
        if (track.paused) {
            track.play();
            //controlBtn.textContent = "Pause";
            controlBtn.className = "pause";
        } else {
            track.pause();
             //controlBtn.textContent = "Play";
            controlBtn.className = "play";
        }
    }
    controlBtn.addEventListener("click", playPause);
    track.addEventListener("ended", function() {
      controlBtn.className = "play";
    });

// QUIT BUTTON
function loadHomePage() {
    window.location.assign("mainmenu.html");
    alert("test");
}


// alert
var ALERT_TITLE = ":(";
var ALERT_BUTTON_TEXT1 = "YES";
var ALERT_BUTTON_TEXT2 = "NO";

if (document.getElementById) {
  window.alert = function(txt) {
    createCustomAlert(txt);
  }
}

function createCustomAlert(txt) {
  d = document;

  if (d.getElementById("modalContainer")) return;

  mObj = d.getElementsByTagName("body")[0].appendChild(d.createElement("div"));
  mObj.id = "modalContainer";
  mObj.style.height = d.documentElement.scrollHeight + "px";

  alertObj = mObj.appendChild(d.createElement("div"));
  alertObj.id = "alertBox";
  if (d.all && !window.opera) alertObj.style.top = document.documentElement.scrollTop + "px";
  alertObj.style.left = (d.documentElement.scrollWidth - alertObj.offsetWidth) / 2 + "px";
  alertObj.style.visiblity = "visible";

  h1 = alertObj.appendChild(d.createElement("h1"));
  h1.appendChild(d.createTextNode(ALERT_TITLE));

  msg = alertObj.appendChild(d.createElement("p"));
  //msg.appendChild(d.createTextNode(txt));
  msg.innerHTML = txt;

  btn1 = alertObj.appendChild(d.createElement("a"));
  btn1.id = "closeBtn1";
  btn1.appendChild(d.createTextNode(ALERT_BUTTON_TEXT1));
  btn1.href = "#";
  btn1.focus();
  btn1.onclick = function() {
    // removeCustomAlert();
    window.location.assign("mainmenu.html");
    return true;
  }

  btn2 = alertObj.appendChild(d.createElement("a"));
  btn2.id = "closeBtn2";
  btn2.appendChild(d.createTextNode(ALERT_BUTTON_TEXT2));
  btn2.href = "#";
  btn2.focus();
  btn2.onclick = function() {
    removeCustomAlert();
    return false;
  }

  alertObj.style.display = "block";

}

function removeCustomAlert() {
  document.getElementsByTagName("body")[0].removeChild(document.getElementById("modalContainer"));
}

function ful() {
  alert('Alert this pages');
}

//
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
