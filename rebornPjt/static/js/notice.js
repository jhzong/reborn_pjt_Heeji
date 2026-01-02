document.addEventListener('DOMContentLoaded', () => {
    console.log("게시판 스크립트 로드 완료");
    
    // 검색 버튼 클릭 이벤트 예시
    const searchBtn = document.querySelector('.search-box button');
    searchBtn.addEventListener('click', () => {
        const query = document.querySelector('.search-box input').value;
        if(query) alert(`'${query}' 검색 결과로 이동합니다.`);
    });
});