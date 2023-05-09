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
        
    """
    Object "obj1" {
        depth 0
        folding 0
        scale 1 1 1
        rotation 0 0 0
        translation 0 0 0
        visible 15
        locking 0
        shading 1
        facet 59.5
        color 0.898 0.498 0.698
        color_type 0
    """
    def write(self, file):                
        file.write("\nObject \"%s\" {" % (self.bo.name))
        #self.writeProperties(file)
        self.writeVertices(file)
        self.writeFaces(file)
        #self.writeFacesWithUV(file)        
        file.write("\n}")
        
    
    def writeProperties(self, file):          
        file.write("\n\tdepth 0")
        file.write("\n\tfolding 0")
        file.write("\n\tscale %.6f %.6f %.6f" % (self.bo.scale[0],  self.bo.scale[1],  self.bo.scale[2]))
        file.write("\n\trotation %.6f %.6f %.6f" % (self.bo.rotation_euler[0],  self.bo.rotation_euler[1],  self.bo.rotation_euler[2]))
        file.write("\n\ttranslation %.6f %.6f %.6f" % (self.bo.location[0],  self.bo.location[1],  self.bo.location[2]))
        file.write("\n\tvisible 15")
        file.write("\n\tlocking 0")
        file.write("\n\tshading 1")
        file.write("\n\tfacet 59.5")
        file.write("\n\tcolor 0.898 0.498 0.698")
        file.write("\n\tcolor_type 0")


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
        #eul = mathutils.Euler((radians(rotate_x), radians(rotate_y), radians(rotate_z)), 'XYZ')
        v_global.rotate(eul)             
        return v_global*scale  # scale up from meter to centimeter   
    
    '''
    v_local = object.data.vertices[_VERT_NUMBER_].co # local vertex coordinate
    v_global = object.matrix_world @ v_local # global vertex coordinates
    '''
        
     
     
     
def writeScene(file):
    file.write("\nScene {")
    file.write("\n\tpos 0 0 422212.34")
    file.write("\n\tlookat 0 0 0")
    file.write("\n\thead -0.6936")
    file.write("\n\tpich 0.4436")
    file.write("\n\tbank 0.0000")
    file.write("\n\tortho 0")
    file.write("\n\tzoom2 0.0178")
    file.write("\n\tamb 0.250 0.250 0.250")
    file.write("\n\tfrontclip 63331.855")
    file.write("\n\tbackclip 12666370")
    file.write("\n\tdirlights 1 {")
    file.write("\n\t\tlight {")
    file.write("\n\t\t\tdir 0.408 0.408 0.816")
    file.write("\n\t\t\tcolor 1.000 1.000 1.000")
    file.write("\n\t\t}")
    file.write("\n\t}")
    file.write("\n}")        


def writeMaterial(file):
    file.write("\nMaterial 2 {")
    file.write("\n\t\"mat1\" col(1.000 1.000 1.000 1.000) emi(0.000) spc(0.000)")
    file.write("\n\t\"Dekor\" col(1.000 1.000 1.000 1.000) dif(1.000) amb(0.250) emi(0.250) spc(0.000) power(5.00) tex(\"Dekor_color.bmp\")")
    file.write("\n}")
     
        
def main():
    
    """
    # print all scene names in a list
    print("===================\nAll scenes:")
    print(bpy.data.scenes.keys())
    """ 
     
    fs = open(path, 'w');

    
    fs.write("Metasequoia Document")
    fs.write("\nFormat Text Ver 1.1\n");
    
    #writeScene(fs)
    writeMaterial(fs)
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.hide_render==False:
            print(obj.name)
            mqo = MqoObject(obj)
            mqo.write(fs)

    fs.close()



        
if __name__ == "__main__":
    main()        