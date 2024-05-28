import streamlit as st
import time

st.title('streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)





left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('info')
expander.write('naiyou')
#text = st.text_input('あなたが好きな数字は？')
#condition = st.slider('コンディションは？' , 0, 100, 50)
#'あなたが好きな数字:' , text
#'コンディション:' , condition

#if st.checkbox('Show Image'):
#    img = Image.open('sample.jpg')
#    st.image(img, caption='tori', use_column_width=True)


#f = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)
#st.map(df)

thanks.
 



"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```


"""