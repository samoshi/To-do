// script.js

document.addEventListener("DOMContentLoaded", function () {
    const inputBox = document.getElementById("input-box");
    const button = document.querySelector("button");
    const list = document.getElementById("list-container");

    list.addEventListener("click", (e) => {
        if (e.target.tagName === "LI") {
            e.target.classList.toggle("checked");
            saveData();
        } else if (e.target.tagName === "SPAN") {
            e.target.parentElement.remove();
            saveData();
        }
    });

    button.addEventListener("click", function () {
        addTask(inputBox.value);
    });

    var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked');
        saveData();
    } else if (ev.target.tagName === 'SPAN') {
        // If the clicked element is a SPAN (x), remove the parent LI
        ev.target.parentElement.remove();
        saveData();

        // Make an AJAX request to the Flask server's /remove_task route
        fetch("/remove_task", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ task_id: ev.target.parentElement.dataset.taskId }),
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error("Error:", error));
    }
}, false);

    function addTask(description) {
        console.log("addTask function is called");
        let li = document.createElement("li");
        li.innerHTML = description;
        list.appendChild(li);
        inputBox.value = "";
        let span = document.createElement("span");
        span.innerHTML = "x";
        li.appendChild(span);
        saveData();

        // Make an AJAX request to the Flask server's /add_task route
        fetch("/add_task", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ description: description }),
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error("Error:", error));
    }

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