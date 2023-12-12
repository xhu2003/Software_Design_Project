# **Software_Design_Project**
This is the repo of software design project for oim3640
Group members: Carina Hu, Max Sun
 
# **Project Proposal**: 

## 1. The Big Idea: 

-- Our project aims to develop a stock portfolio management tool/website, designed to assit users to build a personalized stock sportfolio, track real-time stock market data, assess portfolio performance, and receive investment insights.

-- The project will allows the team to epxlore topics like: 
  - Flask: User-input and interace design 
  - API integration such as Yahoo Finance
  - JSON data processing
  - data visualization using python libary such as Matplotlib or Plotly 
  

-- Minimum Viable Product (MVP) will include:
  - user registration and login
  - basic portfolio management functions(adding/removing stocks)
  - integration with a stock market API for real-time data display. 

-- Stretch Goal: 
  - Incorporating platform such as Twiolio to enhance user interaction through phone notification 
  - Provoding Stock performance matrix such as expected return/NPV to inform investment insights 

## 2. Learning Objectives: 

Shared Goals: 
  - Gain proficiency in Flask and its integration with API 
  - Develop skills in working with financial APIs and handling real-time data.
  - Enhance our understanding of database management for user and portfolio data.

Individual Goals:
  - **Carina**: Further enhance my previous knowledge on data extraction, cleaning, and processing to meet my career goals (interest in business analytics); familiarize with interface/website design using flask

  - **Max**: Focus on backend development such as building flask and database integration; improve code efficiency and incorportate financial knowledge to provide forecast to end users.
  
## 3. Implementation Plan
- We plan to investigate and explore all the topics outlined in part 1 to get familar with the documentation. To provide us with more knowledge on how the topics can be used to build our project, we will explore simialr projects in Github to gain an basic understanding of the structure/outline required. 


- Our current plan is to use Flask for constructing the user interface To fetch real-time stock data, we'll explore APIs like Alpha Vantage or Yahoo Finance. The implementation plan will evolve as we dive deeper into these topics and understand their integration better.
## 4.Project Schedule 
### WEEK 1: 
- Explore and build basic flask application and project structure 
- Create basic routes for the functionalities such as user registration, stock management. 
- Draw the user interface design and user expeirnece flow: What kind of experience we want to provide to our users 

### WEEK 2: 
- Explore topics such as user login/authentication and database integration. Figure out the logistics/feasibility of the website feature 
- Test user registration and login
- Figure out how to store user data and process them in the backend 

### WEEK 3:
-  Select a stock market API (such as Alpha Vantage or Yahoo Finance) for fetching real-time stock data.
-  Run the API with the Flask feature to retrieve and display stock prices and details. 
-  Test the feasibility with communication chanel like Slack

### WEEK 4: 
- Set up and integrate twilio to our flask aplication for message notification about stock prices fluctuation
- Develop logic to trigger SMS alerts based on specific conditions (ex: stock price drops or rises beyond a certain threshold).
- Test the function with our own device

### WEEK 5: 
- Run the advance feature added on week 4 to test the functionality of the overall application
- Integrating all the previous sections
- Add additional feastures such as forecasting return or calculating NPV for the selected portfolio, if time allows. 

### WEEK 6: 
- Meet with Professor Li to Debug and refine any code structure 
- Finish the documentation of the entire process 

  

## 5. Collaboration Plan
- We plan to adopt an **Agile development** methodology, with weekly objectives (listed in implementation plan) and regular meetings to assess progress and reassign tasks as needed. Since we project consists of multiple sections and requires integration, agile approach allows us to handle the proejct in smaller sections and allows us to respond to changes quickly. 
  
- We will adopt a both **collaborative and indivudally-paced** work style for this project. We plan to divide tasks based on individual learning goals and expertise to meet individual interests and ensure equal contribution. However, We will also communicate constantly to make sure that we understand each other's task and responsibility. 

## 6. Risks & Limitations
- Since we need to store individual data for portfolio management, the risk and challenge lies in the data storage and manamenet process. Additional tools such as SQL might need to be explored to achieve the purpose of the project

- Since the process requires data storage, limitation might occur as it may require more front-end feature for website design, which is a topic yet to be covered in the scope of this course. 

## 7. Additional Course content 
Topics that would be beneficial to the project:
- API Integration such as Yahoo Finance and Twilio 
- User interface design details for website construction
- Testing various features within Flask
- Database Design and Management