const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('showw');
        } else {
            entry.target.classList.remove('showw');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hiddden');
hiddenElements.forEach((el) => observer.observe(el));
