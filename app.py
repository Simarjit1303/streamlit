import streamlit as streamlit
import pandas as pd
import numpy as np


# dataframe = pd.DataFrame({
#         "Column 1": [1, 2, 3, 4], 
#         "Column 2": [10, 20, 30, 40]
#         })

# streamlit.write("strealit.table:")
# streamlit.write(dataframe)

# streamlit.write("strealit.table:")
# streamlit.table(dataframe)

# streamlit.write("strealit.dataframe:")
# streamlit.dataframe(dataframe)


# chart_data = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns=['a', 'b', 'c']
#         )
# streamlit.line_chart(chart_data)

# streamlit.write("Chart data:")
# streamlit.write(chart_data)

# streamlit.write("streamlit.line_chart:")
# streamlit.line_chart(chart_data)

# streamlit.write("streamlit.area_chart:")
# streamlit.area_chart(chart_data)

# streamlit.write("streamlit.bar_chart:")
# streamlit.bar_chart(chart_data)

# map_data = pd.DataFrame(
#         np.random.randn(1000, 2) / [50, 50] + [52.52, 13.405],
#         columns=['lat', 'lon'])

# streamlit.write("streamlit.map:")
# streamlit.map(map_data)

sidebar = streamlit.sidebar("test sidebar")


tabs = streamlit.tabs(["CHARST", "help"])
with tabs[0]:
        
        streamlit.header("CHARTS")
        streamlit.write("This is the charts tab.")
        
        col1, col2 = streamlit.columns(2)

        with col1:
                with streamlit.expander("Function settings"):

                        x = np.linspace(0, np.pi * 2, 100)

                        t = streamlit.slider("t", 0.0, 10.0, 1.0)

                        x0 = streamlit.slider("x0", 0.0, np.pi * 2, 0.0)

                        y = np.sin(x * t + x0)

                        function_name = streamlit.selectbox("Function", ["sin", "cos", "tan"])
                        function_dict = {
                                "sin": np.sin,
                                "cos": np.cos,
                                "tan": np.tan
                                }

        with col2:
                if streamlit.checkbox("Show line chart"):
                        y = function_dict[function_name](x * t + x0)
                        streamlit.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y},))
with tabs[1]:
        streamlit.header("HELP")
        streamlit.write("This is the help tab.")
        streamlit.write("""
        - Adjust the sliders to change the parameters of the function.
        - Select the function type from the dropdown menu.
        - Check the box to display the line chart.
        """)