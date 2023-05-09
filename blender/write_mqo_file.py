# blender python script to write the required mqo file for the af5-mqo-to-tgc.exe converter
# Writes a very reduced mqo format, since the converter ignores most of the scenery/object attributes

# writes all rendered meshes (bpy.data.objects[objname].hide_render=false)




import bpy
import mathutils
from math import radians
import os


#path =  os.path.splitext(bpy.data.filepath)[0] + ".mqo"
path = "C:/Users/Klaus/Documents/aerofly RC 7/scenery/burgfalken/burgfalken.mqo"

scale = 100.0
 



class MqoObject:
    
    def __init__(self, blenderObject):        # bo = BlenderObject        
        self.bo = blenderObject
        
   
    def write(self, file):                
        file.write("\nObject \"%s\" {" % (self.bo.name))        
        self.writeVertices(file)
        self.writeFaces(file)
        #self.writeFacesWithUV(file)        
        file.write("\n}")   


    def writeVertices(self, file):   
        mesh = self.bo.data
        file.write("\n\tvertex %d {" % len(mesh.vertices))
        for vert in mesh.vertices:
            v_transf = self.transformVertex(vert)
            file.write("\n\t\t%.6f %.6f %.6f" % (v_transf[0], v_transf[1], v_transf[2]))
        file.write("\n\t}")
        
    def writeFaces(self, file):   
        mesh = self.bo.data        
        file.write("\n\tface %d {" % len(mesh.polygons))    
        for face in mesh.polygons:
            file.write("\n\t\t%d V(" % len(face.vertices))            
            '''
            for vertidx in face.vertices:
                file.write("%d " %(vertidx))
            '''
            #invert normals 
            # by writing first index and the rest from last to second 
            file.write("%d " %(face.vertices[0]))
            for i in range(len(face.vertices)-1,0,-1):
                 file.write("%d " %(face.vertices[i]))            
            file.write(")")
        file.write("\n\t}")
        
    
    
    ''' 
    writes out vertices with material and UV coordinates.    
    '''    
    def writeFacesWithUV(self, file):   
        mesh = self.bo.data
        uv_layer = mesh.uv_layers.active.data
        file.write("\n\tface %d {" % len(mesh.polygons))    
        for poly in mesh.polygons:            
            # range is used here to show how the polygons reference loops,
            # for convenience 'poly.loop_indices' can be used instead.
            vertices = list()
            for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
                vertices.append((mesh.loops[loop_index].vertex_index, uv_layer[loop_index].uv))
                #file.write("    Vertex: %d" % mesh.loops[loop_index].vertex_index)
                #file.write("    UV: %r" % uv_layer[loop_index].uv)    
            
            file.write("\n\t\t%d V(" % len(vertices))   
            file.write("%d " %(vertices[0][0])) 
            for i in range(len(vertices)-1,0,-1):
                 file.write("%d " %(vertices[i][0]))    
            file.write(")")   
            
            file.write(" M(0) ") 
            
            file.write(" UV(")   
            file.write("%f %f" %(vertices[0][1][0], vertices[0][1][1])) 
            for i in range(len(vertices)-1,0,-1):
                file.write(" %f %f" %(vertices[i][1][0], vertices[i][1][1]))  
            file.write(")")               
                    
        file.write("\n\t}")
        
        
        
    def transformVertex(self, vertex):        
        v_local = vertex.co # local vertex coordinate
        v_global = self.bo.matrix_world @ v_local # global vertex coordinates
        eul = mathutils.Euler((radians(-90.0), 0.0, 0.0), 'XYZ')
        v_global.rotate(eul)             
        return v_global*scale  # scale up from meter to centimeter   
    
# end of class MqoObject     




def writeMaterial(file):
    file.write("\nMaterial 1 {")
    file.write("\n\t\"mat1\" col(1.000 1.000 1.000 1.000) emi(0.000) spc(0.000)")
    file.write("\n}")
     
     
     
        
def main():
     
    fs = open(path, 'w');
    
    fs.write("Metasequoia Document")
    fs.write("\nFormat Text Ver 1.1\n");
    
    writeMaterial(fs)
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.hide_render==False:
            print(obj.name)
            mqo = MqoObject(obj)
            mqo.write(fs)

    fs.close()



        
if __name__ == "__main__":
    main()        