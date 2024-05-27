import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('Display Image')

img = Image.open('sample.jpg')

st.image(img, caption='tori', use_column_width=True)


#f = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)
#st.map(df)
 



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