// script.js
document.addEventListener('DOMContentLoaded', function () {
    const taskItems = document.querySelectorAll('.task-item');

    function handleTaskAction(url) {
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

            event.stopPropagation(); // Prevent event propagation to parent elements
            handleTaskAction(url);
        });
    });
});
