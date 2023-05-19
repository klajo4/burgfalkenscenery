
## Install required software

- Download aerofly_fs_4_blender_plugin_20220715.zip from IPACS and install the plugin.
- Download aerofly_tutorial_3dmodel_to_rc8_part1.zip from IPACS and unzip it to a directory of your choice.
- Run the installer aerofly_rc_8_content_converter_x64_installer_2020-01-02.exe from the tools subdirectory.
- Choose "C:\AeroflyTools\Aerofly RC 8 Content Converter" as targetdirectory, 
  if you want convert_burgfalken.bat to work without changes.
  
  

## Convert blender-scene to aerofly-scene

- Open burgfalken.blender
- The following 2 steps is necessary, because the rc8-content-converter doesn't like local transforms:(
- Select all objects of the blender scene and perform "Apply all Transforms".
- Save the blender file under a new name e.g. burgfalken_temp.blend
- Now export burgfalken_temp.blend to convert_rc8/input/burgfalken.tgi (via the aerofly_fs_4_blender_plugin)
- Run convert_burgfalken.bat
- Copy the resulting file convert_rc8/output/burgfalken.tmb to  
C:/Users/.../Documents/aerofly RC 8/scenery/burgfalken/burgfalken.tmb


