# PROJECT REPORT

## SCOPE OF PROJECT

The primary goal of this project is to develop predictive models that can effectively identify individuals at risk of cardiovascular disease based on their health-related attributes. The dataset captures a diverse set of information, ranging from measurable physical characteristics to lifestyle choices, providing a holistic view for predictive analysis.

## MINIMUM TECHNICAL REQUIREMENTS

To accomplish project goals, the following minimum technical requirements have been identified:

- MS - EXCEL with Data Analytics Tool Pack
- GIT and GitHub account
- PYTHON ver3.x and above
- 8GB of RAM

These components are crucial for the foundational infrastructure that will support the project's development lifecycle.

## DATA RESOURCES

Appropriate data resources are essential for informed decision-making and include:

- [https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)
- Discussions with Medical Practitioners for Data Relations

Access to these resources will enable us to process, analyze, and classify data efficiently, ensuring accuracy in project deliverables.

## DATASET DESCRIPTION

Our data sets encompass a variety of formats and origins. It comprises 70,000 records of patient data, with 11 features and a target variable. The dataset is designed to provide insights into the presence or absence of cardiovascular disease based on various health-related factors.

There are 3 types of input features:

- _Objective_: Factual information
- _Examination_: Results of medical examination
- _Subjective_: Information given by the patient.

Features:

1. Age | _Objective_ _Feature_ | age | int (days)
2. Height | _Objective_ _Feature_ | height | int (cm)
3. Weight | _Objective_ _Feature_ | weight | float (kg)
4. Gender | _Objective_ _Feature_ | gender | categorical code 1:Female, 2:Male
5. Systolic Blood Pressure | _Examination_ _Feature_ | bp_high | int
6. Diastolic Blood Pressure | _Examination_ _Feature_ | bp_low | int
7. Cholesterol | _Examination_ _Feature_ | cholesterol | 1: normal, 2: above normal, 3: high
8. Glucose Leves | _Examination_ _Feature_ | gluc | 1: normal, 2: above normal, 3: high
9. Smoking | _Subjective_ _Feature_ | smoke | binary
10. Alcohol intake | _Subjective_ _Feature_ | alco | binary
11. Physical activity | _Subjective_ _Feature_ | physically_active | binary
12. Cardiovascular Disease Presence | Target Variable | cardio | binary

Each data variable provides unique insights and value to the project, helping drive our strategic approach to achieving the project objectives.

