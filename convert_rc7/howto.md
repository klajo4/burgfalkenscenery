
## Install required software

- Download af5-developer-tools-v5050003.zip
- Unzip and copy the following two files into this directory  
	af5-mqo-to-tgc.exe  
	ipacs_export.lic
  



## Convert blender-scene to aerofly-scene

- Open burgfalken.blender
- Execute write_mqo_file.py  
  This will write burgfalken.mqo to the directory ../convert_rc7
- To generate burgfalken.tgc, execute from commandline  
  ```af5-mqo-to-tgc.exe  burgfalken```
- Copy the resulting file convert_rc7/burgfalken.tgc  
  to C:/Users/.../Documents/aerofly RC 7/scenery/burgfalken/burgfalken.tgc