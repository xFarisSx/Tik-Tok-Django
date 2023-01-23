const loginLink = document.getElementById("loginLink");
const registerLink = document.getElementById("registerLink");

const links = [loginLink, registerLink];

loginLink.addEventListener("mousemove", (e) => {
    loginLink.style.color = `#fff`;
    loginLink.style.backgroundColor = `rgb(226, 33, 71)`;
    registerLink.style.color = `rgb(226, 33, 71)`;
    registerLink.style.backgroundColor = `#fff`;
});
loginLink.addEventListener("mouseleave", (e) => {
    loginLink.style.color = `rgb(226, 33, 71)`;
    loginLink.style.backgroundColor = `#fff`;
    registerLink.style.color = `#fff`;
    registerLink.style.backgroundColor = `rgb(226, 33, 71)`;
});

registerLink.addEventListener("mouseenter", (e) => {
    registerLink.style.color = `rgb(226, 33, 71)`;
    registerLink.style.backgroundColor = `#fff`;
    loginLink.style.color = `#fff`;
    loginLink.style.backgroundColor = `rgb(226, 33, 71)`;
});
registerLink.addEventListener("mouseleave", (e) => {
    loginLink.style.color = `rgb(226, 33, 71)`;
    loginLink.style.backgroundColor = `#fff`;
    registerLink.style.color = `#fff`;
    registerLink.style.backgroundColor = `rgb(226, 33, 71)`;
});
