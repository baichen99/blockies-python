from blockies.blockies import Option, CreateIcon

bg = [134, 85, 36]
fore = [245, 14, 249]
spot = [54, 52, 210]
option = Option(size=10, scale=4, seed='seedString', bgColor=bg, foreColor=fore, spotColor=spot)
CreateIcon(option, './output.png')