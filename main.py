import streamlit as st
import time

st.title('Streamlit 入門')
st.write('progress bar')
'Start!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column,midle_column,right_column = st.columns(3)
button = left_column.button('show text in right column. ')
if button:
    right_column.write("This is right column")

expander = st.expander('toiawase')
expander.write(("toiawasenaiyou"))

# option = st.sidebar.text_input('please teach me your hobby.')
# 'your hobby is ', option , '.'

# condition = st.sidebar.slider('your condition',0,100,50)
# 'your condition is ',condition,'.'

# option = st.selectbox(
#     'Please teach me your favolite number.',
#     list(range(1,11))
# )

# 'your favorite number ', option ,'.'

# if st.checkbox('Show Image'):
#     img = Image.open('/home/mahigashimura/develop webapp/Screenshot 2022-04-01 23.43.32.png')
#     st.image(img,caption='test',use_column_width=True)

