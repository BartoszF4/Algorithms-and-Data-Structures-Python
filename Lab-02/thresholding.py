def single_thresholding(img_2d, threshold):
    height = len(img_2d)
    width = len(img_2d[0])
    result = []

    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img_2d[y][x]
            gray = int(0.2990 * r + 0.5870 * g + 0.1140 * b)
            row.append(255 if gray >= threshold else 0)
        result.append(row)

    return result


def double_thresholding(img_2d, t_low, t_up):
    height = len(img_2d)
    width = len(img_2d[0])
    result = []

    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img_2d[y][x]
            gray = int(0.2990 * r + 0.5870 * g + 0.1140 * b)
            row.append(255 if t_low <= gray <= t_up else 0)
        result.append(row)

    return result