"""Make icns that can be used on macOS."""
import os
import pathlib
import cairosvg
from subprocess import PIPE, call


def _make_icns():
    for root, _, files in os.walk("./styles", topdown=False):
        for name in files:
            if name.endswith(".svg"):
                source = os.path.sep.join(pathlib.Path(root).parts)
                out_path = pathlib.Path("icns") / source
                if ("64" not in out_path.parts and
                        "scalable" not in out_path.parts):
                    continue

                png_path_128 = os.path.sep.join(out_path.parts)
                png_path_128 = png_path_128.replace("64", "128")

                os.makedirs(str(png_path_128), exist_ok=True)

                png_name = name.replace(".svg", ".png")
                png_path_128 = os.path.join(png_path_128, png_name)
                cairosvg.svg2png(
                    url=str(pathlib.Path(source) / name),
                    write_to=png_path_128,
                    output_width=128,
                    output_height=128
                )

                icn_path = png_path_128.replace(".png", ".ico")
                call(["png2icns", icn_path, png_path_128],
                     stdout=PIPE, stderr=PIPE)
                os.remove(png_path_128)


if __name__ == "__main__":
    _make_icns()
