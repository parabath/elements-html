<!DOCTYPE html>
<html>
<head>
    <title>Feedback Form</title>
    <!-- Include jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
    <form id='fform'>
        <input name='first-name' id='f-name' placeholder='first-name'>
        <input name='last-name' id='l-name' placeholder='last-name'>
        <input name='u-comment' id='u-c' placeholder='comment'>   
        <input type='submit' value='Send Feedback'> <!-- corrected value attribute -->
    </form>

    <script>
        $(document).ready(function() {
            $("#fform").submit(function(e) {
                e.preventDefault(); // Prevent default form submission

                // Collect form data
                var formData = $(this).serialize();

                // Send data to process.php using AJAX
                $.ajax({
                    url: "loprocess.php",
                    type: "POST",
                    data: formData,
                    success: function(response) {
                        // Handle the response (e.g., update UI)
                        console.log(response);
                    },
                    error: function(xhr, status, error) {
                        console.error("AJAX error:", error);
                    }
                });
            });
        });
    </script>
</body>
</html>
