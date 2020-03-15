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
