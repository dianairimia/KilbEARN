 //DIANA get the number of players form backend
function getNumberOfPlayers(){
  return 4;
}

//initialise players
var player = new Array(getNumberOfPlayers());
var width = new Array(getNumberOfPlayers());
var height = new Array(getNumberOfPlayers());
for (i = 0; i < getNumberOfPlayers(); i++){
  player[i] = new Image();
  width[i] = 519;
  height[i] = 522;

}


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

function calculateWidthNew(square){
  var width = 1;
  if((square > 9) && (square < 21)){
    return width;
  }
  if((square == 0) || ((square < 40) && (square > 29))){
    width = 519;
    return width;
  }

  if((square < 10) && (square > 0)){
    width = 451 - 48*(square - 1);
    return width;
  }

  if((square < 30) && (square > 20)){
    width = 48*(square - 21) + 67;
    return width;
  }
}

function calculateHeigthNew(square){
  var height = 0;
  if((square > 19) && (square < 31)){
    return height;
  }

  if(square < 11){
    height = 522;
    return height;
  }

  if((square > 30) && (square < 40)){
    height = 69 + 48*(square - 31);
    return height;
  }
  if((square > 10) && (square < 20)){
    height = 522 - 48*(square - 11) - 69;
    return height;
  }

}


//DIANA the actual drawing function, that calls itself -> you have to get things from backend here
function draw() {
  var ctx = setupCanvas(document.querySelector('canvas'));
  ctx.globalCompositeOperation = 'destination-over';
  var clear = ctx.clearRect(0, 0, 570, 570); // clear canvas
  ctx.save();
  ctx.restore();
  ctx.beginPath();
  ctx.stroke();
  //DIANA this is a true or false variable that is going to trigger the movement update of the player
  var updatePlayer = true;

  if (updatePlayer == true){
    //DIANA square is the number of square that the player has to go to get from backend
    var square = 39;
    var widthNew = calculateWidthNew(square);
    var heigthNew = calculateHeigthNew(square);
    //DIANA whichPlayerToUpdate is pretty self explanatory but you have to get the value from the backend
    var whichPlayerToUpdate = 3;
    if ((width[whichPlayerToUpdate] != widthNew) || (height[whichPlayerToUpdate] != heigthNew)){
      if((width[whichPlayerToUpdate] == 1) && (height[whichPlayerToUpdate] == 0)){
        width[whichPlayerToUpdate] = width[whichPlayerToUpdate] + 1;
      }
      else if((width[whichPlayerToUpdate] == 519) && (height[whichPlayerToUpdate] == 522)){
        width[whichPlayerToUpdate] = width[whichPlayerToUpdate] - 1;
      }
      else if((width[whichPlayerToUpdate] == 519) && (height[whichPlayerToUpdate] == 0)){
        height[whichPlayerToUpdate] = height[whichPlayerToUpdate] + 1;
      }
      else if((width[whichPlayerToUpdate] == 1) && (height[whichPlayerToUpdate] == 522)){
        height[whichPlayerToUpdate] = height[whichPlayerToUpdate] - 1;
      }
      else if(width[whichPlayerToUpdate] == 1){
        height[whichPlayerToUpdate] = height[whichPlayerToUpdate] - 1;
      }
      else if(width[whichPlayerToUpdate] == 519){
        height[whichPlayerToUpdate] = height[whichPlayerToUpdate] + 1;
      }
      else if(height[whichPlayerToUpdate] == 0){
        width[whichPlayerToUpdate] = width[whichPlayerToUpdate] + 1;
      }
      else if(height[whichPlayerToUpdate] == 522){
        width[whichPlayerToUpdate] = width[whichPlayerToUpdate] - 1;
      }


    }



  }


  for (i = 0; i < getNumberOfPlayers(); i++){
    if(i == 0){
      ctx.drawImage(player[i], 2 + width[i], 1 + height[i], 23, 23);
    }
    if(i == 1){
      ctx.drawImage(player[i], 27 + width[i], 1 + height[i], 23, 23);
    }
    if(i == 2){
      ctx.drawImage(player[i], 2 + width[i], 24 + height[i], 23, 23);
    }
    if(i == 3){
      ctx.drawImage(player[i], 27 + width[i], 24 + height[i], 23, 23);
    }
  }



  window.requestAnimationFrame(draw);
}





//calling main function
init();



  // ctx.drawImage(player[0], 2, 1+test, 23, 23);
  // ctx.drawImage(player[1], 27, 1+test, 23, 23);
  // ctx.drawImage(player[2], 2, 24+test, 23, 23);
  // ctx.drawImage(player[3], 27, 24+test, 23, 23);


  // ctx.drawImage(player[0], 2+519, 1+522, 23, 23);
  // ctx.drawImage(player[1], 27+519, 1+522, 23, 23);
  // ctx.drawImage(player[2], 2+519, 24+522, 23, 23);
  // ctx.drawImage(player[3], 27+519, 24+522, 23, 23);