Private ([https://app.clickup.com/9014060945/docs/8cmf9wh-574/8cmf9wh-654](https://app.clickup.com/9014060945/docs/8cmf9wh-574/8cmf9wh-654))

## MEMBERS

The project will be undertaken by a dedicated team consisting of skilled individuals, each bringing their expertise:

- **PRAKASH PUN** \- [https://github.com/](https://github.com/tirth-patel01)[prakash-pun](https://github.com/prakash-pun)
- **GAURAV SINGH** - [https://github.com/gaurav809](https://github.com/gaurav809)
- **TIRTH PATEL** \- [https://github.com/tirth-patel01](https://github.com/tirth-patel01)
- **BIKKY SINGH** - [https://github.com/](https://github.com/tirth-patel01)[bikkysr](https://github.com/bikkysr)
- **JANKIBA** **ZALA** \- [https://github.com/](https://github.com/tirth-patel01)[Janki-31](https://github.com/Janki-31)
- **RUTUL PRAJAPATI** - [https://github.com/](https://github.com/tirth-patel01)[rutul7802](https://github.com/rutul7802)
- **YETUNDE SHITTU** - [https://github.com/](https://github.com/tirth-patel01)[whyteeth](https://github.com/whyteeth)
- **SWETHA TANIKONDA** - [https://github.com/](https://github.com/tirth-patel01)[Swethaloyalist](https://github.com/Swethaloyalist)
- **AMAN NAIN** - [https://github.com/amannain122](https://github.com/amannain122)

Collectively, the team's collaborative efforts will be pivotal in steering the project towards success.

## DATA CLEANING

In the initial phase, each team member was assigned a particular column to find descriptive statistics for individual columns and also the relation with the target variable.

## Data Description

Cardiovascular disease (CVD) is a term that covers several conditions that affect the heart and blood vessels, such as coronary heart disease, stroke, heart failure, and more. CVD is a leading cause of death and disability worldwide, and it can be prevented or delayed by identifying and modifying the risk factors that contribute to its development. Here is a summary:

●Age: Age is one of the most important risk factors for cardiovascular disease, as the risk increases with advancing age. This is because the aging process affects the structure and function of the heart and blood vessels, making them more prone to damage and disease. The risk of cardiovascular disease also varies by sex and race, as women tend to develop the disease later than men, and some racial and ethnic groups have higher rates of the disease than others.

●Height: Height may have a modest influence on the risk of cardiovascular disease, as some studies have suggested that taller people have a lower risk than shorter people. This may be due to genetic, environmental, or developmental factors that affect both height and cardiovascular health. However, the effect of height is not very strong and may be confounded by other factors, such as body weight, diet, and physical activity.

●Weight: Weight, or more specifically, body mass index (BMI), is a measure of body fatness that can affect the risk of cardiovascular disease. BMI is calculated by dividing weight in kilograms by height in meters squared. A BMI of 18.5 to 24.9 is considered normal, while a BMI of 25 to 29.9 is considered overweight, and a BMI of 30 or more is considered obese. Overweight and obesity can increase the risk of cardiovascular disease by raising blood pressure, cholesterol, blood sugar, and inflammation, and by impairing the function of the heart and blood vessels. Losing weight can lower the risk of cardiovascular disease and improve the quality of life.

●Gender: Gender is another important risk factor for cardiovascular disease, as men and women have different patterns and outcomes of the disease. Men tend to develop the disease earlier and more severely than women and have a higher risk of dying from the disease. Women, on the other hand, tend to have more atypical symptoms and less effective treatments than men, and have a higher risk of complications and disability from the disease. The differences between men and women may be due to biological, hormonal, behavioral, and social factors that affect the development and progression of the disease.

●Systolic blood pressure(ap_hi): Systolic blood pressure is the pressure of blood against the artery walls when the heart contracts. It is the higher of the two numbers in a blood pressure reading, and is usually written first, such as 120/80 mmHg. Systolic blood pressure is a major risk factor for cardiovascular disease, as high systolic blood pressure, or hypertension, can damage the arteries, the heart, and other organs, and increase the risk of heart attack, stroke, heart failure, and kidney disease. Systolic blood pressure is considered normal if it is less than 120 mmHg, elevated if it is 120 to 129 mmHg, high if it is 130 to 139 mmHg, and very high if it is 140 mmHg or more. Systolic blood pressure can be controlled by lifestyle changes, such as quitting smoking, exercising, eating a healthy diet, reducing stress, and limiting alcohol intake, and by medications, such as diuretics, beta-blockers, calcium channel blockers, angiotensin-converting enzyme inhibitors, and angiotensin receptor blockers.

●Diastolic blood pressure(ap_lo): Diastolic blood pressure is the pressure of blood against the artery walls when the heart relaxes. It is the lower of the two numbers in a blood pressure reading, and is usually written second, such as 120/80 mmHg. Diastolic blood pressure is also a risk factor for cardiovascular disease, but less than systolic blood pressure. High diastolic blood pressure, or hypertension, can also damage the arteries, the heart, and other organs, and increase the risk of cardiovascular events. Diastolic blood pressure is considered normal if it is less than 80 mmHg, high if it is 80 to 89 mmHg, and very high if it is 90 mmHg or more. Diastolic blood pressure can be controlled by some lifestyle changes and medications as systolic blood pressure.

●Cholesterol: Cholesterol is a type of fat that circulates in the blood and is essential for many bodily functions. However, too much of the bad cholesterol (LDL) or too little of the good cholesterol (HDL) can increase the risk of cardiovascular disease by forming plaques in the arteries that can narrow or block the blood flow to the heart and brain. High cholesterol can be lowered by lifestyle changes, such as quitting smoking, exercising, eating a healthy diet, and losing weight, and by medications, such as statins, bile acid sequestrants, niacin, fibrates, and ezetimibe.

●Glucose(gluc): Glucose is a type of sugar that is the main source of energy for the cells. Glucose levels in the blood are regulated by the hormone insulin, which is produced by the pancreas. High glucose levels, or hyperglycemia, can occur when the body does not produce enough insulin or does not use it properly, as in diabetes. High glucose levels can damage the blood vessels and nerves, and increase the risk of cardiovascular disease, especially in people with diabetes. Glucose levels can be controlled by lifestyle changes, such as exercising, eating a healthy diet, and losing weight, and by medications, such as metformin, sulfonylureas, thiazolidinediones, and insulin.

●Smoking(smoke): Smoking is one of the most important modifiable risk factors for cardiovascular disease, as smoking damages the lining of the arteries, increases blood pressure and heart rate, reduces oxygen supply to the heart, and increases the risk of blood clots. Smoking is also a risk factor for other diseases, such as lung cancer, chronic obstructive pulmonary disease, and stroke. Quitting smoking can significantly lower the risk of cardiovascular disease and improve the overall health and well-being.

●Alcohol intake(alco): Alcohol intake can have both beneficial and harmful effects on the risk of cardiovascular disease, depending on the amount and frequency of consumption. Moderate alcohol intake, defined as up to one drink per day for women and up to two drinks per day for men, may have a protective effect on the risk of cardiovascular disease, by increasing HDL cholesterol, reducing blood clotting, and lowering stress. However, excessive alcohol intake, defined as more than three drinks per day for women and more than four drinks per day for men, can have a detrimental effect on the risk of cardiovascular disease, by increasing blood pressure, triglycerides, weight, and inflammation, and by causing irregular heartbeats, cardiomyopathy, and stroke. Therefore, it is advisable to limit alcohol intake to moderate levels or avoid it altogether, especially for people who have other risk factors or existing cardiovascular disease.

●Physical activity(active): Physical activity is one of the most beneficial lifestyle factors for preventing and managing cardiovascular disease, as physical activity can improve cardiovascular fitness, lower blood pressure, control blood sugar, prevent obesity, reduce stress, and enhance mood. Regular physical activity can also reduce the risk of other chronic diseases, such as diabetes, cancer, and dementia. The American Heart Association recommends at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous-intensity aerobic exercise per week for adults, and at least 60 minutes of moderate-to-vigorous physical activity per day for children and adolescents.

●Presence or absence of cardiovascular disease(cardio): The presence or absence of cardiovascular disease is the ultimate outcome of the interaction of all the other risk factors, as well as genetic and environmental factors. People who have already had a cardiovascular event, such as a heart attack or a stroke, have a higher risk of having another event, compared to people who have not had any cardiovascular disease. Therefore, people who have cardiovascular disease need to be more aggressive in controlling their risk factors and adhering to their treatment plans, to prevent further complications and improve their quality of life. People who do not have cardiovascular disease need to be aware of their risk factors and take preventive measures to lower their risk and maintain their cardiovascular health.

These are some of the main factors that can affect the risk of CVD, but there are others, such as stress, air pollution, and inflammation, that can also play a role. To predict the risk of CVD, various models have been developed that use different combinations of these factors, such as the Framingham Risk Score, the SCORE, the Reynolds, the ACC/AHA, the JBS3, the MESA, the QRISK, and the China-PAR[8](https://www.healthy-heart.org/keep-your-heart-healthy/predicting-managing-risk-of-heart-disease/). These models use mathematical equations or machine learning algorithms to estimate the probability of having a CVD event, such as a heart attack or a stroke, within a certain time frame, usually 10 or 30 years. These models can help identify high-risk individuals who may benefit from more intensive interventions, such as medications, surgery, or lifestyle changes, to prevent or delay the onset of CVD…

Source(s)

1\. [Cardiovascular disease risk factors | Ada](https://ada.com/cardiovascular-disease-risk-factors/)

2\. [Cardiac Risk Calculator and Assessment - Cleveland Clinic](https://my.clevelandclinic.org/health/articles/17085-heart-risk-factor-calculators)

3\. [Predicting and managing the risk of heart disease](https://www.healthy-heart.org/keep-your-heart-healthy/predicting-managing-risk-of-heart-disease/)

4\. [A cardiologist’s guide to machine learning in cardiovascular disease ...](https://link.springer.com/article/10.1007/s00395-023-00982-7)

5\. [An innovative model for predicting coronary heart disease using ...](https://cardiab.biomedcentral.com/articles/10.1186/s12933-023-01939-9)

6\. [Modelling of longitudinal data to predict cardiovascular disease risk ...](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-021-01472-x)

7\. [Implementation of a Heart Disease Risk Prediction Model Using ... - Hindawi](https://www.hindawi.com/journals/cmmm/2022/6517716/)

8\. [Cardiovascular Disease Photos and Premium High Res Pictures - Getty Images](https://www.gettyimages.com/photos/cardiovascular-disease)

9\. [Cardiovascular Disease Pictures, Images and Stock Photos](https://www.istockphoto.com/photos/cardiovascular-disease)

10\. [Cardiovascular Disease royalty-free images - Shutterstock](https://www.shutterstock.com/search/cardiovascular-disease)

11\. [A Visual Guide to Heart Disease - WebMD](https://www.webmd.com/heart-disease/ss/slideshow-visual-guide-to-heart-disease)

12\. [Leading cardiologists reveal new heart disease risk calculator](https://newsroom.heart.org/news/leading-cardiologists-reveal-new-heart-disease-risk-calculator)

13\. [Getty](https://media.gettyimages.com/photos/kid-is-measuring-the-growth-picture-id1151779376?b=1&k=6&m=1151779376&s=612x612&w=0&h=A9YRX22UMmFd27muIZtDfysJPmuXc4AzfjutjgfsfgQ=)
