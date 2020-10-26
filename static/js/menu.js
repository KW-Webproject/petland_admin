const menu = document.querySelector(".nav__menu");
let selected = document.querySelector(".selected");
menu.addEventListener("click", (e) => {
    const target = e.target;
    selected.classList.remove("selected");
    target.classList.add("selected");
    selected = target;
})