const card = document.querySelector(".card")
const icon = document.getElementById("main_icon")
const header = document.getElementById("main_header")
const disc = document.getElementById("main_disc")
const temp = document.getElementById("temp")

function rainFunction() {
    card.classList.remove("sun")
    card.classList.remove("cloudy")
    card.classList.remove("thunder")
    card.classList.add("rainy")
    icon.classList.remove("bx-sun")
    icon.classList.remove("bx-cloud-lightning")
    icon.classList.remove("bx-cloud")
    icon.classList.add("bx-cloud-light-rain")
    header.innerHTML = "Rainy"
    disc.innerHTML = "Friday"
    temp.innerHTML = "15°c"
}

function dayFuntion() {
    card.classList.remove("rainy")
    card.classList.remove("cloudy")
    card.classList.remove("thunder")
    card.classList.add("sun")
    icon.classList.remove("bx-cloud-light-rain")
    icon.classList.remove("bx-cloud-lightning")
    icon.classList.remove("bx-cloud")
    icon.classList.add("bx-sun")
    header.innerHTML = "Sunny"
    disc.innerHTML = "Thursday"
    temp.innerHTML = "29°c"
}

function thunderFuntion() {
    card.classList.remove("sun")
    card.classList.remove("cloudy")
    card.classList.remove("rainy")
    card.classList.add("thunder")
    icon.classList.remove("bx-cloud-light-rain")
    icon.classList.remove("bx-sun")
    icon.classList.remove("bx-cloud")
    icon.classList.add("bx-cloud-lightning")
    header.innerHTML = "Thunder"
    disc.innerHTML = "Saturday"
    temp.innerHTML = "10°c"
}

function cloudFunction() {
    card.classList.remove("thunder")
    card.classList.remove("sun")
    card.classList.remove("rainy")
    card.classList.add("cloudy")
    icon.classList.remove("bx-cloud-light-rain")
    icon.classList.remove("bx-sun")
    icon.classList.remove("bx-cloud-lightning")
    icon.classList.add("bx-cloud")
    header.innerHTML = "Cloudy"
    disc.innerHTML = "Sunday"
    temp.innerHTML = "20°c"
}