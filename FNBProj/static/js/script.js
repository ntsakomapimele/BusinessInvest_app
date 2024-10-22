// Simple in-memory user storage for demonstration
const users = {};

// Handle user registration
document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const businessName = document.getElementById('businessName').value;
    const businessType = document.getElementById('businessType').value;
    const businessDescription = document.getElementById('businessDescription').value;

    // Simple validation
    if (!email || !password || !businessName || !businessType || !businessDescription) {
        alert('Please fill in all fields.');
        return;
    }

    // Store user data (in a real app, you would send this to your server)
    users[email] = { password, businessName, businessType, businessDescription };
    alert('Registration successful!');

    // Close the modal
    const registerModal = bootstrap.Modal.getInstance(document.getElementById('registerModal'));
    registerModal.hide();
});

// Handle user login
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    // Validate login
    if (users[email] && users[email].password === password) {
        alert(`Welcome back, ${users[email].businessName}!`);
        document.getElementById('loginForm').reset();
        document.querySelector('.login-container').style.display = 'none';
        document.getElementById('dashboard').style.display = 'block';
        document.getElementById('welcomeMessage').innerText = `Hello, ${users[email].businessName}`;
    } else {
        alert('Invalid email or password.');
    }
});
 // JavaScript to show/hide fields based on user selection
        document.getElementById('userType').addEventListener('change', function() {
            const userType = this.value;
            const businessOwnerFields = document.querySelector('.business-owner-fields');
            const investorFields = document.querySelector('.investor-fields');
            
            if (userType === 'Business Owner') {
                businessOwnerFields.style.display = 'block';
                investorFields.style.display = 'none';
            } else if (userType === 'Investor') {
                businessOwnerFields.style.display = 'none';
                investorFields.style.display = 'block';
            }
        });


        document.addEventListener('DOMContentLoaded', function() {
            const userTypeSelect = document.getElementById('userType');
            const businessOwnerFields = document.querySelector('.business-owner-fields');
            const investorFields = document.querySelector('.investor-fields');
        
            // Event listener for user type select
            userTypeSelect.addEventListener('change', function() {
                const userType = userTypeSelect.value;
        
                // Show/Hide fields based on user type selection
                if (userType === 'Business Owner') {
                    businessOwnerFields.style.display = 'block';
                    investorFields.style.display = 'none';
                } else if (userType === 'Investor') {
                    businessOwnerFields.style.display = 'none';
                    investorFields.style.display = 'block';
                } else {
                    businessOwnerFields.style.display = 'none';
                    investorFields.style.display = 'none';
                }
            });
        });
        