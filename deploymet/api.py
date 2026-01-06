from flask import Flask,request,jsonify
import joblib 
import help as lm

app=Flask(__name__)

@app.route('/')
def home():
	return jsonify({'hello':"world"})

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    try:
        response_data = [data.get('male'), data.get('age'), data.get('BPMeds'), 
                         data.get('prevalentHyp'), data.get('diabetes'),
                         data.get('totChol'), data.get('sysBP'), 
                         data.get('diaBP'), data.get('BMI'), 
                         data.get('glucose')]
    
        res=lm.predict(response_data)
        print(response_data)
    
        return jsonify({'res':str(int(res))})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)