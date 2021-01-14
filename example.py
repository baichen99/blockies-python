from blockies.blockies import Option, CreateIcon

bg = [134, 85, 36]
fore = [245, 14, 249]
spot = [54, 52, 210]
option = Option(size=10, scale=4, seed='seedString', bgColor=bg, foreColor=fore, spotColor=spot)
CreateIcon(option, './output.png')

# generate 6 icons
from blockies.blockies import RenderImg
import matplotlib.pyplot as plt

for i in range(6):
  option = Option(size=10, scale=4, seed=f'seedString{i}')
  img = RenderImg(option)
  plt.subplot(2, 3, i+1)
  plt.xticks([]), plt.yticks([])  # 隐藏坐标轴
  plt.imshow(img)
plt.show()
  