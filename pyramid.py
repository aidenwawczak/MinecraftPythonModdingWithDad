from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 42
width = 8
height = 0
length = 8
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height, z + length - 1, blockType)
mc.setBlocks(x + 2, y + 2, z + 2, x + width - 2, y + height, z + length - 2, blockType)
mc.setBlocks(x + 3, y + 3, z + 3, x + width - 3, y + height, z + length - 3, blockType)
mc.setBlock(x + 4, y + 4, z + 4, 138)
