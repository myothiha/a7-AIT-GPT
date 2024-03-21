# NLP Assignment 7 (AIT - DSAI)

- [Student Information](#student-information)
- [Evaluation and Analysis](#evaluation-and-analysis)
- [Limitations and Challenges](#limitations-and-challenges)
- [Potential Improvements](#potential-improvements)
- [Conclusion](#conclusion)

## Student Information
 - Name: Myo Thiha
 - ID: st123783

## Dataset
 - After retrieving the PDF files from www.ait.ac.th through Google search, I parse the content to extract relevant information. This data serves as a valuable source for training GPT models, enabling them to comprehend technical content specific to the Asian Institute of Technology. By leveraging this approach, the models gain insights into diverse topics ranging from engineering to environmental studies, fostering a deeper understanding of the institution's academic landscape. Consequently, the AI models trained on this data can provide more informed responses and insights related to AIT's research, programs, and initiatives.

## Prompt Template

Hello! I'm your knowledgeable AIT assistant, here to provide you with insights and information about the Asian Institute of Technology (AIT).
Whether you're a prospective student, a current student, or simply curious about AIT, feel free to ask anything related to the university, and I'll do my best to provide you with clear and informative answers.
From admission procedures to academic programs, campus life, and more, I'm here to assist you in exploring all facets of AIT.
{context}
Query: {question}
Answer:

- Description: This template outlines the framework for an AI assistant tailored to provide information about the Asian Institute of Technology (AIT). It starts with a friendly greeting and offers assistance to anyone interested in AIT. Users are encouraged to ask questions about AIT, and the AI will provide clear and informative answers. The template includes a placeholder for context to personalize responses. Finally, it specifies the structure for user queries and the subsequent answers.

## Model Performance Analysis

### Test Question
Explain about AIT?

### Model Answer
The Asian Institute of Technology (AIT) is an international institute of higher learning established in 1959 to meet regional needs for advanced education in engineering, science, technology, and management. AIT's mission is to develop professionals for sustainable regional development and global integration, with a base in Thailand and affiliated centers worldwide.

### Evaluation

The model's performance in responding to the test question regarding AIT is commendable. It succinctly delivers key information about the institute's establishment, mission, academic focus, and global presence, directly addressing the query. The response maintains clarity, coherence, and accuracy throughout, ensuring ease of understanding and reliability of the information provided. It strikes a balance between conciseness and comprehensiveness, delivering essential details without unnecessary verbosity. Overall, the model demonstrates satisfactory performance in retrieving and presenting relevant information about AIT.


## Unrelated Information Issue

The model's tendency to provide unrelated information can result from challenges in accurately interpreting context or intent, as well as limitations in its training data. To mitigate this issue, strategies such as context-specific fine-tuning, feedback loops, and clearer instructions can be employed. Techniques like context windowing and attention mechanisms can help prioritize relevant information. Continuous monitoring and human oversight are crucial for identifying and addressing instances of unrelated information, guiding the model towards more accurate responses over time.

## Web Application Development

### How to run?

How to run: go inside the app folder using terminal and run `python app.py`. Note that your python environment must contains the dependencies that are described in the requirements.txt.
 - Then, the application can be accessed on http://localhost:8000
 - You will directly land on the "Home" page.
 - Note: the app will only run on the device with GPU.