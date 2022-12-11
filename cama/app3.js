let leftCheck = document.getElementById("left");
let rightCheck = document.getElementById("right");

class FacePart {
  constructor(className, timeout = 2000) {
    this.className = className;
    this.domElement = document.getElementsByClassName(className)[0];
    this.appliedClasses = [];
    this.timeout = timeout;
  }

  addClass(className) {
    if (!this.appliedClasses.includes(className)) {
      this.domElement.classList.add(className);
      setTimeout(() => {
        this.removeClass(className);
      }, this.timeout);
    }
  }
  removeClass(className) {
    this.domElement.classList.remove(className);
    this.appliedClasses = [];
  }
}
