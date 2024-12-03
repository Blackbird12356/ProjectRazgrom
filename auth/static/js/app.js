const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            // Добавляем класс "showw", если элемент виден
            entry.target.classList.add('showw');

            // Прекращаем наблюдение за этим элементом, так как он уже видим
            observer.unobserve(entry.target);
        }
    });
});

// Находим все скрытые элементы
const hiddenElements = document.querySelectorAll('.hiddden');
hiddenElements.forEach((el) => observer.observe(el));

// Функция проверки, достигнут ли конец страницы
const checkScrollEnd = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight;
    const clientHeight = document.documentElement.clientHeight;

    if (scrollTop + clientHeight >= scrollHeight) {
        // Останавливаем наблюдение за всеми элементами
        observer.disconnect();
        console.log("Достигнут конец страницы. Наблюдение остановлено.");
    }
};

// Добавляем обработчик события прокрутки
window.addEventListener('scroll', checkScrollEnd);


