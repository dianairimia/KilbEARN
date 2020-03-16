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
