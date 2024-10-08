<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KcalFit</title>
    <link rel="stylesheet" href="static/css/main.css">
    <style>
         #container {
            display: flex;
            justify-content: space-between;
            margin: 30px auto;
            width: 90%;
            max-width: 1200px;
        }

        /* 달력 스타일 */
        #calendar {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 15px;
            flex: 2;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        .day {
            border: 1px solid #e1e1e1;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            transition: background-color 0.2s ease, transform 0.2s ease;
        }

        .day:hover {
            background-color: #f0f0f0;
            transform: translateY(-5px);
        }

        .day.has-data {
            border: 1px solid #b99bff;
        }

        .meal-indicator {
            width: 55px;
            height: 23px;
            border-radius: 5px;
            margin-top: 10px;
        }

        .meal-indicator.active {
            background-color: #ffd1e6;
        }

        .meal-indicator.inactive {
            background-color: #ececec;
        }

        /* 입력 폼 스타일 */
        #dietForm {
            flex: 1;
            background-color: #fff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        #dietForm h2 {
            margin-top: 0;
            font-size: 24px;
            color: #007bff;
        }

        label {
            font-size: 16px;
            margin-bottom: 8px;
            display: block;
        }

        input[type="text"],
        select,
        textarea {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin-top: 8px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            background-color: #f9f9f9;
        }

        textarea {
            resize: vertical;
        }

        button {
            width: 100%;
            padding: 12px;
            font-size: 18px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.2s ease;
        }

        button:hover {
            background-color: #0056b3;
        }

        /* 반응형 디자인 */
        @media (max-width: 768px) {
            #container {
                flex-direction: column;
                align-items: center;
            }

            #calendar, #dietForm {
                width: 100%;
                margin-bottom: 20px;
            }
        }

        /* 모바일 화면용 스타일 */
        @media (max-width: 480px) {
            #logo {
                font-size: 28px;
            }

            #menu a {
                font-size: 16px;
            }

            .day {
                padding: 15px;
            }

            .meal-indicator {
                width: 15px;
                height: 15px;
            }

            button {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div id="header">
        <h1 id="logo">KcalFit</h1>
        <ul id="menu">
            <a href="/"><li>홈</li></a>
            <a href="/diet"><li class="onlink">식단</li></a>
            <a href="/moisture"><li>수분</li></a>
            <a href="/exercise"><li>운동</li></a>
            <a href="/alarm"><li>알림</li></a>
            <a href="/mypage"><li>마이페이지</li></a>
        </ul>
    </div>
    <div id="container">
        
        <div id="calendar">
            <!-- 달력이 생성될 자리 -->
        </div>
        <form id="dietForm" method="POST" action="/save_diet">
            <h2>10월 식단 입력</h2><br>
            <label for="date">날짜:</label>
            <input type="text" id="date" name="date" readonly><br>

            <label for="meal_type">식사 타입:</label>
            <select id="meal_type" name="meal_type">
                <option value="아침">아침</option>
                <option value="점심">점심</option>
                <option value="저녁">저녁</option>
            </select><br>

            <label for="meal_content">식단 내용:</label><br>
            <textarea id="meal_content" name="meal_content" rows="4" cols="50"></textarea><br>

            <button type="submit">저장하기</button>
        </form>
    </div>
    <script>
        // JavaScript 부분은 변경되지 않음
        function createCalendar(dietData) {
            const calendar = document.getElementById('calendar');
            const year = 2024;
            const month = 9; // 10월 (0부터 시작)
            const lastDay = new Date(year, month + 1, 0).getDate(); // 10월 마지막 날

            for (let day = 1; day <= lastDay; day++) {
                const dayElement = document.createElement('div');
                dayElement.classList.add('day', 'calendar-day');
                const d = document.createElement('span');
                d.setAttribute("class", day);
                d.innerHTML = day;
                dayElement.appendChild(d);

                const dateString = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;

                // 식단이 있는 날짜일 경우 표시
                if (dietData[dateString]) {
                    dayElement.classList.add('has-data');

                    // 각 meal_type에 따라 div를 생성하고 표시
                    ['아침', '점심', '저녁'].forEach(mealType => {
                        const mealDiv = document.createElement('div');
                        mealDiv.classList.add('meal-indicator', mealType);

                        // 식단이 있는 경우 표시, 없으면 비활성 상태로 유지
                        if (dietData[dateString][mealType]) {
                            mealDiv.classList.add('active');
                            mealDiv.title = `${mealType}: ${dietData[dateString][mealType]}`;
                        } else {
                            mealDiv.classList.add('inactive');
                        }
                        mealDiv.innerHTML = `${mealType}`;
                        dayElement.appendChild(mealDiv);
                    });
                }

                // 날짜 클릭 시 새 식단을 추가하거나 수정할 수 있도록 설정
                dayElement.onclick = function() {
                    selectDate(dateString, dietData);
                };

                calendar.appendChild(dayElement);
            }
        }

        document.addEventListener('click', function(e) {
            // 클릭된 요소가 'meal-indicator' 클래스를 가진 경우 처리
            if (e.target.classList.contains('meal-indicator')) {
                const mealElement = e.target;
                const dayElement = mealElement.closest('.calendar-day'); // 날짜 요소를 가져옴
                const date = dayElement.querySelector('span').innerText; // 날짜를 가져옴 (예: 1, 2, 3...)

                const mealType = mealElement.classList[1]; // 아침, 점심, 저녁 중 하나
                const mealContent = mealElement.getAttribute('title') ? mealElement.getAttribute('title').split(': ')[1] : '';

                // 날짜를 폼에 설정
                document.getElementById('date').value = `2024-10-${date.padStart(2, '0')}`; // '2024-10-' + '01' 형식으로 설정

                // 식사 타입을 폼에 설정
                document.getElementById('meal_type').value = mealType;

                // 식단 내용을 폼에 설정
                document.getElementById('meal_content').value = mealContent;

                console.log(`Clicked meal: ${mealType}, Date: ${date}, Content: ${mealContent}`);
            }
        });

        // 특정 meal_type(아침, 점심, 저녁)을 선택했을 때 해당 데이터를 폼에 로드
        function selectMeal(date, mealType, mealContent) {
            const dateInput = document.getElementById('date');
            const mealTypeInput = document.getElementById('meal_type');
            const mealContentInput = document.getElementById('meal_content');

            // 선택한 날짜와 식사 타입을 폼에 채움
            dateInput.value = date;
            mealTypeInput.value = mealType;
            mealContentInput.value = mealContent;
        }

        // 날짜 선택 시 실행되는 함수
        function selectDate(date, dietData) {
            const dateInput = document.getElementById('date');
            dateInput.value = date;

            const mealType = document.getElementById('meal_type');
            const mealContent = document.getElementById('meal_content');

            // 해당 날짜에 저장된 식단이 있을 경우 폼에 채움
            if (dietData[date]) {
                const currentMealType = mealType.value;  // 사용자가 선택한 식사 타입
                mealContent.value = dietData[date][currentMealType] || ''; // 식사 타입에 따른 식단 내용
            } else {
                // 저장된 식단이 없는 경우 빈 폼 제공
                mealContent.value = '';
            }
            
            // 새로운 식단을 추가할 때를 대비해 form reset 상태도 준비
            mealContent.value = '';
        }

        // 페이지 로드 시 달력과 DB 데이터를 불러옴
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/get_diet_data')
                .then(response => response.json())
                .then(data => {
                    createCalendar(data);
                });
        });
    </script>
    
</body>
</html>
