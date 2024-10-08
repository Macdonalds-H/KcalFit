<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>알림 설정</title>
    <link rel="stylesheet" href="static/css/main.css">
    <link rel="stylesheet" href="static/css/alarm.css">
    <style>
        /* 기존 CSS 스타일 유지 */
        body {
            font-family: 'Noto Sans KR', sans-serif; 
            margin: 0;
            padding: 0;
        }
        /* ... (나머지 스타일 생략) ... */
        .notification-list {
            margin-top: 20px;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 5px;
            background-color: #fff;
        }
        .notification-item {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <!-- 상단 네비게이션 메뉴 추가 -->
    <div id="header">
        <h1 id="logo">KcalFit</h1>
        <ul id="menu">
            <a href="/"><li>홈</li></a>
            <a href="/diet"><li>식단</li></a>
            <a href="/moisture"><li>수분</li></a>
            <a href="/exercise"><li>운동</li></a>
            <a href="/alarm"><li class="onlink">알림</li></a>
            <a href="/mypage"><li>마이페이지</li></a>
        </ul>
    </div>

    <div class="container">
        <div style="float: left; width: 500px;">
            <h1>알림 설정</h1>
            <form id="dietForm" method="POST" action="/alarm">
            <!-- 식단 입력 알림 -->
            <div class="section">
                <h2>식단 입력 알림</h2>
                <label for="meal-frequency">하루에 몇 번 알려드릴까요?</label>
                <div class="inputs-container">
                    <input type="number" id="meal-frequency" name="meal-frequency" min="0" max="10" value="0" oninput="updateTimeInputs('meal')">
                    <span>회</span>
                </div>
                <div id="meal-time-inputs" class="time-inputs"></div>
            </div>
    
            <!-- 물 섭취 알림 -->
            <div class="section">
                <h2>물 섭취 알림</h2>
                <label for="water-frequency">하루에 몇 번 알려드릴까요?</label>
                <div class="inputs-container">
                    <input type="number" id="water-frequency" name="water-frequency" min="0" max="20" value="0" oninput="updateTimeInputs('water')">
                    <span>회</span>
                </div>
                <div id="water-time-inputs" class="time-inputs"></div>
            </div>
    
            <button id="start-button" onclick="startNotifications()">설정 완료</button>
            <div id="alert-message" class="alert" style="display:none;">이미 알림이 설정되었습니다.</div>
            </form>
        </div>
        
        
        <!-- 저장된 알림 목록 표시 -->
        <div class="notification-list" style="float: right; width: 390px;">
            <h2>저장된 알림</h2>
            {% if reminders %}
                {% for reminder in reminders %}
                <div class="notification-list">
                    <div class="notification-item">
                        <div class="notification-details">
                            <span class="notification-title notification-header">식단 알림</span>
                            <span>{{ reminder.diet_count }}회</span>
                        </div>
                        <ul class="notification-times">
                            {% for time in reminder.diet_times %}
                                <li>{{ time }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                
                    <div class="notification-item">
                        <div class="notification-details">
                            <span class="notification-title notification-header">물 섭취 알림</span>
                            <span>{{ reminder.water_count }}회</span>
                        </div>
                        <ul class="notification-times">
                            {% for time in reminder.water_times %}
                                <li>{{ time }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                </div>
                {% endfor %}
            {% else %}
                <p>저장된 알림이 없습니다.</p>
            {% endif %}
        </div>
        
    </div>

    <script>
        // 기존 JavaScript 코드는 그대로 사용
        let mealTimes = [];
        let waterTimes = [];
        let notificationsScheduled = false; // 알림이 시작되었는지 여부

        function updateTimeInputs(type) {
            const frequency = document.getElementById(`${type}-frequency`).value;
            const timeInputsContainer = document.getElementById(`${type}-time-inputs`);

            // 기존 입력 필드 삭제
            timeInputsContainer.innerHTML = '';

            // 새로운 입력 필드를 수량만큼 추가
            for (let i = 1; i <= frequency; i++) {
                const wrapper = document.createElement('div');
                wrapper.classList.add('time-input-wrapper');

                const label = document.createElement('label');
                label.textContent = `${i}번째 알림 시간: `;
                const input = document.createElement('input');
                input.type = 'time';
                input.name = `${type}-time-${i}`;
                input.id = `${type}-time-${i}`;
                wrapper.appendChild(label);
                wrapper.appendChild(input);
                timeInputsContainer.appendChild(wrapper);
            }
        }

        function startNotifications() {
            if (notificationsScheduled) {
                document.getElementById('alert-message').style.display = 'block';
                return; // 이미 알림이 설정된 경우 중복 방지
            }

            mealTimes = getTimeValues('meal');
            waterTimes = getTimeValues('water');

            // 식단 및 물 섭취 알림 예약
            scheduleNotifications(mealTimes, '식단을 입력해주세요.');
            scheduleNotifications(waterTimes, '물을 마실 시간이에요.');

            // 설정 완료 알림
            alert('설정이 완료되었습니다.');
            

            notificationsScheduled = true; // 알림 설정 상태를 true로 변경

            // 페이지 이동을 막기 위해 기본 form 동작을 막음
            return false; // 이 부분이 추가되어 알림 후 페이지 이동이 발생하지 않음
        }

        function getTimeValues(type) {
            const frequency = document.getElementById(`${type}-frequency`).value;
            const times = [];

            for (let i = 1; i <= frequency; i++) {
                const timeValue = document.getElementById(`${type}-time-${i}`).value;
                if (timeValue) {
                    times.push(timeValue);
                }
            }

            return times;
        }

        function scheduleNotifications(times, message) {
            times.forEach(time => {
                const [hours, minutes] = time.split(':');
                const now = new Date();
                const notificationTime = new Date();

                // 알림 시간을 설정
                notificationTime.setHours(hours);
                notificationTime.setMinutes(minutes);
                notificationTime.setSeconds(0);

                // 알림이 이미 지난 경우 다음 날로 설정
                if (notificationTime < now) {
                    notificationTime.setDate(notificationTime.getDate() + 1);
                }

                // 알림 예약
                setTimeout(() => {
                    alert(message);
                }, notificationTime.getTime() - now.getTime());
            });
        }
    </script>
</body>
</html>
