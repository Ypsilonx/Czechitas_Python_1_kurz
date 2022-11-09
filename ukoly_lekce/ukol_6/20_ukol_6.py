def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

import csv

with open('znamky_za_semestr.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rows = []
    for row in csv_reader:
        if line_count == 0:
            header = row
            # print(header)
            line_count += 1
        else:
            row = replace_values(row, '1', 'A')
            row = replace_values(row, '2', 'B')
            row = replace_values(row, '3', 'C')
            row = replace_values(row, '4', 'D')
            row = replace_values(row, '5', 'F')
            rows.append(row)
            line_count += 1
    print(f'Ve třídě je {line_count - 1} žáků.')
    # print(rows)
    
    with open('znamky_za_semestr_upravene.csv', mode='w+', encoding='utf-8', newline='') as csv_file2:
        csv_writer = csv.writer(csv_file2, delimiter=',')
        
        csv_writer.writerow(header)
        csv_writer.writerows(rows)