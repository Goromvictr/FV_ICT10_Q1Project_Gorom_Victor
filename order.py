from pyscript import document

product_names = { # Mapping of checkbox IDs to product names
    "pansitbato_cb": "Pansit Bato",
    "bicolexpress_cb": "Bicol Express",
    "tinuktok_cb": "Tinuktok",
    "kalingking_cb": "Kalingking",
    "pinakru_cb": "Pinakru"
}

def calculate_total(event=None): # Calculate total price based on selected products and quantities
    products = {
        "pansitbato_cb": {"price": 159, "qty_id": "pansitbato_qty"},
        "bicolexpress_cb": {"price": 149, "qty_id": "bicolexpress_qty"},
        "tinuktok_cb": {"price": 139, "qty_id": "tinuktok_qty"},
        "kalingking_cb": {"price": 99, "qty_id": "kalingking_qty"},
        "pinakru_cb": {"price": 99, "qty_id": "pinakru_qty"}
    }

    total = 0
    checked = 0

    for checkbox_id, data in products.items():
        checkbox = document.getElementById(checkbox_id)
        qty_input = document.getElementById(data["qty_id"])
        quantity = int(qty_input.value) if qty_input.value else 0

        if checkbox.checked and quantity > 0:
            total += data["price"] * quantity
            checked += 1

    # ✅ Check delivery checkbox
    delivery_checkbox = document.getElementById("delivery_cb")
    delivery = delivery_checkbox.checked if delivery_checkbox else False

    if delivery:
        total += 50
        delivery_note = "Delivery fee of ₱50.00 included."
    else:
        delivery_note = "No delivery fee."

    output = document.getElementById("output")
    if checked == 0:
        output.innerText = "Please select at least one product and enter quantity."
    else:
        output.innerText = f"Total: ₱{total:.2f}\n{delivery_note}"


def confirm_order(event=None): # Confirm order and display details
    prices = {
        "pansitbato_cb": {"price": 159, "qty_id": "pansitbato_qty"},
        "bicolexpress_cb": {"price": 149, "qty_id": "bicolexpress_qty"},
        "tinuktok_cb": {"price": 139, "qty_id": "tinuktok_qty"},
        "kalingking_cb": {"price": 99, "qty_id": "kalingking_qty"},
        "pinakru_cb": {"price": 99, "qty_id": "pinakru_qty"}
    }

    product_names = {
        "pansitbato_cb": "Pansit Bato",
        "bicolexpress_cb": "Bicol Express",
        "tinuktok_cb": "Tinuktok",
        "kalingking_cb": "Kalingking",
        "pinakru_cb": "Pinakru"
    }

    selected = []
    total = 0

    for prod_id, data in prices.items():
        checkbox = document.getElementById(prod_id)
        qty_input = document.getElementById(data["qty_id"])
        quantity = int(qty_input.value) if qty_input.value else 0

        if checkbox.checked and quantity > 0:
            selected.append(f"{product_names[prod_id]} x{quantity}")
            total += data["price"] * quantity

    customer_name = document.getElementById("name").value.strip()
    lastname = document.getElementById("lastname").value.strip()
    email = document.getElementById("email").value.strip()
    contact = document.getElementById("contact").value.strip()

    output2 = document.getElementById("output2")
    container3 = document.querySelector(".container3")

    if not customer_name or not lastname or not email or not contact:
        output2.innerText = "Please fill in all customer details before confirming."
        return

    if not selected:
        output2.innerText = "Please select at least one product and enter quantity before confirming."
        return

    # Delivery logic goes here
    delivery_checkbox = document.getElementById("delivery_cb")
    delivery = delivery_checkbox.checked if delivery_checkbox else False

    if delivery:
        total += 50
        delivery_note = "Delivery: Yes (₱50.00 added)"
    else:
        delivery_note = "Delivery: No"

    message = (
        f"Order confirmed for {customer_name} {lastname}!\n"
        f"Products: {', '.join(selected)}\n"
        f"{delivery_note}\n"
        f"Total: ₱{total:.2f}\n"
        f"Thank you for your order."
    )

    output2.innerText = message
    container3.classList.add("expanded")


def clear_content(event=None): # Clear all inputs and outputs
    document.getElementById("output").innerText = ""
    document.getElementById("output2").innerText = ""
    document.getElementById("name").value = ""
    document.getElementById("lastname").value = ""
    document.getElementById("email").value = ""
    document.getElementById("contact").value = ""
    for prod_id in ["pansitbato_cb", "bicolexpress_cb", "tinuktok_cb", "kalingking_cb", "pinakru_cb"]:
        document.getElementById(prod_id).checked = False