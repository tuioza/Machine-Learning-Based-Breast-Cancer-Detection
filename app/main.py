import streamlit as st

def main():
    st.set_page_config(
        page_title='Cancer prediction',
        layout='wide',
        initial_sidebar_state='expanded',
        

    )
    with st.container():
        st.title("Breast cancer predictor")
        st.write("The app uses a machine learning model to predict if a breast mass is benign or malignant based on lab measurements. You can manually update measurements using sliders in the sidebar.")
    col1, col2 = st.columns((4,1))
    with col1:
        st.write("this is colum 1")
    with col2:
        st.write("this column 2")
    return

if __name__ == '__main__':
    main()