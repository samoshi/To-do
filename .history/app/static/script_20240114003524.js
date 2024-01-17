// static/script.js

function enableTaskInteractivity() {
    $('li').hover(
        function() {
            // Mouse enters: darken background, show red cross
            $(this).css('background-color', '#28a7454d');
            $(this).append('<span class="remove-task">❌</span>');
        },
        function() {
            // Mouse leaves: revert background, hide red cross
            $(this).css('background-color', '#fff');
            $(this).find('.remove-task').remove();
        }
    );

    $('li').click(function() {
        // Click on task: toggle completion, remove the task
        $(this).toggleClass('completed').fadeOut('slow', function() {
            $(this).remove();
        });
    });
}
