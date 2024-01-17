document.addEventListener('DOMContentLoaded', function () {
    const inputBox = document.getElementById("input-box");
    const button = document.querySelector("button");
    const list = document.getElementById("list-container");

    console.log("Script loaded!");

    function addTask() {
        console.log("addTask function is called");
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        list.appendChild(li);
        inputBox.value = '';
        let span = document.createElement("span");
        span.innerHTML = "x";
        li.appendChild(span);
        saveData();
    }

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

    function clearTasks() {
        localStorage.removeItem("data");
        list.innerHTML = ""; // Clear the tasks from the visible list
    }

    window.addEventListener("load", showTask);
});
