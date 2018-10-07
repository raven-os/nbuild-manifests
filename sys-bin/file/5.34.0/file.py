from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::essentials/file#5.34.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="ftp://ftp.astron.com/pub/file/file-5.34.tar.gz",
            sha256="f15a50dbbfa83fec0bd1161e8e191b092ec832720e30cd14536e044ac623b20a",
        ),
    )
