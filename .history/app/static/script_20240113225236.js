// static/script.js

function enableTaskInteractivity() {
    $('li').hover(
        function() {
            // Mouse enters: darken background, show red cross
            $(this).css('background-color', '#f8d7da');
            $(this).append('<span class="remove-task">❌</span>');
        },
        function() {
            // Mouse leaves: revert background, hide red cross
            $(this).css('background-color', '#fff');
            $(this).find('.remove-task').remove();
        }
    );

    $('li').click(function() {
        // Click on task: toggle completion
        $(this).toggleClass('completed');
    });
}
