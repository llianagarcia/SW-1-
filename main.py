from pyscript import document


CLUB_MEMBERS = [
    "Lliana Garcia",
    "Hezekiah Yap",
    "Ashely Magaling",
    "Daniella Guintu "
]


def check_membership(event=None):
    """
    Retrieves candidate name inputs, checks club membership,
    and displays status without conditional statements or loops.
    """
    
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()

    
    candidate_name = f"{first_name} {last_name}".strip().title()

    
    is_member = candidate_name in CLUB_MEMBERS

    
    messages = {
        True: f"Congratulations, {candidate_name}! You are now part of the Rainbow Catering Club.",
        False: f"Sorry {candidate_name}, your name is not on the list."
    }

   
    result_message = messages[is_member]

    
    result_element = document.querySelector("#result-area")
    result_element.innerText = result_message

    
    style_classes = {
        True: "alert alert-success mt-4 text-center fw-bold",
        False: "alert alert-danger mt-4 text-center fw-bold"
    }
    
    
    result_card = document.querySelector("#result-card")
    result_card.className = style_classes[is_member]