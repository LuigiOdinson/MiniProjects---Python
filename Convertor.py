import tkinter as tk

bg_color = "gray90"
window = tk.Tk()
window.geometry("600x400")
window.configure(bg=bg_color)
window.title("Converter")

# drop down options
input_options = ["Decimal", "Binary", "Octal", "Hexadecimal"]
output_options = ["Decimal", "Binary", "Octal", "Hexadecimal"]
input_variable = tk.StringVar(window)
input_variable.set("Decimal")
output_variable = tk.StringVar(window)
output_variable.set("Decimal")

# widgets
input_menu = tk.OptionMenu(window, input_variable, *input_options)
input_menu.config(width=20)
input_menu.grid(column=0, row=0, padx=30, pady=40)

label1 = tk.Label(window, text="to", font=('Arial', 14))
label1.configure(bg=bg_color)
label1.grid(column=1, row=0, padx=30, pady=40)

output_menu = tk.OptionMenu(window, output_variable, *output_options)
output_menu.config(width=20)
output_menu.grid(column=2, row=0, padx=30, pady=40)

label2 = tk.Label(window, text="Enter input number:", font=('Arial', 14))
label2.configure(bg=bg_color)
label2.grid(column=0, row=1, padx=30, sticky="W")

input_entry = tk.Entry(window, font=('Arial', 13))
input_entry.grid(column=0, row=2, padx=30, pady=20)

label3 = tk.Label(window, text="Output:", font=('Arial', 14))
label3.configure(bg=bg_color)
label3.grid(column=0, row=3, padx=30, pady=20, sticky="W")

output_label = tk.Label(window, text="", font=('Arial', 14), height=4)
output_label.config(bg="gray85")
output_label.grid(column=0, row=4, padx=30, sticky="WE")


def decimal_con(num, output):
    # converting decimal to any output
    result = ""
    if output == "Binary":
        while num >= 1:
            result += str(num % 2)
            num //= 2
        result = int(result[::-1])
    if output == "Octal":
        while num >= 1:
            result += str(num % 8)
            num //= 8
        result = int(result[::-1])
    if output == "Hexadecimal":
        while num >= 1:
            if num % 16 < 10:
                result += str(num % 16)
            if num % 16 >= 10:
                hex_nums = {'A': 10, 'B': 11, 'C': 12,
                            'D': 13, "E": 14, 'F': 15}
                for k, v in hex_nums.items():
                    if num % 16 == v:
                        result += str(k)
            num //= 16
        result = result[::-1]
    if output == "Decimal":
        result = num
    return result


def binary_con(num, output):
    # converting binary to any output
    result = 0
    length = len(str(num))
    if output == "Decimal":
        for i in str(num):
            length -= 1
            result += (2 ** length) * int(i)
    if output == "Octal":
        decimal_result = binary_con(num, "Decimal")  # The decimal result for simpler conversion
        result = decimal_con(decimal_result, "Octal")
    if output == "Hexadecimal":
        decimal_result = binary_con(num, "Decimal")
        result = decimal_con(decimal_result, "Hexadecimal")
    if output == "Binary":
        result = num
    return result


def octal_con(num, output):
    # converting octal to any output
    result = 0
    length = len(str(num))
    if output == "Decimal":
        for i in str(num):
            length -= 1
            result += (8 ** length) * int(i)
    if output == "Binary":
        decimal_result = octal_con(num, "Decimal")
        result = decimal_con(decimal_result, "Binary")
    if output == "Hexadecimal":
        decimal_result = octal_con(num, "Decimal")
        result = decimal_con(decimal_result, "Hexadecimal")
    if output == "Octal":
        result = num
    return result


def hexadecimal_con(num, output):
    # converting hexadecimal to any output
    if output == "Decimal":
        hex_nums = {'A': 10, 'B': 11, 'C': 12,
                    'D': 13, "E": 14, 'F': 15}
        result = 0
        length = len(str(num))
        for n in str(num):
            length -= 1
            if n in hex_nums.keys():
                for key in hex_nums.keys():
                    if n == key:
                        result += (16 ** length) * hex_nums.get(key)
                        break
            else:
                result += (16 ** length) * int(n)

    if output == "Binary":
        decimal_result = hexadecimal_con(num, "Decimal")
        result = decimal_con(decimal_result, "Binary")
    if output == "Octal":
        decimal_result = hexadecimal_con(num, "Decimal")
        result = decimal_con(decimal_result, "Octal")
    if output == "Hexadecimal":
        result = num
    return result


def convert():
    input = input_variable.get()
    output = output_variable.get()
    num = input_entry.get()

    result = ""
    if input == "Decimal":
        result = decimal_con(int(num), output)

    if input == "Binary":
        result = binary_con(int(num), output)

    if input == "Octal":
        result = octal_con(int(num), output)

    if input == "Hexadecimal":
        result = hexadecimal_con(num, output)

    output_label.config(text=result)


submit_button = tk.Button(window, text="Convert", font=('Arial', 12), command=convert)
submit_button.config(bg="gray80")
submit_button.grid(column=1, row=2)

window.mainloop()
