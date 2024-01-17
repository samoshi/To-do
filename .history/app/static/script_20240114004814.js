// script.js
document.addEventListener('DOMContentLoaded', function () {
    const taskItems = document.querySelectorAll('.task-item');

    function completeTask(url, event) {
        event.stopPropagation();  // Prevent the event from reaching parent elements
        window.location.href = url;
    }

    function removeTask(url, event) {
        event.stopPropagation();  // Prevent the event from reaching parent elements
        window.location.href = url;
    }

    taskItems.forEach((taskItem) => {
        taskItem.addEventListener('mouseover', () => {
            taskItem.classList.add('hovered-task');
        });

        taskItem.addEventListener('mouseout', () => {
            taskItem.classList.remove('hovered-task');
        });

        taskItem.addEventListener('click', (event) => {
            const isCompletedTask = taskItem.classList.contains('completed-task');
            const url = isCompletedTask
                ? '{{ url_for('remove_task', task_id=loop.index-1) }}'
                : '{{ url_for('complete_task', task_id=loop.index-1) }}';

            if (isCompletedTask) {
                removeTask(url, event);
            } else {
                completeTask(url, event);
            }
        });
    });
});
