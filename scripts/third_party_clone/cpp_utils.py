import os
import shutil
import multiprocessing
import time


class install_cpp_utils:
    def __init__(self, d):
        self.d = d
        self.install_dir = "./third_party"

    def run(self):
        self.__install_csv_parser()
        self.__install_spdlog()

    def __install_spdlog(self):
        # https://github.com/gabime/spdlog.git
        path = self.install_dir + "/spdlog/spdlog"
        os.system("sudo rm -rf " + self.install_dir + "/spdlog")

        os.system(
            "git clone https://github.com/gabime/spdlog.git " + path)

        os.system("mkdir " + path + "/../build")
        os.system("mkdir " + path + "/../install")
        os.chdir(path + "/../build")
        os.system("cmake ../spdlog -DCMAKE_INSTALL_PREFIX=../install")

        num_cpu_cores = multiprocessing.cpu_count()
        os.system("make -j" + str(num_cpu_cores - 1))
        os.system("sudo make install")

        os.chdir("../../../")

    def __install_csv_parser(self):
        # https://github.com/ben-strasser/fast-cpp-csv-parser
        path = self.install_dir + "/fast-cpp-csv-parser"
        shutil.rmtree(path, ignore_errors=True)

        os.system(
            "git clone https://github.com/ben-strasser/fast-cpp-csv-parser.git " + path)
        os.system("mkdir ./src/log")
        shutil.copyfile(path + "/csv.h", "./src/log/csv.h")
