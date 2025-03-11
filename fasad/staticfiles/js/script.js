// Инициализация слайдера
const swiper = new Swiper('.swiper', {
    // Основные параметры
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    
    // Пагинация
    pagination: {
        el: '.swiper-pagination',
        clickable: true
    },
    
    // Навигационные кнопки
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    
    // Автопрокрутка
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    
    // Эффект перехода
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
    
    // Клавиатура
    keyboard: {
        enabled: true,
        onlyInViewport: false,
    },
});
