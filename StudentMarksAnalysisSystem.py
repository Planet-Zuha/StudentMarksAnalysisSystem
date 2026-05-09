import streamlit as st
import numpy as np
import pandas as pd

st.title("Student Marks Analysis System")

students = []

for i in range(3):

    st.subheader(f"Student {i+1}")

    name = st.text_input(f"Enter Student Name {i+1}")

    gender = st.radio(
        f"Select Gender {i+1}",
        ("Male", "Female"),
        key=i
    )

    marks = st.number_input(
        f"Enter Marks {i+1}",
        min_value=0,
        max_value=100,
        key=f"marks{i}"
    )

    students.append({
        "name": name,
        "gender": gender,
        "marks": marks
    })

if st.button("Submit"):

    try:

        for student in students:

            if student["name"] == "":
                raise ValueError("Student name cannot be empty!")

        marks_array = np.array(
            [student["marks"] for student in students]
        )

        mean_marks = np.mean(marks_array)
        max_marks = np.max(marks_array)

        st.success("Data submitted successfully!")

        st.write("Mean Marks:", round(mean_marks, 2))
        st.write("Maximum Marks:", max_marks)

        for student in students:

            if student["marks"] >= 50:
                student["result"] = "Pass"
            else:
                student["result"] = "Fail"

        df = pd.DataFrame(students)

        sorted_df = df.sort_values(by="marks")

        st.subheader("Student Data")
        st.dataframe(sorted_df)

        st.subheader("Student Marks Graph")

        chart_data = sorted_df.set_index("name")["marks"]

        st.bar_chart(chart_data)

    except ValueError as e:
        st.error(e)