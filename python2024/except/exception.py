import sys

for i, aline in enumerate(sys.stdin.readlines()):

    fields = aline.strip().split(',')
    line_no= i+1
    field_no= len(fields)
    try:
        if field_no < 4:
            raise Exception(f'資料欄位數不足: line:{line_no} 欄位數:{field_no}')
        if field_no > 4:
            raise Exception(f'資料欄位數過多: line:{line_no} 欄位數:{field_no}')
        elif field_no == 4:
            format_errors = []
            value_errors = []
            for j, field in enumerate(fields):
                if j == 1:
                    if not field.isdigit():
                        format_errors.append(2)
                if j == 2:
                    if not field.isdigit():
                        format_errors.append(3)
                if j == 3:
                    if not field.isdigit():
                        format_errors.append(4)
                    elif field != '0' and field != '1':
                        value_errors.append(4)

            if format_errors and value_errors:
                raise Exception(f'資料格式錯誤與值錯誤: line:{line_no} 格式錯誤:{",".join(map(str, format_errors))} 值錯誤:{",".join(map(str, value_errors))}')
            elif format_errors:
                raise Exception(f'資料格式錯誤: line:{line_no} 格式錯誤:{",".join(map(str, format_errors))}')
            elif value_errors:
                raise Exception(f'資料值錯誤: line:{line_no} 值錯誤:{",".join(map(str, value_errors))}')
    except Exception as e:
        print(e)