// class facePart {
//   constructor(className, even = false) {
//     this.className = className;
//     this.elmnt = document.getElementsByClassName(className)[0];
//     this.classList = [];
//     this.even = even;
//   }

//   addClass(className) {
//     if (!this.classList.includes(className)) {
//       this.elmnt.classList.add(className);

//       this.classList.push(className);
//     }
//     setTimeout(() => {
//       this.removeClass(className);
//     }, 1500);
//   }
//   removeClass(className) {
//     // if (this.classList.includes(className)) {
//     //   this.classList.splice(this.classList.indexOf(className), 1);
//     // }
//     this.elmnt.classList.remove(className);
//     this.classList = [];
//   }

//   reset() {
//     if (this.classList.length != 0) {
//       this.elmnt.classList.remove(this.classList);
//       this.removeClass(this.classList);
//     }
//   }
// }
class facePart {
  constructor(className, timeout = 2000) {
    this.className = className;
    this.domElement = document.getElementsByClassName(className)[0];
    this.appliedClasses = [];
    this.timeout = timeout;
  }

  addClass(className, reset = true) {
    if (!this.appliedClasses.includes(className)) {
      this.domElement.classList.add(className);
      if (reset) {
        setTimeout(() => {
          this.removeClass(className);
        }, this.timeout);
      }
    }
  }
  removeClass(className) {
    this.domElement.classList.remove(className);
    this.appliedClasses = [];
  }
}

//let e=document.getElementById('mouth').setAttribute("d", "m77 150 c0 20, 40 20, 40 0");
let lip = new facePart("lip");
let lipUpper = new facePart("lip-upper");
let lip12 = new facePart("lip-12");
let lip14 = new facePart("lip-14");
let lip15 = new facePart("lip-15");
let lipRight = new facePart("lip-right");
let lipLeft = new facePart("lip-left");
let mouthWhite = new facePart("mouth-white");
let mouth3 = new facePart("mouth3");
let mouth4 = new facePart("mouth4");
let mouth5 = new facePart("mouth5");
let mouth6 = new facePart("mouth6");
let lidRight = new facePart("lid-right");
let lidLeft = new facePart("lid-left");
let checkLeft = new facePart("check-left");
let checkRight = new facePart("check-right");
let chin = new facePart("chin");
let browRight = new facePart("brow-right");
let browLeft = new facePart("brow-left");
let nose = new facePart("nose");
let leftNose = new facePart("left-nose");
let rightNose = new facePart("right-nose");
let elmouth = new facePart("ell-mouth");

let leftCheck = document.getElementById("left");
let rightCheck = document.getElementById("right");

const elmnts = [
  lip,
  lidLeft,
  lidRight,
  mouthWhite,

  browRight,
  browLeft,
  lidRight,
  lidLeft,
  checkLeft,
  checkRight,
  chin,
  nose,
];

// setTimeout(() => {
//   browRight.addClass("lowerer");
//   browLeft.addClass("lowerer");
//   lidRight.addClass("narrow");
//   lidLeft.addClass("narrow");
//   checkLeft.addClass("raiser");
//   checkRight.addClass("raiser");
// }, 1000);

// setTimeout(()=>{
//   browLeft.classList.remove("lowerer")
//   browRight.classList.remove("lowerer")
// },2000)
function apply(parts) {
  if (leftCheck.checked) {
    parts["right"].element.addClass(parts["right"].className);
  }
  if (rightCheck.checked) {
    parts["left"].element.addClass(parts["left"].className);
  }
}

function neutral() {
  elmnts.forEach((e) => e.reset());
}

