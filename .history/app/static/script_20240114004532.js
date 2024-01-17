// script.js
document.addEventListener('DOMContentLoaded', function () {
    const taskItems = document.querySelectorAll('.task-item');

    function completeTask(url) {
        window.location.href = url;
    }

    function removeTask(url) {
        window.location.href = url;
    }

    taskItems.forEach((taskItem) => {
        taskItem.addEventListener('mouseover', () => {
            taskItem.classList.add('hovered-task');
        });

        taskItem.addEventListener('mouseout', () => {
            taskItem.classList.remove('hovered-task');
        });
    });
});
