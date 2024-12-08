import csv

def generate_symbol(pin_data, output_file=None):
    symbol_template = """(symbol ""
    {pins}
)"""
    pin_template = """(pin {pin_type} line (at 0 {y_position:.2f} 0) (length 3.81)
      (name "{pin_name}" (effects (font (size 1.27 1.27))))
      (number "{pin_number}" (effects (font (size 1.27 1.27))))
    )"""

    pins_str = ""
    y_position = 0
    for pin_number, pin_name, pin_type in pin_data:
        pin_str = pin_template.format(pin_type=pin_type, pin_name=pin_name, pin_number=pin_number, y_position=-y_position)
        pins_str += pin_str + "\n    "
        y_position += 2.54

    symbol_str = symbol_template.format(pins=pins_str.strip())
    
    if output_file:
        with open(output_file, 'w') as file:
            file.write(symbol_str)
    else:
        print(symbol_str)

def read_csv(file_path):
    pin_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            pin_data.append(row)
    return pin_data

# Example usage (change paths to match your setup)
csv_file_path = 'kicad-auto\example_pins.csv'
output_file_path = 'kicad-auto\output.txt'

pin_data = read_csv(csv_file_path)
generate_symbol(pin_data, output_file=output_file_path)