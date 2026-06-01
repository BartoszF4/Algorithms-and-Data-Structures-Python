def naive_mean_filter(img_2d, mask_size):
    height = len(img_2d)
    width = len(img_2d[0])
    offset = mask_size // 2
    result = []

    for y in range(height):
        row = []
        for x in range(width):
            val_sum = 0
            count = 0
            for my in range(-offset, offset + 1):
                for mx in range(-offset, offset + 1):
                    ny = y + my
                    nx = x + mx
                    if 0 <= ny < height and 0 <= nx < width:
                        val_sum += img_2d[ny][nx]
                        count += 1
            row.append(val_sum // count)
        result.append(row)
    return result


def build_summed_area_table(img_2d):
    height = len(img_2d)
    width = len(img_2d[0])
    sat = []
    for y in range(height):
        sat.append([0] * width)

    for y in range(height):
        for x in range(width):
            val = img_2d[y][x]
            top = sat[y - 1][x] if y > 0 else 0
            left = sat[y][x - 1] if x > 0 else 0
            top_left = sat[y - 1][x - 1] if y > 0 and x > 0 else 0
            sat[y][x] = val + top + left - top_left
    return sat


def sat_mean_filter(img_2d, mask_size):
    height = len(img_2d)
    width = len(img_2d[0])
    sat = build_summed_area_table(img_2d)
    offset = mask_size // 2
    result = []

    for y in range(height):
        row = []
        for x in range(width):
            y0 = max(0, y - offset)
            y1 = min(height - 1, y + offset)
            x0 = max(0, x - offset)
            x1 = min(width - 1, x + offset)

            A = sat[y0 - 1][x0 - 1] if y0 > 0 and x0 > 0 else 0
            B = sat[y0 - 1][x1] if y0 > 0 else 0
            C = sat[y1][x0 - 1] if x0 > 0 else 0
            D = sat[y1][x1]

            total_sum = D + A - B - C
            count = (y1 - y0 + 1) * (x1 - x0 + 1)
            row.append(total_sum // count)
        result.append(row)
    return result