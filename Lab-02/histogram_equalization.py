def equalize_histogram(img_2d):
    height = len(img_2d)
    width = len(img_2d[0])
    total_pixels = height * width

    hist = [0] * 256
    for y in range(height):
        for x in range(width):
            hist[img_2d[y][x]] += 1

    cdf = [0] * 256
    current_sum = 0
    for i in range(256):
        current_sum += hist[i]
        cdf[i] = current_sum

    cdf_min = 0
    for val in cdf:
        if val > 0:
            cdf_min = val
            break

    result = []
    for y in range(height):
        row = []
        for x in range(width):
            v = img_2d[y][x]

            new_val = round(((cdf[v] - cdf_min) / (total_pixels - cdf_min)) * 255)

            row.append(new_val)
        result.append(row)

    return result