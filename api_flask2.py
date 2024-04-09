from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

dic = {0: 'no_tumor', 1: 'tumor'}

model = load_model('../Models/TZ_14_89.keras')  # Update the model path

model.make_predict_function()

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(224, 224))
    i = image.img_to_array(i) / 255.0
    i = i.reshape(1, 224, 224, 3)
    p = model.predict(i)
    print(p)
    return p[0]

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("tumor_app2.html")

@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        p = predict_label(img_path) 
        predicted_class = 'tumor' if p > 0.5 else 'no_tumor'
        return render_template("tumor_app2.html", prediction= predicted_class, img_path=img_path)
    return render_template("tumor_app2.html")  # Add this line to handle GET requests

if __name__ == '__main__':
    app.run(debug=True)
