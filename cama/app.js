//let e=document.getElementById('mouth').setAttribute("d", "m77 150 c0 20, 40 20, 40 0");
let mouth = document.getElementById("mouth");
let browRight = document.getElementsByClassName("brow-right")[0];
let browLeft = document.getElementsByClassName("brow-left")[0];

setTimeout(()=>{
  browLeft.classList.add("lowerer")
  browRight.classList.add("lowerer")
},1000)

setTimeout(()=>{
  browLeft.classList.remove("lowerer")
  browRight.classList.remove("lowerer")
},2000)
// setTimeout(() => {
//   mouth.classList.add("sad");
// }, 1500);
