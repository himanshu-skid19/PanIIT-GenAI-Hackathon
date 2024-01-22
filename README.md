<h1 align="center">DineWise AI - Transforming India's Nutrition</h1>

This Project is part of the PanIIT GenAI Hackathon, with the aim to develop a tool that leverages AI that serves the greater good, showcasing the positive potential of AI in our society.

## Introduction
We develop a diet planner application to serve its users with automated diet planning and meal recommendations. With busy schedules, conflicting dietary advice, and individual health goals, people often struggle to make informed choices about their nutrition.

Our AI-integrated diet planner application emerges as a timely and essential solution for this.

## Features
### 1. Personalized Nutrition
Our app can analyze an individual's specific health profile, including age, gender, weight, height, activity level, and medical history, to create a tailored nutrition plan.

### 2. Real-Time Dietary Monitoring
Users can input their daily food intake and receive instant feedback on their nutritional choices. AI can track macronutrient and micronutrient intake to ensure that users meet their daily requirements.

### 3. Recipe Suggestion
The application can suggest personalized recipes based on users' dietary preferences and goals.
AI can optimize recipes for nutrient balance and variety, making it easier for users to diversify their diets.
We give the user option to provide the available ingredients, and our AI makes a healthy recipe tailored to the user's requirements. 

### 4. Goal Oriented Planning
Users can set specific health and fitness goals, such as weight loss, muscle gain, or improved energy levels. AI adjusts meal plans accordingly, continuously optimizing them to align with the user's progress.

## Installation and Setup

1. **Install Dependencies:**
   Install the required libraries using:
```python
pip install -r requirements.txt
```
2. **API Keys Setup:**
Add your Mixtral API key in the "model.py" file:
  ```python
  OPENROUTER_API_KEY = '<INSERT API KEY HERE>'
  ```

3. **Run the Application:**
Execute the following command to run the app:
```python
streamlit run app.py
```
