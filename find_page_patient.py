while True:
    max_entry = int(input("Enter the maximum entry : "))
    max_entry -= 1

    # Belarus, 
    max_entry -= 1244

    current_page_no = (max_entry // 21) + 1
    current_patient_no = (max_entry % 21) + 1
    print(f"Page : {current_page_no}, Patient : {current_patient_no}")
    input()