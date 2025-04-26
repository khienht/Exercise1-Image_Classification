document.getElementById('upload-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData();
    const imageFile = document.getElementById('image-upload').files[0];
    formData.append('image', imageFile);

    try {
        const response = await fetch('https://your-render-app-url.com/predict', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        
        if (response.ok) {
            document.getElementById('prediction').innerText = `Prediction: ${result.label}`;
        } else {
            document.getElementById('prediction').innerText = 'Error: Unable to classify image.';
        }
    } catch (error) {
        document.getElementById('prediction').innerText = 'Error: Could not reach the server.';
        console.error(error);
    }
});

