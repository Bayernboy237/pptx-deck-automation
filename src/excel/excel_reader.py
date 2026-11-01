from openpyxl import load_workbook

def extract_data(file_path, sheet_name, cell_range):

    workbook = load_workbook(file_path, data_only=True, read_only=True)

    try: 
        worksheet = workbook[f"{sheet_name}"]

        data = []

        for row in worksheet[cell_range]:

            row = [cell.value for cell in row]
            
            data.append(row)
        

        return data

    finally: 
        workbook.close()