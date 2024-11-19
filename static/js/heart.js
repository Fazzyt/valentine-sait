function createHeart() {
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
        </svg>
    `;

    const size = Math.random() * 20 + 10;
    heart.style.width = `${size}px`;
    heart.style.height = `${size}px`;

    heart.style.left = `${Math.random() * 100}%`;

    const fallDuration = Math.random() * 3 + 2;
    heart.style.transition = `transform ${fallDuration}s linear`;

    document.getElementById('hearts').appendChild(heart);

    requestAnimationFrame(() => {
        heart.style.transform = `translateY(100vh)`;
    });

    setTimeout(() => {
        heart.remove();
    }, fallDuration * 1000);
}

function startHeartfall() {
    const interval = Math.random() * 150 + 50;
    createHeart();
    setTimeout(startHeartfall, interval);
}

function initHeartfall() {
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    if (!isMobile) {
        startHeartfall();
    } else {
        let heartCount = 0;
        function mobileHeartfall() {
            if (heartCount < 20) { // Ограничиваем количество сердец
                createHeart();
                heartCount++;
            }
            setTimeout(mobileHeartfall, Math.random() * 300 + 200);
        }
        mobileHeartfall();
    }
}

initHeartfall();