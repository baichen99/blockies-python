import cv2
import random
import math
import numpy
import hashlib

class Option:
  def __init__(self, size, scale, seed='seedstring', bgColor=None, foreColor=None, spotColor=None, mirror=None):
    # size 是一行的方格数量
    # scale 是一个方格所占像素数量
    self.size = size
    self.scale = scale
    self.width = size * scale
    self.height = size * scale
    self.mirror = mirror or True

    # 把seedstring转换成数字
    md5obj = hashlib.md5()
    md5obj.update(seed.encode('utf-8'))
    self.seed = md5obj.hexdigest()
    random.seed(int(self.seed, 16))

    self.bgColor = bgColor or createColor()
    self.foreColor = foreColor or createColor()
    self.spotColor = spotColor or createColor()

def file2num(path):
  with open(path,'rb') as f:
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
  return int(hash, 16)

def rand():
  r = random.random()
  random.seed(r)
  return r

def createColor():
  r = rand() * 255
  g = rand() * 255
  b = rand() * 255
  return [b, g, r]


def createImgData(option):
  data = numpy.zeros((option.size, option.size), dtype=numpy.int)
  for i in range(option.size):
    for j in range(option.size):
      # data == 0 bgColor
      # data == 1 foreColor
      # data == 2 spotColor
      # 这里*2.3 是让bgColor有 1/2.3的概率  spotColor有0.3/2.3的概率
      # 如果想增加spot出现概率, 可以增加这个数字，但是不能>=3
      data[i][j] = math.floor(rand()*2.3)
  return data

def createMirrorData(option):
  data = numpy.zeros((option.size, option.size), dtype=numpy.int)
  height = option.size
  width = option.size
  dataWidth = math.ceil(width / 2)
  mirrorWidth = width - dataWidth
  for i in range(height):
    row = [0] * dataWidth
    for j in range(dataWidth):
      row[j] = math.floor(rand()*2.3)
    r = row[0:dataWidth]
    r.reverse()
    row.extend(r)
    data[i,:] = row
  return data


def RenderImg(opt, data):
  def fillColor(row, col, color, scale):
    for i in range(row*scale, (row+1)*scale):
      for j in range(col*scale, (col+1)*scale):
        img[i,j,:] = color

  img = numpy.zeros((opt.height, opt.width, 3), dtype=numpy.uint8)
  for i in range(opt.size):
    for j in range(opt.size):
      if data[i, j] == 0:
        fillColor(i, j, opt.bgColor, opt.scale)
      elif data[i, j] == 1:
        fillColor(i, j, opt.foreColor, opt.scale)
      elif data[i, j] == 2:
        fillColor(i, j, opt.spotColor, opt.scale) 
  return img

def CreateIcon(opt, outputPath):
  if opt.mirror:
    data = createMirrorData(opt)
  else:
    data = createImgData(opt)
  img = RenderImg(opt, data)
  cv2.imwrite(outputPath, img)

if __name__ == '__main__':
  option = Option(size=8, scale=4, seed='seedstring')
  CreateIcon(option, './output.png')