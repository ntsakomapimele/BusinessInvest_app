$(document).ready(function() {
    $('#businessForm').on('submit', function(e) {
        e.preventDefault(); // Prevent default form submission

        // Perform custom validation (if needed)
        // Display a success message
        alert('Business Registered Successfully!');

        // Optionally, you can reset the form
        $(this).trigger('reset');
    });
});
