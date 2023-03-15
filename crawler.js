// select the unit before writing this code the developer console of the browser
const buttons = document.querySelector(".card-body").childNodes;
let i = 0;
const max = buttons.length;
setInterval(() => {
  if (i >= max) {
    clearInterval();
    return;
  }

  let title = document.querySelector("h1");
  console.log(title.innerText);
  let button = buttons[i].childNodes[0];
  button.click();
  let downloadButton = document.querySelector(
    ".course-exercise-content .d-flex .primary span"
  );
  downloadButton.click();
  i++;
}, 1500);