function generateButtons() {
  const actions = [
    {
      id: "0",
      name: "neutral",

      action: () => {
        neutral();
      },
    },
    {
      id: "1",
      name: "Inner Brow Raiser",
      action: () => {
        // current.push({
        //   className: "outer",
        //   element: browRight,
        // });
        apply({
          right: {
            className: "inner",
            element: browRight,
          },
          left: {
            className: "inner",
            element: browLeft,
          },
        });
      },
    },
    {
      id: "2",
      name: "Outer Brow Raiser (unilateral, right side)",
      action: () => {
        // current.push({
        //   className: "outer",
        //   element: browRight,
        // });
        apply({
          right: {
            className: "outer",
            element: browRight,
          },
          left: {
            className: "outer",
            element: browLeft,
          },
        });
      },
    },
    {
      id: "3",
      name: "neutral",
    },
    {
      id: "4",
      name: "Brow Lowerer",
      action: () => {
        // current = current.concat([
        //   {
        //     className: "lowerer",
        //     element: browRight,
        //   },
        //   {
        //     className: "lowerer",
        //     element: browLeft,
        //   },
        // ]);
        apply({
          right: {
            className: "lowerer",
            element: browRight,
          },
          left: {
            className: "lowerer",
            element: browLeft,
          },
        });
      },
    },
    {
      id: "5",
      name: "neutral",
      action: () => {
        lidLeft.addClass("raiser");
        lidRight.addClass("raiser");
      },
    },
    {
      id: "6",
      name: "neutral",
      action: () => {
        lidLeft.addClass("narrow");
        lidRight.addClass("narrow");
        checkLeft.addClass("raiser");
        checkRight.addClass("raiser");
      },
    },
    {
      id: "7",
      name: "neutral",
      action: () => {
        lidLeft.addClass("narrow");
        lidRight.addClass("narrow");
      },
    },
    {
      id: "8",
      name: "neutral",
    },
    {
      id: "9",

      name: "winkler",
      action: () => {
        nose.addClass("winkler");
        rightNose.removeClass("hidden");
        leftNose.removeClass("hidden");
      },
    },
    {
      id: "10",
      name: "neutral",
      action: () => {
        lipUpper.removeClass("hidden");
        lip.addClass("hidden");
      },
    },
    {
      id: "11",
      name: "neutral",
      action: () => {
        lipRight.removeClass("hidden");
        lipLeft.removeClass("hidden");
        mouth3.removeClass("hidden");
        mouth4.removeClass("hidden");
      },
    },
    {
      id: "12",

      name: "neutral",
      action: () => {
        lip.addClass("puller");
        lip12.removeClass("hidden");
        setTimeout(() => {
          lip12.addClass("hidden", false);
        }, 2000);
      },
    },
    {
      id: "13",
      name: "neutral",
      action: () => {
        lip.addClass("puffer");
        checkLeft.addClass("lower");
        checkRight.addClass("lower");
      },
    },
    {
      id: "14",
      name: "neutral",
      action: () => {
        lip.addClass("hidden");
        lip14.removeClass("hidden");
      },
    },
    {
      id: "15",
      name: "dimpler",
      action: () => {
        lip.addClass("depressor");
        // lip15.removeClass("hidden")
      },
    },
    {
      id: "16",
      name: "neutral",
      action: () => {
        // lipRight.removeClass("hidden");
        // lipLeft.removeClass("hidden");
        mouthWhite.removeClass("hidden");
        lip.addClass("hidden");
      },
    },
    {
      id: "17",
      name: "neutral",
      action: () => {
        lip.addClass("raiser");
      },
    },
    {
      id: "18",
      name: "neutral",
      action: () => {
        elmouth.removeClass("hidden");

        lip.addClass("hidden");
      },
    },
    {
      id: "0",
      name: "neutral",
    },
  ];
  const parent = document.getElementsByClassName("right_options")[0];
  const doms = actions.map((a) => {
    const btn = document.createElement("button");
    btn.textContent = a.id;
    btn.title = a.name;
    btn.addEventListener("click", () => {
      // neutral()
      a.action();
    });
    return btn;
  });
  for (var d of doms) {
    console.log(d);
    parent.appendChild(d);
  }
}

generateButtons();

// newpath = document.createElementNS("SVG","path");
// newpath.setAttribute("id", "pathIdD");
// newpath.setAttribute("d", "M 1,97.857143 C 19.285714,96.428571 24.016862,131.64801 90.714286,132.85714 140.78762,133.7649 202.79376,66.16041 202.79376,66.16041");
// newpath.setAttribute("stroke", "black");
// newpath.setAttribute("stroke-width", 3);
// newpath.setAttribute("opacity", 1);
// newpath.setAttribute("fill", "none");

// document.getElementById("fullPageID").appendChild(newpath);
