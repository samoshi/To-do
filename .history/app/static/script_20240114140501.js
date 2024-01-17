// ...

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
        if (inputBox.value.trim() !== '') {
            addTask(inputBox.value);
        } else {
            alert("Please enter a non-empty task.");
        }
    });

    function addTask(description) {
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
    
            // Add "x" buttons to the tasks
            const tasks = document.querySelectorAll('#list-container li');
            tasks.forEach(task => {
                let li = document.createElement("li");
                li.innerHTML = task.description;
                if (task.completed) {
                    li.classList.add("checked");
                }
                let span = document.createElement("span");
                span.innerHTML = "x";
                task.appendChild(span);
            });
        }
    }

    window.addEventListener("load", showTask);

    // Clear Tasks function
    window.clearTasks = function () {
        localStorage.removeItem("data");
        list.innerHTML = ""; // Clear the tasks from the visible list
    };
});
