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

// Обработка отправки формы
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const modal = document.getElementById('successModal');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(form);
            
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showSuccessModal();
                    form.reset();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Даже в случае ошибки показываем модальное окно
                showSuccessModal();
                form.reset();
            });
        });
    }
});

// Функции для работы с модальным окном
function showSuccessModal() {
    const modal = document.getElementById('successModal');
    modal.classList.add('show');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('successModal');
    modal.classList.remove('show');
    document.body.style.overflow = '';
}

// Закрытие модального окна при клике вне его
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('successModal');
    const modalContent = modal.querySelector('.modal-content');
    
    modal.addEventListener('click', function(e) {
        if (e.target === this) {
            closeModal();
        }
    });
    
    // Предотвращение закрытия при клике на содержимое модального окна
    modalContent.addEventListener('click', function(e) {
        e.stopPropagation();
    });
    
    // Закрытие по клавише Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeModal();
        }
    });
});
