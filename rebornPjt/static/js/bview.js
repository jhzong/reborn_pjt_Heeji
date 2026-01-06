// 답글 입력창 켜고 끄기
function toggleReply(commentId) {
    const form = document.getElementById(`reply-form-${commentId}`);
    if (form) {
        form.style.display = form.style.display === 'none' ? 'block' : 'none';
    }
}

// 게시글 본문 수정창 켜고 끄기
function togglePostEdit() {
    const display = document.getElementById('post-display');
    const form = document.getElementById('post-edit-form');
    const headerTitle = document.querySelector('.view-header h1'); // 제목 숨기기용 (선택사항)

    if (form.style.display === 'none') {
        form.style.display = 'block';
        display.style.display = 'none';
        if(headerTitle) headerTitle.style.opacity = '0.3'; // 수정 중임을 표시
    } else {
        form.style.display = 'none';
        display.style.display = 'block';
        if(headerTitle) headerTitle.style.opacity = '1';
    }
}

// 2. 댓글 및 답글 수정 토글
function toggleEdit(commentId) {
    const contentP = document.getElementById(`content-${commentId}`);
    const editForm = document.getElementById(`edit-form-${commentId}`);

    if (editForm.style.display === 'none') {
        contentP.style.display = 'none';
        editForm.style.display = 'block';
    } else {
        contentP.style.display = 'block';
        editForm.style.display = 'none';
    }
}

