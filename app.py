from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>馬青煒算命系統</title>
    <style>
        body {
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        #result img {
            max-width: 200px;
            display: block;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h1>馬青煒算命系統</h1>

<form id="myForm">
    <label>1. 姓名：</label><br>
    <input type="text" id="name" required><br><br>

    <label>2. 生日（民國年月日）：</label><br>
    民國 
    <input type="number" id="year" min="1" max="150" style="width:80px;" required> 年
    <input type="number" id="month" min="1" max="12" style="width:60px;" required> 月
    <input type="number" id="day" min="1" max="31" style="width:60px;" required> 日
    <br><br>

    <label>3. 性別：</label><br>
    <input type="radio" name="gender" value="男" required> 男
    <input type="radio" name="gender" value="女"> 女
    <br><br>

    <label>4. 選擇算命方法：</label><br>
    <input type="radio" name="fortuneType" value="六爻卜卦" required> 六爻卜卦<br>
    <input type="radio" name="fortuneType" value="塔羅占卜"> 塔羅占卜<br>
    <input type="radio" name="fortuneType" value="八字命盤"> 八字命盤<br><br>

    <button type="submit">開始算命</button>
</form>

<hr>

<h2>個人資料：</h2>
<div id="result"></div>

<script>
document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const year = document.getElementById("year").value;
    const month = document.getElementById("month").value;
    const day = document.getElementById("day").value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const fortuneType = document.querySelector('input[name="fortuneType"]:checked').value;

    let fortuneResult = "";

    if (fortuneType === "六爻卜卦") {
        fortuneResult = "蒙卦：容易被騙或被帶風向";
    } 
    else if (fortuneType === "塔羅占卜") {
        fortuneResult = "寶劍七：生活中總是疏忽大意";
    } 
    else if (fortuneType === "八字命盤") {
        fortuneResult = "財星弱，比劫旺：容易被熟人詐騙";
    }

    document.getElementById("result").innerHTML = `
        <p><strong>姓名：</strong>${name}</p>
        <p><strong>生日：</strong>民國 ${year} 年 ${month} 月 ${day} 日</p>
        <p><strong>性別：</strong>${gender}</p>
        <p><strong>算命方式：</strong>${fortuneType}</p>
        <hr>
        <p><strong>算命結果：</strong>${fortuneResult}</p>
        <br>
        <p style="color:red; font-weight:bold;">
            恭喜你被社交工程詐騙了，下次要注意，不要被騙個資了，就算是朋友也不可以輕易相信！！！<br><br>
            P.S.社交工程詐騙利用心理操控誘使受害者洩露個資或密碼，常透過電話、訊息或網路假冒信任對象，目的是盜取金錢或敏感資料<br><br>
            還有不要透漏這裡面的內容，不然我的專題表單會沒人填<br><br>
            雖然被我社交工程詐騙了，但是請幫我填一下表單：
        </p>
        <p>
            🔗 <a href="https://docs.google.com/forms/d/e/1FAIpQLSfbtuWhQHNon5524qm1lpMOXbyj06knxGAWsCAhy6Og6tSNCg/viewform?usp=dialog" target="_blank">點我填寫 Google 表單</a>
        </p>
    `;
});
</script>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 如果您想要處理 POST 數據，可以在這裡添加
        pass
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)