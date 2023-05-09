# Aerofly RC7 Scenery Burgfalken
This is a fork of Cornelius Munz's repository "burgfalkenscenery".  
Its purpose is, to add some proper collision objects to this beautiful panorama.

## Remarks
I've got Aerofly RC7 running on Windows.  
Therefore the scenery is not tested/provided for RC8 or MacOS


## Install
To use the scenery extract the following zip file into your scenery folder   
of your local Aerofly RC installation:  
https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/rc7-burgfalken.zip


#### Target file location Windows, RC7
```C:\Benutzer\…..\Dokumente\aeroflyRC7\scenery``` (german)  
```C:\Users\…..\Documents\aeroflyRC7\scenery```    (common)


## Update
If you have already installed an older version of the burgfalke scenery, you can simply replace 2 files:
1.	```C:\Benutzer\…..\Dokumente\aeroflyRC7\scenery\burgfalken.tsc```  
	by https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/raw/burgfalken.tsc
	
2.	```C:\Benutzer\…..\Dokumente\aeroflyRC7\scenery\burgfalken\burgfalken.tgc```   
	by https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/raw/burgfalken/burgfalken.tgc 



After restarting Aerofly, you'll find the new/updated scenery in the user defined sceneries




# Version 1.1.0

## finished
- Written a blender python script, to produce the required mqo file from blender scene.  
  Writes a very simplyfied mqo format, since the mqo-to-tgc converter ignores most   
  of the scene/object properties anyway.
- Created CollisionObjects:
	- Groundgrid (not perfect, needs refinement later)
	- Some trees (not all, so far)
	- Huts and hedges
- Adjusted north direction and altitude 
- Defined startpositions for aiplanes and gliders (with winsh).

## to be done
- Implement missing trees 
- Define starting positions for Helis
- Define positions for contests (Limbo, baloon..)
- Refine groundgrid (optional)

