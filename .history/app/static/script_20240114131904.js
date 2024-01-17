// script.js

let inputBox;
const button = document.querySelector("button");
const list = document.getElementById("list-container");
console.log("Script loaded!");

// Rest of your code...

function addTask() {
    console.log("addTask function is called");
    let li = document.createElement("li");
    li.innerHTML = inputBox.value;
    list.appendChild(li);
    inputBox.value = "";
    let span = document.createElement("span");
    span.innerHTML = "x";
    li.appendChild(span);
    saveData();
}

document.addEventListener("DOMContentLoaded", function () {
    inputBox = document.getElementById("input-box");

    list.addEventListener("click", (e) => {
        if (e.target.tagName === "LI") {
            e.target.classList.toggle("checked");
            saveData();
        } else if (e.target.tagName === "SPAN") {
            e.target.parentElement.remove();
            saveData();
        }
    });

    button.addEventListener("click", addTask);

    function saveData() {
        localStorage.setItem("data", list.innerHTML);
    }

    function showTask() {
        const savedData = localStorage.getItem("data");
        if (savedData) {
            list.innerHTML = savedData;
        }
    }

    window.addEventListener("load", showTask);

    // Clear Tasks function
    window.clearTasks = function () {
        localStorage.removeItem("data");
        list.innerHTML = ""; // Clear the tasks from the visible list
    };
});