# Resume Builder using ChatGPT
## Try Out the Website 
* https://www.wresume.ai
* https://chromewebstore.google.com/detail/wresume-ai-generate-and-o/bnhbllmcopnkobibdhdhedpeofkemkoo

## WResume is now available as a [Chrome Extension](https://chromewebstore.google.com/detail/wresume-ai-generate-and-o/bnhbllmcopnkobibdhdhedpeofkemkoo?authuser=0&hl=en-GB)
Writing a resume doesn’t have to be a hassle. **WResume AI** helps you create and maintain **ATS-friendly** resume points whenever and wherever inspiration strikes. 
- ✅ **Resume points Tailored to you** – Explain your work in your own words and WResume refines it into ATS-friendly, professional resume-ready points. 
- ✅ **Save up to 10 resume points** – Shortlist your favorite resume points and make your future resume edits quick.
- ✅ **Seamless integration** – Your saved points sync with [wresume.ai](https://wresume.ai) , so they're ready for your next resume edits.

No more last-minute stress. No more struggling with words. Just fast resume building—on your terms.

🚀 **Install now and let WResume be a part of your success story**

**Tr Now: https://chromewebstore.google.com/detail/wresume-ai-generate-and-o/bnhbllmcopnkobibdhdhedpeofkemkoo?authuser=0&hl=en-GB**

<img width="407" alt="image" src="https://github.com/user-attachments/assets/197fd8f5-f0f8-4a6c-97db-927d2124bd0c" />

## Motivation
The most important part of applying for a job and getting an interview is having a very formal and concise resume. 
The important part of building a resume are
* Proper Formatting
* Keep the content short and formal 

Now the problem of formatting is already been taken care of by using many customizable templates. The latter is very stressful and time consuming for students.
To say the capabilities of ChatGPT are good is an understatment. OpenAI has built this amazing tool which can make our tasks easier and faster with reliable accuracy. 

To solve this problem, I've built a resume builder which takes data needed for the resume and use GPT to make the the job description formal. The description input doesn't have to be formal. 


## Architecture
<img width="700" alt="image" src="https://user-images.githubusercontent.com/60289522/211461227-c74de195-fdbb-45c8-a77b-b51551f75420.png">

## Run Instructions
* **Requirements** : [Python](https://www.python.org/downloads/)
* Install pdflatex (For Mac Users you can execute `brew install --cask mactex`
* Create an [OpenAI API Token](https://beta.openai.com/account/api-keys)
* Replace the API Token in `gpt_summary.py`
* Go to the desired folder and execute `make run`
* After submitting, for checking the result, go to `result/Resume.pdf`
* For further fine-tuning, edit  `resume/Resume.tex`. 
* To export to pdf run `pdflatex -interaction=nonstopmode result/Resume.tex` 

## Results
### UI
<img width="500" alt="image" src="https://user-images.githubusercontent.com/60289522/211463999-bd30781d-d4cd-46d0-98f1-c7d03fdafdd3.png">

### Resultant Resume
<img width="350" alt="image" src="https://user-images.githubusercontent.com/60289522/211461415-96f97ded-f909-4270-a589-8ba6887ff20c.png">

## This is now available for free
* [WResume](https://www.wresume.ai/)
* [WResume Demo Video](https://www.youtube.com/watch?v=gkUCH-PbHkg&list=LL&index=2&t=20s)
* [Share your experience](https://forms.gle/Xgt1XGKpwSqAGwus8)

## Referenes
* [OpenAI API documentation](https://beta.openai.com/docs/introduction)
* [Resume Template](https://www.overleaf.com/articles/resume-shubhi-rani-apr-2019/fhxzrkcmjzjp)
