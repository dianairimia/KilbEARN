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

// Music    var track = document.getElementById('track');
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
}
