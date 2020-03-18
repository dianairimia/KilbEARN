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
 width[i] = 522;
 height[i] = 522;
}
var ownedPlace = new Array(40);
var ownedPlaceWidth = new Array(40);
var ownedPlaceHeight = new Array(40);
var hausesPerProperty = new Array(40);

for (i = 0; i<40; i++){
 ownedPlace[i] = new Image();
 ownedPlace[i].src = '';
 ownedPlaceHeight[i] = 0;
 ownedPlaceWidth[i] = 0;
 hausesPerProperty[i] = 0;
}
var hause = new Image();
hause.src = 'normalHause.png';
var hotel = new Image();
hotel.src = 'fancyHause.png';


//DIANA this is the main function -> get the backend to give in which are the files instead of me writing them (you can make it for cycle if it's easier)
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
 var width = 0;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 522;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 453 - 48*(square - 1);
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 69;
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

function ownedPlaceWidthCalculate(square){
 var width = 1;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 414;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 414 - 48*(square - 1) - 13;
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 17;
   return width;
 }




}

function ownedPlaceHeightCalculate(square){
 var height = 1;
 if((square > 19) && (square < 31)){
   return height;
 }

 if(square < 11){
   height = 414;
   return height;
 }

 if((square > 30) && (square < 40)){
   height = 48*(square - 31) + 17;
   return height;
 }
 if((square > 10) && (square < 20)){
   height = 414 - 48*(square - 11) - 13;
   return height;
 }


}

function hotelWidthCalculate(square){
 var width = 1;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 450;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 432 - 48*(square - 1) - 13;
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 17 + 18;
   return width;
 }




}

function hotelHeightCalculate(square){
 var height = 1;
 if((square > 19) && (square < 31)){
   return height;
 }

 if(square < 11){
   height = 450;
   return height;
 }

 if((square > 30) && (square < 40)){
   height = 48*(square - 31) + 17 + 18;
   return height;
 }
 if((square > 10) && (square < 20)){
   height = 432 - 48*(square - 11) - 13;
   return height;
 }


}

function hauseWidthCalculate(square){
 var width = 1;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 450;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 414 - 48*(square - 1) - 13;
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 17;
   return width;
 }




}

function hauseHeightCalculate(square){
 var height = 1;
 if((square > 19) && (square < 31)){
   return height;
 }

 if(square < 11){
   height = 450;
   return height;
 }

 if((square > 30) && (square < 40)){
   height = 48*(square - 31) + 17;
   return height;
 }
 if((square > 10) && (square < 20)){
   height = 414 - 48*(square - 11) - 13;
   return height;
 }


}

function hause2WidthCalculate(square){
 var width = 1;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 450;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 414 - 48*(square - 1) - 13+12;
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 17+12;
   return width;
 }




}

function hause2HeightCalculate(square){
 var height = 1;
 if((square > 19) && (square < 31)){
   return height;
 }

 if(square < 11){
   height = 450;
   return height;
 }

 if((square > 30) && (square < 40)){
   height = 48*(square - 31) + 17+12;
   return height;
 }
 if((square > 10) && (square < 20)){
   height = 414 - 48*(square - 11) - 13+12;
   return height;
 }


}

function hause3WidthCalculate(square){
 var width = 1;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 450;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 414 - 48*(square - 1) - 13+24;
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 17+24;
   return width;
 }




}

function hause3HeightCalculate(square){
 var height = 1;
 if((square > 19) && (square < 31)){
   return height;
 }

 if(square < 11){
   height = 450;
   return height;
 }

 if((square > 30) && (square < 40)){
   height = 48*(square - 31) + 17+24;
   return height;
 }
 if((square > 10) && (square < 20)){
   height = 414 - 48*(square - 11) - 13+24;
   return height;
 }


}

function hause4WidthCalculate(square){
 var width = 1;
 if((square > 9) && (square < 21)){
   return width;
 }
 if((square == 0) || ((square < 40) && (square > 29))){
   width = 450;
   return width;
 }

 if((square < 10) && (square > 0)){
   width = 414 - 48*(square - 1) - 13+36;
   return width;
 }

 if((square < 30) && (square > 20)){
   width = 48*(square - 21) + 17+36;
   return width;
 }




}

