(() => {
  const script = document.currentScript;
  const lessons = (script?.dataset.lessons || document.body.dataset.quizLessons || '')
    .split(',').map(value => value.trim()).filter(Boolean);
  if (!lessons.length) return;

  const names = {
    '03-01':'TF 발행','03-02':'Child frame','03-03':'TF Listener',
    '03-04':'RViz 시각화','03-05':'Domain ID','03-06':'다중 Domain 제어',
    '03-07':'Domain Bridge','03-08':'Description','03-09':'Gazebo',
    '03-10':'SLAM','03-11':'Localization','03-12':'PID Navigation',
    '03-13':'Navigation','03-14':'Python Nav2','03-15':'Nav2 설정',
    '04-01':'PinkyPro 소개','04-02':'환경 설정','04-03':'맵 작성',
    '04-04':'Nav2 주행','04-05':'Jupyter 내비게이션','04-06':'LCD',
    '04-07':'LCD·LED ROS 2 제어','05-00':'GPU·CUDA·cuDNN 설정'
  };
  const box = document.createElement('section');
  box.className = 'lesson-quiz-cta';
  box.innerHTML = `
    <div><small>LESSON CHECK</small><h2>이 강의, 문제로 확인하기</h2>
    <p>방금 학습한 핵심 개념·수식·코드·오류 진단 문제를 풀어보세요.</p></div>
    <div class="lesson-quiz-links">${lessons.map(id =>
      `<a href="../quiz.html?lesson=${id}&v=c4965b7">${id} · ${names[id]} 10문제 풀기 →</a>`
    ).join('')}</div>`;
  const style = document.createElement('style');
  style.textContent = `.lesson-quiz-cta{width:min(1100px,calc(100% - 32px));margin:36px auto 64px;padding:28px;display:flex;justify-content:space-between;align-items:center;gap:24px;border:1px solid #b89cff;border-radius:18px;background:linear-gradient(135deg,#f5f0ff,#fff)}.lesson-quiz-cta small{color:#7048e8;font-weight:900;letter-spacing:.12em}.lesson-quiz-cta h2{margin:7px 0}.lesson-quiz-cta p{margin:0;color:#586174}.lesson-quiz-links{display:flex;flex-direction:column;gap:9px;flex:none}.lesson-quiz-links a{display:block;padding:13px 17px;border-radius:11px;background:#7048e8;color:#fff!important;text-decoration:none;font-weight:850}.lesson-quiz-links a:hover{background:#5734c7}@media(max-width:700px){.lesson-quiz-cta{align-items:stretch;flex-direction:column}.lesson-quiz-links{width:100%}}`;
  document.head.appendChild(style);
  (document.querySelector('main') || document.body).appendChild(box);
})();
