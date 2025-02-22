from flask import Flask, request, render_template
from aisuite import AISuite
import config

app = Flask(__name__)
aisuite = AISuite()

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["question"]
        try:
            generated_responses = aisuite.generate_text(model_name=config.MODEL_NAME, prompt=user_input, max_length=config.MAX_LENGTH, num_return_sequences=config.NUM_RETURN_SEQUENCES)
            response = generated_responses[0]['generated_text']
        except Exception as e:
            response = f"Error: {str(e)}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
