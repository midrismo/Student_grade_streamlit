import streamlit as st


st.set_page_config(page_title="Simple Grade Calculator", page_icon="📚")

st.title("📚 Student Grade Calculator")
st.write("Enter your marks below to find your average grade.")

subject_count = st.selectbox("How many subjects do you have?", [3, 4, 5, 6, 7, 8])

with st.form("grade_calculator"):
    st.subheader("Enter your marks")
    st.caption("Enter each mark as a number from 0 to 100.")

    marks = []
    for subject_number in range(1, subject_count + 1):
        mark = st.number_input(
            f"Subject {subject_number}",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key=f"subject_{subject_number}",
        )
        marks.append(mark)

    calculate = st.form_submit_button("Calculate my grade", type="primary")

if calculate:
    average = sum(marks) / len(marks)

    if average >= 90:
        letter_grade = "A"
        message = "Excellent work!"
    elif average >= 80:
        letter_grade = "B"
        message = "Very good work!"
    elif average >= 70:
        letter_grade = "C"
        message = "Good effort!"
    elif average >= 60:
        letter_grade = "D"
        message = "You passed, but keep practicing."
    else:
        letter_grade = "F"
        message = "Keep studying. You can improve!"

    st.subheader("Your result")
    st.metric("Average mark", f"{average:.1f}%")
    st.metric("Letter grade", letter_grade)
    st.write(message)
    st.progress(average / 100)

st.divider()
st.caption("Grade guide: A = 90–100, B = 80–89, C = 70–79, D = 60–69, F = below 60.")
