import bpy

#move vertex with the index 0 by 1 unit in positive x direction
bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0

#move vertex with the index 0 by 1 unit in positive y direction
bpy.data.objects["Cube"].data.vertices[0].co.y += 1.0

#move vertex with the index 0 by 1 unit in positive z direction
bpy.data.objects["Cube"].data.vertices[0].co.z += 1.0

