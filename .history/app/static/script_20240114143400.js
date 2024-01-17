// // ...

// document.addEventListener("DOMContentLoaded", function () {
//     const inputBox = document.getElementById("input-box");
//     const button = document.querySelector("button");
//     const list = document.getElementById("list-container");

//     list.addEventListener("click", (e) => {
//         if (e.target.tagName === "LI") {
//             e.target.classList.toggle("checked");
//             saveData();
//         } else if (e.target.tagName === "SPAN") {
//             e.target.parentElement.remove();
//             saveData();
//         }
//     });

//     button.addEventListener("click", function () {
//         if (inputBox.value.trim() !== '') {
//             addTask(inputBox.value);
//         } else {
//             alert("Please enter a non-empty task.");
//         }
//     });

//     function addTask(description) {
//         // Make an AJAX request to the Flask server's /add_task route
//         fetch("/add_task", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({ description: description }),
//         })
//             .then(response => response.json())
//             .then(data => console.log(data))
//             .catch(error => console.error("Error:", error));
//     }

//     function showTask() {
//         // Fetch tasks from the Flask server's /tasks route
//         fetch("/tasks")
//             .then(response => response.json())
//             .then(tasks => {
//                 list.innerHTML = ""; // Clear the visible list
//                 tasks.forEach(task => {
//                     let li = document.createElement("li");
//                     li.innerHTML = task.description;
//                     if (task.completed) {
//                         li.classList.add("checked");
//                     }
//                     list.appendChild(li);
//                     let span = document.createElement("span");
//                     span.innerHTML = "x";
//                     li.appendChild(span);
//                 });
//             })
//             .catch(error => console.error("Error:", error));
//     }    

//     window.addEventListener("load", showTask);

//     // Clear Tasks function
//     window.clearTasks = function () {
//         localStorage.removeItem("data");
//         list.innerHTML = ""; // Clear the tasks from the visible list
//     };
// });
