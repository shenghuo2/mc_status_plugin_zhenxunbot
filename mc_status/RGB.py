from PIL import Image
# 高版本的RGB三原色渐变的实现
def gradient(start, end, steps):
    r1, g1, b1 = start
    r2, g2, b2 = end
    r_step = (r2 - r1) / steps
    g_step = (g2 - g1) / steps
    b_step = (b2 - b1) / steps
    gradient = []
    for i in range(steps):
        r = r1 + (r_step * i)
        g = g1 + (g_step * i)
        b = b1 + (b_step * i)
        gradient.append((int(r), int(g), int(b)))
    return gradient

start = (255, 0, 0)  # 红
end = (0, 0, 255)    # 蓝
steps = 10

gradient = gradient(start, end, steps)

width = len(gradient)
height = 1

img = Image.new('RGB', (width, height))
pixels = img.load()

for x in range(width):
    pixels[x, 0] = gradient[x]

img.show()
