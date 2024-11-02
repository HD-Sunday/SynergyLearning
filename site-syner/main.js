// Массив изображений
let imagesArray;
imagesArray = [
    'img/img1.jpg',
    'img/img2.jpeg',
    'img/img3.jpg',
    'img/img4.jpg',
    'img/img5.jpg'
];

// Текущий индекс изображения
let currentIndex = 0;

// Функция для изменения изображения при нажатии на кнопку "вперед"
const forward = () => {
    currentIndex++;
    if (currentIndex === imagesArray.length) {
        currentIndex = 0;
    }
    updateImage(currentIndex);
};

// Функция для изменения изображения при нажатии на кнопку "назад"
const backward = () => {
    currentIndex--;
    if (currentIndex < 0) {
        currentIndex = imagesArray.length - 1;
    }
    updateImage(currentIndex);
};

// Функция для обновления изображения
const updateImage = (index) => {
    const images = document.querySelector('.slider-images');
    images.innerHTML = '';
    images.appendChild(document.createElement('img'));
    images.querySelector('img').src = imagesArray[index];
    const currentImage = document.querySelector('.current-image');
    currentImage.textContent = `Изображение ${index + 1} из ${imagesArray.length}`;
};

// Привязка событий к кнопкам
const forwardBtn = document.querySelector('.btn-forward');
forwardBtn.addEventListener('click', forward);
const backwardBtn = document.querySelector('.btn-backward');
backwardBtn.addEventListener('click', backward);

// Инициализация слайдера
updateImage(currentIndex);