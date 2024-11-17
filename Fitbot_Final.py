from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key="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" 
)

def chat_with_groq(prompt):
    fitness_prompt = f"You're a fitness expert. Answer the following questions with fitness and health-related information. {prompt}"

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": fitness_prompt,
        }],
        model="llama3-8b-8192", 
    )

    return chat_completion.choices[0].message.content


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
   
    user_input = request.form['user_input']
    
   
    response = chat_with_groq(user_input)
    
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
