// JavaScript (script.js)
document.getElementById('produce-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Gather form data
    const formData = new FormData(this);

    // Convert form data to JSON
    const produceData = {};
    formData.forEach((value, key) => {
        produceData[key] = value;
    });

    // Example: send produceData to your backend via AJAX
    // Replace 'your-api-endpoint' with the actual endpoint URL
    fetch('your-api-endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(produceData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Produce added successfully:', data);
        // Optionally, perform any additional actions (e.g., show success message, redirect to another page)
    })
    .catch(error => {
        console.error('Error adding produce:', error);
        // Optionally, handle errors (e.g., display error message to the user)
    });
});
