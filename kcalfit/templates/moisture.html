<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수분 섭취량 기록</title>
    <link rel="stylesheet" href="static/css/main.css">
    <link rel="stylesheet" href="/static/css/moisture.css">
</head>
<body>
    <div id="header">
        <h1 id="logo">KcalFit</h1>
        <ul id="menu">
            <a href="/"><li>홈</li></a>
            <a href="/diet"><li>식단</li></a>
            <a href="/moisture"><li class="onlink">수분</li></a>
            <a href="/exercise"><li>운동</li></a>
            <a href="/alarm"><li>알림</li></a>
            <a href="/mypage"><li>마이페이지</li></a>
        </ul>
    </div>
    <div id="container">
        <div style="padding-top: 120px;width: 40%;">
            <!-- 수분 섭취 진행 바 -->
            <div class="intake-progress-container">
                <div class="intake-progress">
                    <div class="progress-header">
                        <span> 일일 수분 섭취량 </span>
                        <span class="goal"> 목표: <span id="api_goal"></span></span><button onclick="get_moisture_goal()">목표 불러오기</button>
                    </div>
            
                    <!-- 수분 섭취량에 따라 진행 바가 변동 -->
                    <progress value="{{ current_intake }}" max="{{ target_intake }}" class="progress-bar"></progress>
                    <div class="progress-text">
                        {{ current_intake }} ml / <span id="api_goal2"></span>
                    </div>
                </div>
            </div>
            
            <!-- 섭취량 입력 폼 -->
            <div class="intake-input-container">
                <form action="/save_moisture" method="post">
                    <label for="intake"> 섭취량 입력 (ml): </label>
                    <input type="hidden" name="go_intake" value="30">
                    <input type="number" id="intake" name="target_intake" min="0"  required>
                    <button type="submit">저장</button>
                </form>
            </div>
        </div>
        <!-- 달력 -->
        <div class="calendar-container">

            <h2>{{ today.year }}년 {{ today.month }}월 달력</h2>
            <div class="table-wrapper">
                <table border="1">
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
                    <tbody>
                        {% for week in month_days %}
                            <tr>
                                {% for day in week %}
                                    {% if day == 0 %}
                                        <td></td> <!-- 빈 칸 -->
                                    {% else %}
                                        {% set date_str = today.replace(day=day).strftime('%Y-%m-%d') %}
                                        {% set intake = hydration_data.get(date_str, 0) %}
                                        <td>
                                            <strong>{{ day }}</strong><br>
                                            섭취량: {{ intake }}ml
                                        </td>
                                    {% endif %}
                                {% endfor %}
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
    function get_moisture_goal(){
        axios.post('/get_moisture_goal')
        .then(function(response) {
            console.log(response)
            const goal = document.getElementById("api_goal");
            const goal2 = document.getElementById("api_goal2");
            const rp = response.data.moisture_goal;
            goal.innerHTML = rp;
            goal2.innerHTML = rp;
        })
        .catch(function(error) {
            console.error(error);
            document.getElementById('loading').style.display = 'none';
            document.getElementById('diet-plan').innerHTML = 'Failed to load diet plan.';
        });
    }
    </script>


    

</body>



</html>