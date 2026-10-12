from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AgroLingo AI</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #eef7e9;
    color: #183b20;
    margin: 0;
    padding: 20px;
}
.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 4px 15px #0002;
}
h1 { color: #18733b; }
label { display: block; margin-top: 18px; font-weight: bold; }
select, button {
    width: 100%;
    padding: 13px;
    margin-top: 8px;
    border-radius: 8px;
    font-size: 16px;
}
select { border: 1px solid #aaa; }
button {
    background: #18733b;
    color: white;
    border: none;
    cursor: pointer;
}
.result {
    margin-top: 20px;
    padding: 15px;
    background: #e4f5df;
    border-radius: 10px;
    line-height: 1.6;
}
footer { margin-top: 20px; font-size: 12px; color: #555; }
</style>
</head>
<body>
<div class="container">
<h1>🌱 AgroLingo AI</h1>
<p>Your crop-health learning assistant for farmers.</p>
<form method="POST">
<label for="crop">Select your crop</label>
<select name="crop" id="crop">
<option>Maize</option>
<option>Wheat</option>
<option>Teff</option>
<option>Sorghum</option>
</select>

<label for="symptom">What symptom do you see?</label>
<select name="symptom" id="symptom">
<option value="yellow">Yellow leaves</option>
<option value="spots">Brown or dark spots</option>
<option value="wilting">Wilting or drooping</option>
<option value="stunted">Slow or stunted growth</option>
</select>

<button type="submit">Get Guidance 🌿</button>
</form>

{% if result %}
<div class="result">
<h3>🌾 General guidance</h3>
<p><b>Crop:</b> {{ crop }}</p>
<p>{{ result }}</p>
</div>
{% endif %}

<footer>
Educational prototype only. Symptoms can have several causes.
Confirm serious crop problems with a local agricultural expert.
</footer>
</div>
</body>
</html>
"""

GUIDANCE = {
    "yellow": "Yellow leaves may result from nutrient deficiency, water problems, pests, or disease. Check soil moisture and inspect several plants before deciding on treatment.",
    "spots": "Spots may be associated with fungal or bacterial disease, pests, or environmental damage. Photograph the affected leaves and ask a local agricultural extension worker for identification.",
    "wilting": "Wilting may be caused by insufficient water, waterlogged soil, damaged roots, or disease. Check soil moisture and drainage before watering more.",
    "stunted": "Slow growth can be associated with poor soil fertility, weeds, unsuitable moisture, pests, or disease. Compare healthy and affected plants and inspect the field."
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    crop = "Maize"

    if request.method == "POST":
        crop = request.form.get("crop", "Maize")
        symptom = request.form.get("symptom", "yellow")
        result = GUIDANCE.get(symptom, GUIDANCE["yellow"])

    return render_template_string(
        HTML, result=result, crop=crop
    )

if __name__ == "__main__":
    app.run(debug=True)