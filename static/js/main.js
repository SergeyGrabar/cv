document.addEventListener("mousemove", function(e) {
    const follower = document.getElementById("follower");
    const x = e.clientX - 10; // Вычитаем половину ширины кружка для центрирования
    const y = e.clientY - 10; // Вычитаем половину высоты кружка для центрирования
    follower.style.left = x + "px";
    follower.style.top = y + "px";
});

const links = document.querySelectorAll(".hover-link");

links.forEach(function(link) {
    link.addEventListener("mouseover", function() {
        const circle = document.getElementById("follower");
        circle.style.transform = "scale(5)"; // Увеличение размера кружка
    });

    link.addEventListener("mouseout", function() {
        const circle = document.getElementById("follower");
        circle.style.transform = "scale(1)"; // Возврат к обычному размеру
    });
});

const squares = document.querySelectorAll(".logo");
const mainDiv = document.querySelector(".main-div");
const mainDivWidth = mainDiv.clientWidth;
const mainDivHeight = mainDiv.clientHeight;

function animateSquares() {
    squares.forEach((square, index) => {
        let x = Math.random() * (mainDivWidth - square.clientWidth);
        let y = Math.random() * (mainDivHeight - square.clientHeight);
        let rotation = Math.random() * 360;
        square.style.transform = `translate(${x}px, ${y}px) rotate(${rotation}deg)`;
    });
}

animateSquares(); // Запуск анимации при загрузке страницы
setInterval(animateSquares, 5000); // Запуск анимации каждые 5 секунд