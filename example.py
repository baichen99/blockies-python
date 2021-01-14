from blockies.blockies import Option, CreateIcon

bg = [0, 233, 233]
fore = [123, 0, 123]
spot = [22, 22, 233]
option = Option(size=12, scale=4, seed='seedString', bgColor=bg, foreColor=fore, spotColor=spot)
CreateIcon(option, './output.png')