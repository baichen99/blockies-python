# blockies

## introdution

blockies是一个生成块状图标的小程序库, 仿照[此项目](https://github.com/download13/blockies)所写的python版本

## Usage

```Python
from blockies.blockies import Option, CreateIcon

option = Option(size=12, scale=4, seed='seedString')
CreateIcon(option, './output.png')
```

### Use custom color

```Python
from blockies.blockies import Option, CreateIcon

bg = [233, 233, 233]
fore = [123, 123, 123]
spot = [22, 22, 22]
option = Option(size=12, scale=4, seed='seedString', bgColor=bg, foreColor=fore, spotColor=spot)
CreateIcon(option, './output.png')
```

### Create mirror icon

createIcon create a Mirror image by default, you can change that by passing mirror to option

```python
option = Option(size=12, scale=4, seed='seedString', mirror=False)
```
