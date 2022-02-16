import colorgram


colors = colorgram.extract('image.jpg', 20)
extracted_colors = []
for each in range(len(colors)):
    color = colors[each]
    rgb = color.rgb
    pallette = (rgb[0], rgb[1], rgb[2])
    extracted_colors.append(pallette)
print(len(extracted_colors))
print(extracted_colors)
