document.addEventListener("DOMContentLoaded", () => {
  const openIcon = document.querySelector("#openIcon");
  const closeIcon = document.querySelector("#closeIcon");
  const nav = document.querySelector("nav");

  openIcon.onclick = () => {
    nav.style.display = "flex";
    closeIcon.style.display = "block";
    openIcon.style.display = "none";
  };

  closeIcon.onclick = () => {
    openIcon.style.display = "block";
    nav.style.display = "none";
    closeIcon.style.display = "none";
  };
});
