# Aerofly RC7 and RC8 Scenery Burgfalken
This is a fork of Cornelius Munz's repository "burgfalkenscenery".  
Its purpose is, to add some proper collision objects to this beautiful panorama.


![picture of sceney](/blender/resources/scene.jpg)


## Install
**RC7:**
To install the scenery, extract the following zip file   
https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/rc7-burgfalken.zip  

into the user-scenery folder of your local Aerofly RC7 installation  
```C:\Benutzer\…..\Dokumente\aeroflyRC7\scenery``` 

**RC8:**
To install the scenery, extract the following zip file   
https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/rc8-burgfalken.zip  

into the user-scenery folder of your local Aerofly RC8 installation  
```C:\Benutzer\…..\Dokumente\aeroflyRC8\scenery``` 


## Update
If you have already installed an older version of the burgfalke scenery, you can simply replace 2 files:  

**RC7:**
1.	```C:\Benutzer\…..\Dokumente\aeroflyRC7\scenery\burgfalken.tsc```  
	by https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/raw_rc7/burgfalken.tsc  
	
2.  ```C:\Benutzer\…..\Dokumente\aeroflyRC7\scenery\burgfalken\burgfalken.tgc```   
	by https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/raw_rc7/burgfalken/burgfalken.tgc  

**RC8:**
1.	```C:\Benutzer\…..\Dokumente\aeroflyRC8\scenery\burgfalken.tsc```  
	by https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/raw_rc8/burgfalken.tsc  
	
2. 	```C:\Benutzer\…..\Dokumente\aeroflyRC8\scenery\burgfalken\burgfalken.tmb```   
	by https://github.com/klajo4/burgfalkenscenery/blob/master/scenery/raw_rc8/burgfalken/burgfalken.tmb  
	
	 
After restarting Aerofly, you'll find the new/updated scenery in the user defined sceneries  
  
  

## Version 1.1.0:

**finished**
- Written a blender python script, to produce the required mqo file from blender scene.  
  Writes a very simplyfied mqo format, since the mqo-to-tgc converter ignores most   
  of the scene/object properties anyway.
- Created CollisionObjects:
	- Groundgrid (not perfect, needs refinement later)
	- Some trees (not all, so far)
	- Huts and hedges
- Adjusted north direction and altitude 
- Defined startpositions for airplanes and gliders (with winsh).

**to be done**
- Implement missing trees 
- Define starting positions for helis
- Define positions for contests (Limbo, baloon..)
- Refine groundgrid (optional)

