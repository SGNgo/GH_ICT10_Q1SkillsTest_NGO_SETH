from pyscript import display, document

def generate_order(e):
    # Customer info
    customer_name = document.getElementById("name").value
    customer_address = document.getElementById("address").value
    customer_contact = document.getElementById("contact").value

    # Shoes
    shoe1 = document.getElementById("shoe1").value

    # Display order summary
    display(f"Customer Name: {customer_name}", target="output")
    display(f"Address: {customer_address}", target="output")
    display(f"Contact: {customer_contact}", target="output")
    display(f"Total order: {shoe1}", target="output")
  