import zipfile
import pathlib
def make_archive(filepaths, dest_dir, name):
    if name.endswith('.zip'):
        name = name
    else:
        name += '.zip'
    dest_path = pathlib.Path(dest_dir,name)
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

