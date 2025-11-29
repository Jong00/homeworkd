// DOM이 다 로드된 뒤에 실행
document.addEventListener("DOMContentLoaded", function () {
  console.log("JS 로딩 완료!");

  // 예: 로그인 버튼 클릭 이벤트
  const loginBtn = document.getElementById("loginBtn");
  if (loginBtn) {
    loginBtn.addEventListener("click", function () {
      alert("로그인 버튼 클릭됨!");
      // 여기에 원하는 로직 추가
    });
  }

  // 예: 메뉴 토글
  const menuToggle = document.getElementById("menuToggle");
  const nav = document.querySelector(".nav");
  if (menuToggle && nav) {
    menuToggle.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
  }
});
