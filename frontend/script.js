function submitData() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    fetch('http://localhost:5000/store', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}