function hause4HeightCalculate(square){
 var height = 1;
 if((square > 19) && (square < 31)){
   return height;
 }

 if(square < 11){
   height = 450;
   return height;
 }

 if((square > 30) && (square < 40)){
   height = 48*(square - 31) + 17+36;
   return height;
 }
 if((square > 10) && (square < 20)){
   height = 414 - 48*(square - 11) - 13+36;
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
   var square = 21;
   var widthNew = calculateWidthNew(square);
   var heigthNew = calculateHeigthNew(square);
   //DIANA whichPlayerToUpdate is pretty self explanatory but you have to get the value from the backend
   var whichPlayerToUpdate = 3;
   if ((width[whichPlayerToUpdate] != widthNew) || (height[whichPlayerToUpdate] != heigthNew)){
     if((width[whichPlayerToUpdate] == 0) && (height[whichPlayerToUpdate] == 0)){
       width[whichPlayerToUpdate] = width[whichPlayerToUpdate] + 3;
     }
     else if((width[whichPlayerToUpdate] == 522) && (height[whichPlayerToUpdate] == 522)){
       width[whichPlayerToUpdate] = width[whichPlayerToUpdate] - 3;
     }
     else if((width[whichPlayerToUpdate] == 522) && (height[whichPlayerToUpdate] == 0)){
       height[whichPlayerToUpdate] = height[whichPlayerToUpdate] + 3;
     }
     else if((width[whichPlayerToUpdate] == 0) && (height[whichPlayerToUpdate] == 522)){
       height[whichPlayerToUpdate] = height[whichPlayerToUpdate] - 3;
     }
     else if(width[whichPlayerToUpdate] == 0){
       height[whichPlayerToUpdate] = height[whichPlayerToUpdate] - 3;
     }
     else if(width[whichPlayerToUpdate] == 522){
       height[whichPlayerToUpdate] = height[whichPlayerToUpdate] + 3;
     }
     else if(height[whichPlayerToUpdate] == 0){
       width[whichPlayerToUpdate] = width[whichPlayerToUpdate] + 3;
     }
     else if(height[whichPlayerToUpdate] == 522){
       width[whichPlayerToUpdate] = width[whichPlayerToUpdate] - 3;
     }
   }

   // check if the property is not owned yet; if it is not sold to anyone yet and someone lands on interval THEN POP UP MODAL
   // $("#myModal").modal('show'); MAYBE WITH THAT
 }

 //DIANA updateOwnership is variable that will trigger and reveal a small image on top to show who is the owner you have to get it from backend
 var updateOwnership = true;
 if (updateOwnership == true){
   //DIANA place is the variable that reveals where does the owner image should appear above you have to get it from backend
   var place = 21;
   //DIANA which player icon should appear on top
   var payerOwenerShipToUpdate = 2;
   ownedPlace[place] = player[payerOwenerShipToUpdate];
   ownedPlaceWidth[place] = ownedPlaceWidthCalculate(place);
   ownedPlaceHeight[place] = ownedPlaceHeightCalculate(place);



}
//DIANA give this functions a true value if you want to change the number of hauses of a certain place from backend
 var updateHauseNumber = true;
 if (updateHauseNumber == true){
//DIANA state which is square should be updated form backend
   var whichHause = 11;
   //DIANA say the number of hauses 0-4 or 5 for a hotel again form the backend
   hausesPerProperty[whichHause] = 2;



 }


 for (i = 0; i < getNumberOfPlayers(); i++){
   if(i == 0){
     ctx.drawImage(player[i], width[i], 1 + height[i], 23, 23);
   }
   if(i == 1){
     ctx.drawImage(player[i], 25 + width[i], 1 + height[i], 23, 23);
   }
   if(i == 2){
     ctx.drawImage(player[i], width[i], 24 + height[i], 23, 23);
   }
   if(i == 3){
     ctx.drawImage(player[i], 25 + width[i], 24 + height[i], 23, 23);
   }
 }
 for (i = 0; i < 40; i++){
   ctx.drawImage(ownedPlace[i], 69 + ownedPlaceWidth[i], 69 + ownedPlaceHeight[i], 17, 17);

   if ((hausesPerProperty[i] > 0) && (hausesPerProperty[i] < 5)){
     if(hausesPerProperty[i] == 1){
       ctx.drawImage(hause, 53+hauseWidthCalculate(i), 53+hauseHeightCalculate(i), 12, 12);
     }
     if(hausesPerProperty[i] == 2){
       ctx.drawImage(hause, 53+hauseWidthCalculate(i), 53+hauseHeightCalculate(i), 12, 12);
       ctx.drawImage(hause, 53+hause2WidthCalculate(i), 53+hause2HeightCalculate(i), 12, 12);
     }
     if(hausesPerProperty[i] == 3){
       ctx.drawImage(hause, 53+hauseWidthCalculate(i), 53+hauseHeightCalculate(i), 12, 12);
       ctx.drawImage(hause, 53+hause2WidthCalculate(i), 53+hause2HeightCalculate(i), 12, 12);
       ctx.drawImage(hause, 53+hause3WidthCalculate(i), 53+hause3HeightCalculate(i), 12, 12);


     }
     if(hausesPerProperty[i] == 4){
       ctx.drawImage(hause, 53+hauseWidthCalculate(i), 53+hauseHeightCalculate(i), 12, 12);
       ctx.drawImage(hause, 53+hause2WidthCalculate(i), 53+hause2HeightCalculate(i), 12, 12);
       ctx.drawImage(hause, 53+hause3WidthCalculate(i), 53+hause3HeightCalculate(i), 12, 12);
       ctx.drawImage(hause, 53+hause4WidthCalculate(i), 53+hause4HeightCalculate(i), 12, 12);

     }


   }
     if (hausesPerProperty[i] == 5){
       ctx.drawImage(hotel, 51+hotelWidthCalculate(i), 51+hotelHeightCalculate(i), 17, 17);
     }

 }



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

// //
// // Get the modal
// var modal = document.getElementById("myModal");
//
// // Get the button that opens the modal
// var btn = document.getElementById("myBtn");
//
// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];
//
// // When the user clicks the button, open the modal
// btn.onclick = function() {
//   modal.style.display = "block";
// }
//
// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }
//
// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }


//
