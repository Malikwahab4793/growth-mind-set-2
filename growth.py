# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO
# st.set_page_config(page_title= "Data Sweeper", layout='wide')

# #Custom CSs
# st.markdown(
#     """
#     <style>
#     .stApp{
#         background-color: black;
#         color: white
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
# )

# #Title and discription 
# st.title ("Datasweeper strealing Integrator by Abdul Wahab")
# st.write("Transform your file bitween CSV and Excel Formats with build in data cleaning and visulization creating the projecct for Q3!")

# #file uploder
# uploaded_files =st.file_uploader("upload your file (accept CSV or Excel):", type=["cvs", "xlsx"], accept_multiple_files=(True))

# if uploaded_files:
#     for file in uploaded_files:
#         file_exe = os.path.splitext(file.name)[-1].lower() 
#         if file_exe == ".csv":  
#             df = pd.read_csv(file)
#         elif file_exe == "xlsx":
#             df=pd.read_excel(file)
#         else: 
#             st.error(f"unsupported file type:{ file_exe}")
#             continue

# #file details
# st.write("review the head of Dataframe")
# st.dataframe(df.head())



# #data cleaning option 

# st.subheader("data cleaning options")
# if st.checkbox(f"clean data for {file.name}"):
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button(f"Remove duplicate from the file:{file.name}"):
#             df.drop_duplicates(inplace=True)
#             st.write("Duplicate remove!")
#     with col2:
#         if st.button(f"file missing value for {file.name}"):
#             numeric_cols=df.select_dtypes(include=['number'].colums)
#             df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())
#             st.write(f"missing value have been filled!")
#     st.subheader("Select Colums to keep ")
#     colums=st.multiselect(f"chose colums for {file.name}", df.columns, default=df.columns)
#     df=df[colums]

#     #data visuliazation 
#     st.subheader("Data visualization")
#     if st.checkbox(f"show visuliazation for {file.name}"):
#         st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
    
#     #Conversion option
#     st.subheader("Conversion options")
#     conversion_type= st.radio(f"Convert {file.name} to :",["CVS", "Excel"],key=file.name)

#     st.button(f"convert {file.name}")
#     buffer = BytesIO()
#     if conversion_type == "CVS":
#         df.to_cvs(buffer, index=False)
#         file_name = file.name.replace(file_exe, "csv")
#         mime_type="text/cvs"

#     elif conversion_type == "Excel":
#         df.to_excel(buffer, index=False)
#         file_name= file.name.replace(file_exe, "xlsx")
#         mime_type="application/vnd.openxmlformate-officedocuments.spreadsheetml.sheet"
#         buffer.seek(0)
        
#         st.download_button(
#         label=(f"Download {file.name} as {conversion_type}"),
#         data=buffer, 
#         file_name=file_name,
#         mime=mime_type
#     )
# st.success("All file Process successfully!")



import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout='wide')

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("Datasweeper - Streamlit Integrator by Abdul Wahab")
st.write("Transform your file between CSV and Excel formats with built-in data cleaning and visualization. Creating the project for Q3!")

# File uploader
uploaded_files = st.file_uploader("Upload your file (accepts CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # File preview
        st.write(f"Preview of {file.name}:")
        st.dataframe(df.head())

        # Data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include='number').columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")

            # Select columns
            st.subheader("Select Columns to Keep")
            selected_columns = st.multiselect(
                f"Choose columns for {file.name}",
                df.columns.tolist(),
                default=df.columns.tolist()
            )
            df = df[selected_columns]

            # Visualization
            st.subheader("Data Visualization")
            if st.checkbox(f"Show bar chart for {file.name}"):
                numeric_data = df.select_dtypes(include='number')
                if not numeric_data.empty:
                    st.bar_chart(numeric_data.iloc[:, :2])
                else:
                    st.warning("No numeric columns to show in chart.")

            # Conversion
            st.subheader("Conversion Options")
            conversion_type = st.radio(
                f"Convert {file.name} to:",
                ["CSV", "Excel"],
                key=file.name
            )

            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

    st.success("✅ All files processed successfully!")
