const loginLink = document.getElementById("loginLink");
const registerLink = document.getElementById("registerLink");
const videos = document.querySelectorAll('video')
const links = [loginLink, registerLink];
if (loginLink){
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
}


function togglePlay(video) {
    if (video.paused || video.ended) {
      video.play();
    } else {
      video.pause();
    }
  }

for (let video of videos){
    video.addEventListener('click', (e)=> {
        togglePlay(e.target)
    })
}

document.querySelector('.followed').textContent = 'Unfollow'