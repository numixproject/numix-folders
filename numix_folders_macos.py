from pathlib import Path
import os
import pathlib
import cairosvg
from subprocess import PIPE, call


def _update():
    for root, _, files in os.walk("./styles", topdown=False):
        for name in files:
            if name.endswith(".svg"):
                source = "/".join(pathlib.Path(root).parts)
                filename = name
                dest = pathlib.Path("out") / source
                os.makedirs(dest, exist_ok=True)

                out_path = dest
                scalable = "scalable" in pathlib.Path(root).parts
                output_width = (str(pathlib.Path(root).parts[-2])
                                if not scalable else "64")
                output_height = (str(pathlib.Path(root).parts[-2])
                                 if not scalable else "64")
                png_name = filename.replace(".svg", ".png")
                png_path = str((out_path / png_name).absolute())

                if os.path.exists(png_path):
                    os.remove(png_path)

                if "64" in out_path.parts or "scalable" in out_path.parts:
                    png_path_128 = os.path.sep.join(out_path.parts)
                    png_path_128 = png_path_128.replace("64", "128")
                    os.makedirs(str(png_path_128), exist_ok=True)
                    png_path_128 = os.path.join(png_path_128, png_name)
                    cairosvg.svg2png(
                        url=str(pathlib.Path(source) / filename),
                        write_to=png_path_128,
                        output_width=128,
                        output_height=128
                    )

                    ico_path = png_path_128.replace(".png", ".ico")
                    call(["png2icns", ico_path, png_path_128],
                         stdout=PIPE, stderr=PIPE)

                cairosvg.svg2png(
                    url=str(pathlib.Path(source) / filename),
                    write_to=png_path,
                    output_width=int(output_width),
                    output_height=int(output_height)
                )


if __name__ == "__main__":
    _update()
