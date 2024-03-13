const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});


// This is just a placeholder for the user data.
var userData = {
    age: 30,
    gender: 'Male',
    a1c: 5.7,
    weight: 70
    // can add more properties here for other user details
};

document.getElementById('age').textContent = userData.age;
document.getElementById('gender').textContent = userData.gender;
document.getElementById('a1c').textContent = userData.a1c;
document.getElementById('weight').textContent = userData.weight;
// Can add more lines here for other user details
