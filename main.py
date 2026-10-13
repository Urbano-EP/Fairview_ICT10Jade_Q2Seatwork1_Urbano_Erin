from pyscript import document

def checkName(e):
    first_name = ["Erin", "Renn", "GOAT", "John"]
    last_name = ["Urbano", "Santos", "Ako", "Doe"]

    first_name_input = document.getElementById("FirstName").value
    last_name_input = document.getElementById("LastName").value
    full_name = f"{first_name_input} {last_name_input}"

    Correct_Names = ["Erin Urbano", "Renn Santos", "GOAT Ako", "John Doe"]

    confirm_name = full_name in Correct_Names

    message = (f'Sorry {full_name}, your name is not found.', f'Congratulations! {full_name}, your name is found.')

    document.getElementById("output1").innerHTML = message[confirm_name]