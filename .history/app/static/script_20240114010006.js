// script.js
document.addEventListener('DOMContentLoaded', function () {
    const taskItems = document.querySelectorAll('.task-item');

    function handleTaskAction(taskId, isCompleted) {
        const url = isCompleted
            ? '{{ url_for('remove_task', task_id=' + taskId + ') }}'
            : '{{ url_for('complete_task', task_id=' + taskId + ') }}';
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
            const taskId = taskItem.dataset.taskId;
            const isCompletedTask = taskItem.classList.contains('completed-task');

            event.stopPropagation(); // Prevent event propagation to parent elements
            handleTaskAction(taskId, isCompletedTask);
        });
    });
});
