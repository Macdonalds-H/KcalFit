<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>운동 기록 설정</title>
    <link rel="stylesheet" href="static/css/main.css">
    <link rel="stylesheet" href="static/css/dayExer.css">
</head>
<body>
    <div id="header">
        <h1 id="logo">KcalFit</h1>
        <ul id="menu">
            <a href="/"><li>홈</li></a>
            <a href="/diet"><li>식단</li></a>
            <a href="/moisture"><li>수분</li></a>
            <a href="/exercise"><li class="onlink">운동</li></a>
            <a href="/alarm"><li>알림</li></a>
            <a href="/mypage"><li>마이페이지</li></a>
        </ul>
    </div>
    <div id="container">
        <div class="header">
            <h1>운동 기록 설정 화면</h1>
        </div>
        <div class="main-content">
            <div class="calendar">
                <h2>10월</h2>
                <table>
                    <thead>
                        <tr>
                            <th>일</th>
                            <th>월</th>
                            <th>화</th>
                            <th>수</th>
                            <th>목</th>
                            <th>금</th>
                            <th>토</th>
                        </tr>
                    </thead>
                    <tbody id="calendar-body">
                        <!-- 날짜가 여기에 생성됩니다 -->
                    </tbody>
                </table>
            </div>
            
            <div class="settings">
                <form action="/save_exercise" method="POST">
                    <input type="hidden" name="selected_date" id="selected_date"> 
                    <label for="intensity">일일 운동강도</label>
                    <select id="intensity" name="intensity">
                        <option value="" disabled selected>선택</option>
                        <option value="low">저강도</option>
                        <option value="medium">중강도</option>
                        <option value="high">고강도</option>
                    </select>
                    <p id="intensityDescription" class="description"></p>
                    
                    <label for="time">일일 운동시간</label>
                    <input type="number" name="hours" id="hours" min="0" max="23" value="0"> 시간 : 
                    <input type="number" name="minutes" id="minutes" min="0" max="59" value="0"> 분

                    <button id="saveButton" type="submit" class="save-btn">저장하기</button>
                </form>
            </div>
        </div>
    </div>

    <script>
    const today = new Date();
    const currentMonth = today.getMonth();
    const currentYear = today.getFullYear();

    let workoutData = {}; // 날짜별 운동 기록을 저장할 객체
    let selectedDate = null; // 선택된 날짜 저장

    function fetchExerciseData() {
        fetch('/get_exercise_data')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    workoutData = {};
                    data.forEach(entry => {
                        // 날짜 문자열을 Date 객체로 변환
                        const dateObj = new Date(entry.date);
                        // 'YYYY-MM-DD' 형식으로 변환
                        const dateKey = dateObj.toISOString().slice(0, 10);
                        workoutData[dateKey] = {
                            intensity: entry.intensity,
                            time: entry.duration
                        };
                    });
                    generateCalendar(currentMonth, currentYear);
                }
            })
            .catch(error => {
                console.error('Error fetching exercise data:', error);
            });
    }


    function generateCalendar(month, year) {
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const calendarBody = document.getElementById('calendar-body');
    calendarBody.innerHTML = '';

    let date = 1;
    for (let i = 0; i < 6; i++) {
        const row = document.createElement('tr');

        for (let j = 0; j < 7; j++) {
            const cell = document.createElement('td');
            if (i === 0 && j < firstDay) {
                cell.innerHTML = '';
            } else if (date > daysInMonth) {
                break;
            } else {
                const dateKey = `${year}-${String(month + 1).padStart(2, '0')}-${String(date).padStart(2, '0')}`;
                cell.innerHTML = `<span>${date}</span><div class="workout-entry"></div>`;

                // DB에서 운동 기록이 있는 날짜면 해당 내용을 표시
                if (workoutData[dateKey]) {
                    const workoutEntry = workoutData[dateKey];
                    const workoutText = `${workoutEntry.intensity}, ${workoutEntry.time}`;
                    const workoutCell = cell.querySelector('.workout-entry');
                    workoutCell.textContent = workoutText;

                    // 운동 강도에 따라 색상 추가
                    workoutCell.classList.add(`${workoutEntry.intensity}-intensity`);
                }

                // 날짜 선택 이벤트 추가
                cell.addEventListener('click', function() {
                    selectedDate = dateKey;
                    alert(`${selectedDate} 날짜가 선택되었습니다.`);
                });
                date++;
            }
            row.appendChild(cell);
        }
        calendarBody.appendChild(row);
    }
}


    // 페이지 로드 시 현재 달의 캘린더와 DB 운동 기록을 로드
    fetchExerciseData();

    // 운동 기록 저장 함수
    document.getElementById('saveButton').addEventListener('click', function() {
        if (!selectedDate) {
            alert("먼저 날짜를 선택하세요.");
            return;
        }
        document.getElementById('selected_date').value = selectedDate; 

        const intensity = document.getElementById('intensity').value;
        const hours = document.getElementById('hours').value;
        const minutes = document.getElementById('minutes').value;

        if (intensity === "") {
            alert("운동 강도를 선택하세요.");
            return;
        }

        const workoutEntry = `${intensity}강도, ${hours}시간 ${minutes}분`;
        const workoutCell = document.getElementById(selectedDate);
        workoutCell.textContent = workoutEntry;

        workoutCell.classList.remove('low-intensity', 'medium-intensity', 'high-intensity');
        workoutCell.classList.add(`${intensity}-intensity`);

        workoutData[selectedDate] = {
            intensity: intensity,
            time: `${hours}시간 ${minutes}분`
        };

        alert(`${selectedDate} 날짜에 ${workoutEntry} 운동이 기록되었습니다.`);
    });

    // 강도 설명 업데이트
    document.getElementById('intensity').addEventListener('change', function() {
        const intensity = this.value;
        const descriptionElement = document.getElementById('intensityDescription');
        
        let description = '';
        
        if (intensity === 'low') {
            description = '땀이 많이 나지 않는 정도의 가벼운 운동, ex: 걷기, 요가';
        } else if (intensity === 'medium') {
            description = '호흡이 짧아지고 10분 정도 운동 후 땀이 나는 정도, ex: 자전거 타기';
        } else if (intensity === 'high') {
            description = '호흡이 깊고 빨라지며 짧은 시간 운동 후 땀이 날 정도, 대화하기 힘든 정도, ex: 스쿼트, 무산소 플랭크';
        }
        
        descriptionElement.textContent = description;
    });

    window.onload = function() {
        generateCalendar(currentMonth, currentYear);
    };
    </script>
</body>
</html>
