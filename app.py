import sys
from flask import Flask , render_template , request 
from src.pipeline.predict_pipeline import PredictPipeline , CustomData
sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")

app = Flask(__name__)

# @app.route("/", methods = ["GET", "POST"])
# def index():
#     if request.method == "GET":
#         return render_template("index.html")
#     else:
#         data = CustomData(
#             age = (request.form.get("age")),
#             workclass = (request.form.get("workclass")),
#             education_num = (request.form.get("education_num")),
#             marital_status = (request.form.get("marital_status")),
#             occupation = (request.form.get("occupation")),
#             relationship = (request.form.get("relationship")),
#             race = (request.form.get("race")),
#             sex = (request.form.get("sex")),
#             capital_gain = (request.form.get("capital_gain")),
#             capital_loss = (request.form.get("capital_loss")),
#             hours_per_week = (request.form.get("hours_per_week")),
#             native_country = (request.form.get("native_country"))
#         )
        
#         final_data = data.get_data_as_df()
#         print(final_data)
#         print("Before Prediction")
#         predict_pipeline = PredictPipeline()
#         print("Mid Prediction")
#         pred = predict_pipeline.predict(final_data)
#         print("after prediction")

#         result = pred

#         if result == 0:
#             return render_template("predict.html", final_result = "Your Yearly income is less than 50k or equall to 50k")
        
#         else:
#             return render_template("predict.html", final_result = "Your yearly Income is More than 50k ")

# if __name__ == "__main__":
#     app.run(debug=True)

app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    else:
        data = CustomData(
            age = int(request.form.get("age")),
            workclass = (request.form.get("workclass")),
            education_num = (request.form.get("education_num")),
            marital_status = (request.form.get("marital_status")),
            occupation = (request.form.get("occupation")),
            relationship = (request.form.get("relationship")),
            race = (request.form.get("race")),
            sex = (request.form.get("sex")),
            capital_gain = int(request.form.get("capital_gain")),
            capital_loss = int(request.form.get("capital_loss")),
            hours_per_week = int(request.form.get("hours_per_week")),
            native_country = (request.form.get("native_country"))

        )

    final_data = data.get_data_as_df()
    pipeline_prediction = PredictPipeline()
    pred = pipeline_prediction.predict(final_data)

    result = pred

    if result == 0:
        return render_template("predict.html", final_result = "Your Yearly Income is Less than or Equal to 50k:".format(result) )

    elif result == 1:
            return render_template("predict.html", final_result = "Your Yearly Income is More than 50k:".format(result) )
    
if __name__ == "__main__":
     app.run(host = "0.0.0.0", debug = True)