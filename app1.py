import streamlit as st 

from transformers import pipeline
sent_pipeline = pipeline("sentiment-analysis")

def main():

    # st.title("Sentiment Analyzer")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Sentiment Analyzer </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    # st.markdown("# TEXT")
    text = st.text_input(" ",placeholder="Type here ...")

    # result=""
    if st.button("Predict"):
        result=sent_pipeline(text)[0]["label"]
        # st.success('The output is {}'.format(result))
        st.info(f"Sentiment : {result}")


if __name__=='__main__':
    main()
    
    
    
