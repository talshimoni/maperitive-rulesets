from maperipy import App
App.log('script-dir: ' + App.script_dir)
App.run_command('change-dir dir="' + App.script_dir +'"')
App.run_command("run-script file=IsraelHiking.mscript")
# Map Created
App.run_command("generate-tiles minzoom=7 maxzoom=15 use-fprint=true")
App.log("=== Create a Zip file with new tiles ===")
App.run_command("zip zip-file=output\TileUpdate.zip")
App.log("=== Start uploading of tiles zoom 15 and below ===")
App.log('App.start_program("' + App.script_dir + '\UploadTiles.bat")')
App.start_program(App.script_dir + "\UploadTiles.bat")
App.log("=== Start creation of Oruxmap map ===")
App.log('App.start_program(App.script_dir + "\..\..\Mobile Atlas Creator\CreateIsraelHiking.bat", [])')
App.start_program(App.script_dir + "\..\..\Mobile Atlas Creator\CreateIsraelHiking.bat", [])
App.log("=== Create tiles for zoom 16 ===")
App.run_command("generate-tiles minzoom=16 maxzoom=16 use-fprint=true")
App.log("=== Create a Zip file with new tiles ===")
App.run_command("zip zip-file=output\TileUpdate16.zip")
App.log("=== Start uploading of tiles zoom 16 ===")
App.log('App.start_program("' + App.script_dir + '\UploadTiles.bat", "TileUpdate16.zip"])')
App.start_program(App.script_dir + "\UploadTiles.bat", ["TileUpdate16.zip"])